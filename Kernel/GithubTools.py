from github import Auth, Github, GithubIntegration
from Kernel.Logger import logger
import os, sys
import requests
import difflib
import asyncio

GITHUB_TOKEN = ""
KEY = ""
if os.path.exists(os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), "github_pat.txt")):
    with open(os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), "github_pat.txt"), "r") as f:
        GITHUB_TOKEN = f.read().strip()
        
if os.path.exists(os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), "key.pem")):
    with open(os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), "key.pem"), "r") as f:
        KEY = f.read().strip()
    
REPO_NAME = "IntelliMarkets/Wallpaper_API_Index"
GITHUB_APP_ID = "2220480"

async def get_github_instance(token: str = None, private_key: str = None, installation_id: int = None, verify: bool = True):
    """
    根据token获取github实例（异步版本）
    """
    logger.info(f"尝试使你登录……")
    
    # 使用 asyncio.to_thread 将同步操作包装为异步
    def _create_github_instance():
        if private_key and installation_id:
            logger.debug(f"Mode: auth, private_key: True, installation_id: True")
            auth = Auth.AppAuth(GITHUB_APP_ID, private_key)
            g = Github(auth=Auth.AppInstallationAuth(auth, installation_id), verify=verify)
            # g.get_user().login
            return g
        elif token:
            logger.debug(f"Mode: token, token: True")
            return Github(token, verify=verify)
        else:
            logger.debug(f"Mode: default, token: False, private_key: False, installation_id: False")
            return Github(verify=verify)
    
    # 在单独的线程中执行创建操作，避免界面卡死
    return await asyncio.to_thread(_create_github_instance)

def get_repo(github_instance, repo_name):
    """
    获取仓库
    """
    try:
        repo = github_instance.get_repo(repo_name)
        return repo
    except Exception as e:
        print(f"Error getting repository: {e}")
        return None
    

async def get_folder_list(repo, branch="main") -> list:
    """
    获取指定分支中所有的文件夹列表
    """
    return await _get_base(repo, branch, type="dir")

async def get_file_list(repo, branch="main", dir_path="") -> list:
    """
    获取指定分支中指定目录的文件列表
    """
    return await _get_base(repo, branch, type="file", dir_path=dir_path)
    
async def _get_base(repo, branch, type="dir", dir_path=""):
    try:
        contents = await asyncio.to_thread(repo.get_contents, dir_path, ref=branch) # 获取指定目录的内容
        folder_list = []
        while contents:
            file_content = contents.pop(0)
            
            if file_content.type == type:
                folder_list.append(file_content.path)  

        return folder_list
    except Exception as e:
        print(f"Error getting {type} list: {e}")
        return []


def download_folder(repo, folder_path, local_path, branch="main"):
    """
    下载指定文件夹中的全部内容到本地
    """
    try:
        contents = repo.get_contents(folder_path, ref=branch)
        while contents:
            file_content = contents.pop(0)
            if file_content.type == "dir":
                os.makedirs(os.path.join(local_path, file_content.path), exist_ok=True)
                download_folder(repo, file_content.path, local_path, branch)
            else:
                file_url = file_content.download_url
                if file_url:
                    response = requests.get(file_url)
                    response.raise_for_status()  # 检查获取是否成功
                    to_local_path = file_content.path.split(r'/')
                    to_local_path = os.path.join(*to_local_path[1:]) if len(to_local_path) > 1 else file_content.path
                    filepath = os.path.join(local_path, to_local_path)

                    os.makedirs(os.path.dirname(filepath), exist_ok=True) # 确保目录存在
                    with open(filepath, "wb") as f:
                        f.write(response.content)
                    print(f"Downloaded: {file_content.path}")
    
    except requests.exceptions.ConnectionError or requests.exceptions.ConnectTimeout as e:
        e_message = f'''您目前暂时无法连接至插件中心，因为 raw.githubusercontent.com 连接失败或超时。
您可能需要代理或镜像服务以加速您的链接。详细信息：
{e}'''
        raise Exception(e_message)
        
    except Exception as e:
        print(f"Error downloading folder {folder_path}: {e}")
        raise


def check_file_exists(repo, file_path, branch="main"):
    """
    检测指定文件是否存在于存储库
    """
    try:
        repo.get_contents(file_path, ref=branch)
        return True
    except Exception as e:
        if e.status == 404:  # 文件未找到
            return False
        else:
            print(f"Error checking file existence: {e}")
            return False

async def get_file_content(repo, repo_file_path, branch="main"):
    """
    获取远程文件内容
    """
    try:
        file_content = await asyncio.to_thread(repo.get_contents, repo_file_path, ref=branch)
        remote_content = file_content.decoded_content.decode('utf-8')
        return remote_content
    except Exception as e:
        print(f"Error getting file content: {e}")
        return None


def compare_file_content(repo, repo_file_path, local_file_path, branch="main"):
    """
    将指定文件的内容与本地文件对比，返回差异
    """
    try:
        # 获取远程文件内容
        remote_content = get_file_content(repo, repo_file_path, branch)
        
        # 读取本地文件内容
        with open(local_file_path, 'r', encoding='utf-8') as f:
            local_content = f.read()

        # 比较文件内容
        if remote_content == local_content:
            print("Files are identical.")
            return None
        else:
            # 使用 difflib 生成差异
            diff = difflib.unified_diff(local_content.splitlines(), remote_content.splitlines(), fromfile="local", tofile="remote")
            return "\n".join(diff)

    except FileNotFoundError:
        print(f"Local file not found: {local_file_path}")
        return None
    except Exception as e:
        print(f"Error comparing file content: {e}")
        return None



# if __name__ == '__main__':
#     # 初始化 GitHub 客户端
#     g = get_github_instance(GITHUB_TOKEN)

#     # 获取仓库
#     repo = get_repo(g, REPO_NAME)

#     if repo:
#         # 获取所有文件夹
#         folder_list = get_folder_list(repo, branch="main")
#         print("Folder List:", folder_list)

#         # 下载指定文件夹
#         folder_to_download = "docs" # 远程文件夹
#         local_download_path = "downloaded_files"  # 本地文件夹
#         download_folder(repo, folder_to_download, local_download_path, branch="main")

#         # 检查文件是否存在
#         file_to_check = "README.md" 
#         exists = check_file_exists(repo, file_to_check, branch="main")
#         print(f"File '{file_to_check}' exists: {exists}")

#         # 比较文件内容
#         repo_file = "README.md" # 远程文件
#         local_file = "local_README.md" # 本地文件

#         # 先创建一个本地文件，用于对比
#         with open(local_file, "w") as f:
#             f.write("This is a local README file for testing.\n")

#         diff = compare_file_content(repo, repo_file, local_file, branch="main")

#         if diff:
#             print("Differences between files:\n", diff)
#         else:
#             print("No differences found or files are identical.")