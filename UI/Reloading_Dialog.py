from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from qfluentwidgets import (CardWidget, IndeterminateProgressBar, IndeterminateProgressRing, TitleLabel)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(419, 241)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.CardWidget = CardWidget(Form)
        self.CardWidget.setObjectName(u"CardWidget")
        self.verticalLayout_2 = QVBoxLayout(self.CardWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.IndeterminateProgressRing = IndeterminateProgressRing(self.CardWidget)
        self.IndeterminateProgressRing.setObjectName(u"IndeterminateProgressRing")
        self.IndeterminateProgressRing.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.IndeterminateProgressRing)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.TitleLabel = TitleLabel(self.CardWidget)
        self.TitleLabel.setObjectName(u"TitleLabel")
        font = QFont()
        font.setFamilies([u"HarmonyOS Sans SC Black"])
        font.setPointSize(21)
        font.setBold(True)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setTextFormat(Qt.AutoText)
        self.TitleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.TitleLabel)

        self.IndeterminateProgressBar = IndeterminateProgressBar(self.CardWidget)
        self.IndeterminateProgressBar.setObjectName(u"IndeterminateProgressBar")

        self.verticalLayout_2.addWidget(self.IndeterminateProgressBar)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.verticalLayout.addWidget(self.CardWidget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"正在快速重启", None))
    # retranslateUi

