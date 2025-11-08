import sys, os, asyncio
import traceback
import uuid, webbrowser
import qasync, json, aiohttp
from PySide6.QtWidgets import (QApplication, QDialog, 
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSpacerItem, QSizePolicy)
from PySide6.QtCore import (QCoreApplication, QSize, Qt, Signal, QTimer)
from PySide6.QtGui import (QIcon, QPixmap, QFont)

from qfluentwidgets import (NavigationItemPosition, MessageBox, SubtitleLabel, 
    InfoBar, NavigationBar, CardWidget, SwitchButton, PrimaryPushButton, InfoBarPosition)
from qfluentwidgets import FluentIcon as FIF
from functools import partial

if __name__ == "__main__":
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UI.MarketTemplate_ui import Ui_Form
from UI.SearchTemplate_ui import Ui_SearchTemplate
from Kernel.GithubKernal import Markets
from Kernel.Logger import logger
from Kernel.SettingsKernal import SettingsKernal
from Kernel import MainKernal
searching = False

class MarketUI(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.plugin_containers = []
        self.loop = qasync.QEventLoop(self)
        self.icon_cache = {}  # 图标缓存字典 {url: pixmap_data}
        self.max_cache_size = 50  # 最大缓存数量
        self.exclude_apis = []  # 排除的 API 列表
        
        asyncio.set_event_loop(self.loop)
        
        self.NavigationBar.addItem("overview", FIF.TILES, "概览", onClick=lambda: self.on_NavigationBar_changed("//overview"))
        self.NavigationBar.addItem("location", FIF.BOOK_SHELF, "已添加", position=NavigationItemPosition.BOTTOM, onClick=lambda: self.on_NavigationBar_changed("//location"))
        self.NavigationBar.setCurrentItem("overview")
        self.verticalLayout_2.addItem(self.verticalSpacer_9)
        
        self.SearchButton.setEnabled(False)
        self.SearchBox.setEnabled(False)
        
        self.ProgressLine.show()
        self.RestartButton.hide()
        self.SearchButton.setIcon(FIF.SEARCH)
        # self.SearchButton.clicked.connect(lambda: asyncio.create_task(self.on_search_clicked()))
        # self.SearchBox.returnPressed.connect(lambda: asyncio.create_task(self.on_search_clicked()))
        self.SearchButton.clicked.connect(self.on_search_clicked)
        self.SearchBox.returnPressed.connect(self.on_search_clicked)
        self.WikiButton.clicked.connect(lambda: webbrowser.open("https://github.com/SRON-org/APICORE/wiki/Create-a-New-APICORE-Configuration-File/"))
        self.MarketButton.clicked.connect(lambda: webbrowser.open("https://github.com/IntelliMarkets/Wallpaper_API_Index/"))
        self.RestartButton.clicked.connect(lambda: MainKernal.restart_program(self))
        # self.RestartButton.clicked.connect(self.parent.restartSubInterface)
        
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(lambda: asyncio.create_task(self.init_markets()))
        self.timer.start(0)
            
        plm = Plugin_UI_Manager(self)
        setattr(self, 'addPlugin', plm.addPlugin)
        setattr(self, 'delPlugin', plm.delPlugin)
        
        # test
        # self.addPlugin("插件1", "这是插件1的介绍", u".//NewIcon.ico", True, "启用", self.delPlugin)
        # self.delPlugin()
        # self.addPlugin("插件1", "这是插件1的介绍", u"image: url(:/ICO/NewIcon.ico);", True, "启用", lambda: print("插件1被点击"))

    async def init_markets(self):
        self.markets = Markets(self.parent.settings)
        await self.markets.init()
        await self.markets.get_classification()
        self.init_Navigation(self.markets.classification)
        
        # self.verticalLayout_2.addWidget(self.ProgressLine)
        try:
            async for api in self.markets.get_all_apis():
                content = {}
                try: 
                    content = json.loads(api["content"])
                except:
                    pass
                
                self.timer = QTimer(self)
                self.timer.setSingleShot(True)
                self.timer.timeout.connect(
                    lambda content=content: self.addPlugin(content.get("friendly_name", "API"), content.get("intro", "没有介绍。"), content.get("icon", ""), None, f"{'更新/修复/删除' if os.path.isfile(os.path.join(MainKernal.get_config_dir(), 'EnterPoint', api.get('name', '') + '.api.json')) else '添加到 壁纸生成器'}", 
                    lambda _, path=api.get("name", ""), content=content: self.on_add_clicked(path, content, "overview")) 
                    if api["category"] == self.NavigationBar.getCurrentItem()['text'] or "overview" in self.NavigationBar.getCurrentItem()['routeKey'] else None)
                self.timer.start(0)
                
        except Exception as e:
            logger.error(f"获取 API 列表失败: {str(e)}")
            logger.debug(traceback.format_exc())
            
        if hasattr(self.parent, 'apis_updated'):
            self.parent.apis_updated.emit(self.markets.apis)
        self.NavigationBar.addItem("refresh", FIF.UPDATE, "刷新", position=NavigationItemPosition.BOTTOM, onClick=self.restart_markets) 
        self.SearchButton.setEnabled(True)
        self.SearchBox.setEnabled(True)
        self.ProgressLine.hide()
        
    def init_Navigation(self, classifications):
        if not hasattr(self.NavigationBar, "getCurrentItem"):
            def getCurrentItem():
                for k, widget in self.NavigationBar.items.items():
                    if widget.isSelected:
                        return {"routeKey": k, "text": widget._text}
                    
            setattr(self.NavigationBar, "getCurrentItem", getCurrentItem)
            # setattr(self.NavigationBar.getCurrentItem, "routeKey", lambda: getCurrentItem()["name"])
            # setattr(self.NavigationBar.getCurrentItem, "text", lambda: getCurrentItem()["text"])
            
        for i, c in enumerate(classifications):
            handler = partial(self.on_NavigationBar_changed, f"{c}")
            self.NavigationBar.addItem(
                f"tag_{i}", 
                FIF.TAG, 
                c, 
                onClick=lambda *args, handler=handler: handler()
            )
        
    def restart_markets(self):
        self.delPlugin()
        index = self.verticalLayout.indexOf(self.NavigationBar)
        self.NavigationBar.deleteLater()
        self.NavigationBar = NavigationBar(self.scrollAreaWidgetContents_2)
        self.NavigationBar.setObjectName(u"NavigationBar")
        self.NavigationBar.setMaximumSize(QSize(72, 16777215))
        self.verticalLayout.insertWidget(index, self.NavigationBar)
        
        self.SearchButton.setEnabled(False)
        self.SearchBox.setEnabled(False)
        
        self.icon_cache = {}
        self.NavigationBar.addItem("overview", FIF.TILES, "概览", onClick=lambda: self.on_NavigationBar_changed("//overview"))
        self.NavigationBar.addItem("location", FIF.BOOK_SHELF, "已添加", position=NavigationItemPosition.BOTTOM, onClick=lambda: self.on_NavigationBar_changed("//location"))
        self.NavigationBar.setCurrentItem("overview")
        self.ProgressLine.show()
        
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(lambda: asyncio.create_task(self.init_markets()))
        self.timer.start(0)
    
    def _get_item_list(self, source):
        if "overview" in source:
            return [item for sublist in self.markets.apis.values() 
                    if isinstance(sublist, list) for item in sublist]
        
        elif "location" in source:
            items = []
            for path in SettingsKernal.Construct_control(SettingsKernal, path=os.path.join(MainKernal.get_config_dir(), "EnterPoint")):
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        items.append({'name': os.path.basename(path), 'content': content})
                except Exception as e:
                    logger.error(f"无法读取文件 {path}: {str(e)}")
            return items
        elif isinstance(source, str):
            return self.markets.apis.get(source, [])
        
        return []
    
    def process_and_display_items(self, items, item_id, exclude_apis=None, filter_text=None):
        self.delPlugin()
        for api in items:
            try:
                content = json.loads(api.get("content", "{}"))
            except (json.JSONDecodeError, TypeError):
                content = {}
            
            if filter_text:
                filter_text_lower = filter_text.lower()
                name_match = filter_text_lower in api.get("name", "").lower()
                friendly_match = filter_text_lower in content.get("friendly_name", "").lower()
                intro_match = filter_text_lower in content.get("intro", "").lower()
                link_match = filter_text_lower in content.get("link", "").lower()
                if not (name_match or friendly_match or intro_match or link_match):
                    continue 
            
            api_basename = api.get("name", "") if api.get("name", "").endswith(".api.json") else f"{api.get('name', '')}.api.json"
            self.addPlugin(
                content.get("friendly_name", "API"), 
                content.get("intro", "没有介绍。"), 
                content.get("icon", ""), 
                (api_basename not in self.exclude_apis) if "location" in item_id else None, 
                "删除" if "location" in item_id else f"{'更新/修复/删除' if os.path.isfile(os.path.join(MainKernal.get_config_dir(), 'EnterPoint', api.get('name', '') + '.api.json')) else '添加到 壁纸生成器'}", 
                lambda _, path=api.get("name", ""), content=content: self.on_remove_clicked(path, content, item_id) if "location" in item_id 
                else self.on_add_clicked(path, content, item_id), 
                lambda state, api_basename=api_basename, : self.on_checked_changed(state, api_basename))

    def on_NavigationBar_changed(self, item_id):
        items = self._get_item_list(item_id)
        if os.path.isfile(os.path.join(MainKernal.get_config_dir(), "EnterPoint", "exclude.txt")):
            with open(os.path.join(MainKernal.get_config_dir(), "EnterPoint", "exclude.txt"), "r", encoding="utf-8") as f:
                self.exclude_apis = [line.strip() for line in f.readlines()]
        logger.debug(f"排除的API: {self.exclude_apis}")
        self.process_and_display_items(items, item_id, exclude_apis=self.exclude_apis)
            
    def on_checked_changed(self, state, name):
        logger.debug(f"on_checked_changed: {name}")
        if name in self.exclude_apis:
            self.exclude_apis.remove(name)
            InfoBar.info(title='已启用', content=f""""{name}" 已启用。\n请重启 壁纸生成器 后生效。""", orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.BOTTOM_RIGHT,
                    duration=4000, 
                    parent=self.window()
                )
            # if sys.platform == "win32": self.RestartButton.setText("手动重启 (退出)")
            self.RestartButton.show()
            
        else:
            self.exclude_apis.append(name)
            InfoBar.info(title='已禁用', content=f""""{name}" 已禁用。\n请重启 壁纸生成器 后生效。""", orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.BOTTOM_RIGHT,
                    duration=4000, 
                    parent=self.window()
                )
            # if sys.platform == "win32": self.RestartButton.setText("手动重启 (退出)")
            self.RestartButton.show()
            
        try:
            with open(os.path.join(MainKernal.get_config_dir(), "EnterPoint", "exclude.txt"), "w", encoding="utf-8") as f:
                f.write("\n".join(self.exclude_apis))
        except Exception as e:
            logger.error(f"写入排除列表失败: {str(e)}")
            MessageBox("错误", f"""无法禁用/启用图片源，请检查目录写入权限是否给予。\n使用管理员身份运行此程序可能有助于解决此问题。""", self.window())
            
            
    def on_add_clicked(self, name, content, item_id):
        name = f"{name}.api.json" if not name.endswith(".api.json") else name
        if os.path.isfile(os.path.join(MainKernal.get_config_dir(), "EnterPoint", name)):
            msg = MessageBox("提示", f"""图片源 "{content.get('friendly_name', name)}" 已经添加过啦 ♪(´▽｀)\n你可以进行以下操作""", self.window())
            msg.yesButton.setText("更新/修复")
            msg.cancelButton.setText("删除图片源")
            if not msg.exec():
                self.on_remove_clicked(name, content, item_id)
                return
        
        msg = MessageBox("添加图片源", f"""确定要添加图片源 "{content.get('friendly_name', name)}"吗？""", self.window())
        msg.setClosableOnMaskClicked(True)
        if msg.exec():
            new_source = os.path.join(MainKernal.get_config_dir(), "EnterPoint", name)
            with open(new_source, 'w', encoding='utf-8') as f:
                f.write(json.dumps(content, ensure_ascii=False, indent=2, default=str))
                f.close()
                
            InfoBar.info(title='已添加', content=f""""{content.get('friendly_name', name)}" 已添加到 壁纸生成器。\n请重启 壁纸生成器 后生效。""", orient=Qt.Horizontal,
                        isClosable=True,
                        position=InfoBarPosition.BOTTOM_RIGHT,
                        duration=4000, 
                        parent=self.window()
                    )
            # if sys.platform == "win32": self.RestartButton.setText("手动重启 (退出)")
            self.RestartButton.show()
        
    def on_remove_clicked(self, name, content, item_id):
        name = f"{name}.api.json" if not name.endswith(".api.json") else name
        if not os.path.isfile(os.path.join(MainKernal.get_config_dir(), "EnterPoint", name)):
            MessageBox("错误", f"""图片源 "{os.path.join(MainKernal.get_config_dir(), "EnterPoint", name)}" 不存在。""", self.window())
            return
        
        msg = MessageBox("提示", f"""确定要删除图片源 "{content.get('friendly_name', name)}" 吗？""", self.window())
        msg.setClosableOnMaskClicked(True)
        if msg.exec():
            os.remove(os.path.join(MainKernal.get_config_dir(), "EnterPoint", name))
            InfoBar.info(title='已删除', content=f""""{content.get('friendly_name', name)}" 已从 壁纸生成器 中移除。\n请重启 壁纸生成器 后生效。""", orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.BOTTOM_RIGHT,
                    duration=4000, 
                    parent=self.window()
                )
            # if sys.platform == "win32": self.RestartButton.setText("手动重启 (退出)")
            self.RestartButton.show()
            
            if "location" in item_id:
               self.on_NavigationBar_changed("//location") 

    async def on_search_clicked_next(self):    
        BatchWindow = QDialog()
        BatchWindow.setWindowTitle("搜索结果")
        BatchWindow.setWindowIcon(QIcon(".\\NewIcon.ico"))
        ui1 = SearchUI(BatchWindow, self, self.SearchBox.text())
        BatchWindow.show()
        # Keep reference to prevent garbage collection
        setattr(self, '_search_dialog', BatchWindow)
        
    def on_search_clicked(self):
        current_nav_item = next((k if not "tag" in k else widget._text for k, widget in self.NavigationBar.items.items() 
                                if widget.isSelected), None)

        if current_nav_item:
            items = self._get_item_list(current_nav_item)
            self.process_and_display_items(items, filter_text=self.SearchBox.text(), item_id=current_nav_item)
        else:
            items = self._get_item_list("//overview")
            self.process_and_display_items(items, filter_text=self.SearchBox.text(), item_id="//overview")
        

    def _(self):
        pass
    
class SearchUI(QDialog, Ui_SearchTemplate):
    # Semaphore to limit concurrent tasks
    _semaphore = asyncio.Semaphore(3)
    
    def __init__(self, parent: QDialog=None, p=None, keyword=None):
        super().__init__(parent)
        self.setupUi(parent)
        self.parent = p
        # self.verticalLayout_2.addWidget(self.verticalSpacer_9)
        self.SearchButton.setIcon(FIF.SEARCH)
        self.SearchButton.clicked.connect(lambda: asyncio.create_task(self.on_search_clicked()))
        self.SearchBox.returnPressed.connect(lambda: asyncio.create_task(self.on_search_clicked()))
        
        plm = Plugin_UI_Manager(self)
        setattr(self, 'addPlugin', plm.addPlugin)
        setattr(self, 'delPlugin', plm.delPlugin)
        
        self.plugin_containers = []
        self.loop = qasync.QEventLoop(self)
        self.icon_cache = p.icon_cache  # 图标缓存字典 {url: pixmap_data}
        self.max_cache_size = 50  # 最大缓存数量
        asyncio.set_event_loop(self.loop)
        self.search_queue = []
        
        if keyword is not None:
            self.SearchBox.setText(keyword)
            asyncio.create_task(self.on_search_clicked())
        
    async def on_search_clicked(self):
        search_id = uuid.uuid4().hex
        self.search_queue = [search_id]
        self.ProgressLine.show()
        self.delPlugin()
        async with self._semaphore:
            try:
                async for content in self.parent.markets.search_api(self.SearchBox.text()):
                    if search_id not in self.search_queue:
                        return  # Search was cancelled
                    
                    # Schedule UI update in main thread
                    def update_ui():
                        if search_id in self.search_queue: 
                            self.addPlugin(
                                content.get("friendly_name", "API"), 
                                content.get("intro", "没有介绍。"), 
                                content.get("icon", ""), 
                                None, 
                                "添加到 壁纸生成器", 
                                None)
                    
                    QTimer.singleShot(0, update_ui)
                    QApplication.processEvents()
                    
                if search_id in self.search_queue:
                    QTimer.singleShot(0, self.ProgressLine.hide)
                    
            except Exception as e:
                logger.error(f"Search error: {str(e)}")
                if search_id in self.search_queue:
                    self.ProgressLine.hide()
        
class Plugin_UI_Manager(object):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        
    def addPlugin(self, title: str, intro: str, icon: str, is_enabled: any, 
                 action_text: str, action_func = None, change_usability_func = None):
        try:
            if hasattr(self.parent, 'verticalSpacer_9') and self.parent.verticalSpacer_9 is not None:
                if self.parent.verticalLayout_2.indexOf(self.parent.verticalSpacer_9) != -1:
                    self.parent.verticalLayout_2.removeItem(self.parent.verticalSpacer_9)
        except RuntimeError:
            pass

               
        # 查找可用空间的容器
        container = None
        for c in self.parent.plugin_containers:
            if c.count() < 2:
                container = c
                break
        
        if container is None:
            new_container = QHBoxLayout()
            self.parent.plugin_containers.append(new_container)
            self.parent.verticalLayout_2.insertLayout(self.parent.verticalLayout_2.count()-1, new_container)
            container = new_container
        
        # Create plugin card with original layout structure
        Label_Plugin_Card_ = CardWidget(self.parent.scrollAreaWidgetContents) # CardWidget(self.parent.parent.scrollAreaWidgetContents)
        Label_Plugin_Card_.setObjectName(f"Label_Plugin_Card_{container.count()}")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Label_Plugin_Card_.sizePolicy().hasHeightForWidth())
        Label_Plugin_Card_.setSizePolicy(sizePolicy)
        Label_Plugin_Card_.setMinimumSize(QSize(0, 0))
        Label_Plugin_Card_.setMaximumSize(QSize(16777215, 16777215))
        verticalLayout_11 = QVBoxLayout(Label_Plugin_Card_)
        verticalLayout_11.setObjectName(u"verticalLayout_11")
        Plugins_Internal_Container = QVBoxLayout()
        Plugins_Internal_Container.setObjectName(u"Plugins_Internal_Container")
        verticalSpacer_12 = QSpacerItem(20, 3, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        Plugins_Internal_Container.addItem(verticalSpacer_12)

        Plugin_Title = SubtitleLabel(f" {title}", Label_Plugin_Card_)
        Plugin_Title.setObjectName(u"Plugin_Title")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(Plugin_Title.sizePolicy().hasHeightForWidth())
        Plugin_Title.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"HarmonyOS Sans SC"])
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setKerning(True)
        font2.setStyleStrategy(QFont.PreferAntialias)
        Plugin_Title.setFont(font2)
        Plugin_Title.setToolTipDuration(-1)
        Plugin_Title.setToolTip(title)

        Plugins_Internal_Container.addWidget(Plugin_Title)

        verticalSpacer_13 = QSpacerItem(20, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        Plugins_Internal_Container.addItem(verticalSpacer_13)

        Plugins_Internal_Container1 = QHBoxLayout()
        Plugins_Internal_Container1.setObjectName(f"Plugins_Internal_Container_{container.count()}")
        horizontalSpacer_20 = QSpacerItem(7, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        Plugins_Internal_Container1.addItem(horizontalSpacer_20)

        verticalLayout_15 = QVBoxLayout()
        verticalLayout_15.setObjectName(u"verticalLayout_15")
        Plugin_Icon = QLabel(Label_Plugin_Card_)
        Plugin_Icon.setObjectName(u"Plugin_Icon")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(Plugin_Icon.sizePolicy().hasHeightForWidth())
        Plugin_Icon.setSizePolicy(sizePolicy2)
        Plugin_Icon.setMinimumSize(QSize(60, 60))
        Plugin_Icon.setMaximumSize(QSize(60, 16777215))
        
        # 缓存机制，异步加载图片
        async def async_load():
            try:
                if icon in self.parent.icon_cache:
                    cached_data = self.parent.icon_cache[icon]
                    pixmap = QPixmap()
                    if pixmap.loadFromData(cached_data):
                        pixmap = pixmap.scaled(60, 60, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                        Plugin_Icon.setPixmap(pixmap)
                        return

                if icon.startswith(("data:img/", "data:image/")):
                    try:
                        import base64
                        base64_data = icon.split(",")[1]
                        data = base64.b64decode(base64_data)
                        self.parent.icon_cache[icon] = data
                        if len(self.parent.icon_cache) > self.parent.max_cache_size:
                            oldest_key = next(iter(self.parent.icon_cache))
                            del self.parent.icon_cache[oldest_key]
                        
                        pixmap = QPixmap()
                        if pixmap.loadFromData(data):
                            pixmap = pixmap.scaled(60, 60, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                            Plugin_Icon.setPixmap(pixmap)
                            return
                    except Exception as e:
                        logger.error(f"解码base64图片失败: {e}")
                        return
                else:
                    # 原有URL处理逻辑
                    async with aiohttp.ClientSession() as session:
                        async with session.get(icon) as resp:
                            if resp.status == 200:
                                data = await resp.read()
                                self.parent.icon_cache[icon] = data
                                if len(self.parent.icon_cache) > self.parent.max_cache_size:
                                    oldest_key = next(iter(self.parent.icon_cache))
                                    del self.parent.icon_cache[oldest_key]
                                
                                pixmap = QPixmap()
                                if pixmap.loadFromData(data):
                                    pixmap = pixmap.scaled(60, 60, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                                    Plugin_Icon.setPixmap(pixmap)
                                    
            except Exception as e:
                logger.error(f"加载图片失败: {e}")
                # 从缓存中移除无效条目
                if icon in self.parent.icon_cache:
                    del self.parent.icon_cache[icon]
        
        # 使用asyncSlot包装异步函数
        if icon: asyncio.create_task(async_load())
        Plugin_Icon.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        verticalLayout_15.addWidget(Plugin_Icon)

        verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Ignored)

        verticalLayout_15.addItem(verticalSpacer)


        Plugins_Internal_Container1.addLayout(verticalLayout_15)

        horizontalSpacer_21 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        Plugins_Internal_Container1.addItem(horizontalSpacer_21)

        verticalLayout_13 = QVBoxLayout()
        verticalLayout_13.setObjectName(u"verticalLayout_13")
        Plugin_Intro = SubtitleLabel(intro, Label_Plugin_Card_)
        Plugin_Intro.setObjectName(u"Plugin_Intro")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(Plugin_Intro.sizePolicy().hasHeightForWidth())
        Plugin_Intro.setSizePolicy(sizePolicy3)
        Plugin_Intro.setMinimumSize(QSize(0, 75))
        font3 = QFont()
        font3.setFamilies([u"HarmonyOS Sans SC"])
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setKerning(True)
        font3.setStyleStrategy(QFont.PreferAntialias)
        Plugin_Intro.setFont(font3)
        Plugin_Intro.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        Plugin_Intro.setWordWrap(True)
        Plugin_Intro.setToolTipDuration(-1)
        Plugin_Intro.setToolTip(intro)

        verticalLayout_13.addWidget(Plugin_Intro)

        horizontalLayout_6 = QHBoxLayout()
        horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        if isinstance(is_enabled, bool):
            AbilityButton = SwitchButton(Label_Plugin_Card_)
            AbilityButton.setObjectName(u"AbilityButton")
            AbilityButton.setOnText(QCoreApplication.translate("Form", u"\u542f\u7528", None))
            AbilityButton.setOffText(QCoreApplication.translate("Form", u"\u7981\u7528", None))
            AbilityButton.setChecked(is_enabled)
            if change_usability_func is not None:
                AbilityButton.checkedChanged.connect(change_usability_func)
                
            horizontalLayout_6.addWidget(AbilityButton)

        horizontalSpacer_5 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        horizontalLayout_6.addItem(horizontalSpacer_5)

        ActionButton = PrimaryPushButton(action_text, Label_Plugin_Card_)
        if action_func is not None:
            ActionButton.clicked.connect(action_func)
        ActionButton.setObjectName(u"ActionButton")

        horizontalLayout_6.addWidget(ActionButton)
        horizontalSpacer_6 = QSpacerItem(5, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        horizontalLayout_6.addItem(horizontalSpacer_6)
        verticalLayout_13.addLayout(horizontalLayout_6)
        Plugins_Internal_Container1.addLayout(verticalLayout_13)
        Plugins_Internal_Container.addLayout(Plugins_Internal_Container1)
        verticalLayout_11.addLayout(Plugins_Internal_Container)
        
        # Add card to container
        container.addWidget(Label_Plugin_Card_)
        self.parent.verticalLayout_2.addItem(self.parent.verticalSpacer_9)
        
        # Update UI
        self.parent.scrollAreaWidgetContents.adjustSize()
        
    def delPlugin(self):
        """Remove all plugins from the interface"""
        # Remove all widgets from each container
        for container in self.parent.plugin_containers:
            while container.count():
                item = container.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
            
        # Reset to initial state with just one empty container    
        self.parent.plugin_containers = []
        self.parent.scrollAreaWidgetContents.adjustSize()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    market = MarketUI()
    market.show()
    sys.exit(app.exec())