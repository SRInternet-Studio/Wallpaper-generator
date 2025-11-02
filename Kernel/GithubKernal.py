import os, sys, asyncio, json
if __name__ == "__main__":
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Kernel.GithubTools import *
from Kernel.Logger import logger

class Markets(object):
    def __init__(self, settings: dict):
        self.github_instance = None
        self.repo = None
        self.classification = None
        self.apis = {}
        self.installation_id = settings.get("installation_id", None)

    async def init(self):
        self.github_instance = await get_github_instance(GITHUB_TOKEN, KEY, self.installation_id, verify=False)
        self.repo = get_repo(self.github_instance, REPO_NAME)
        if self.repo is None:
            self.github_instance = await get_github_instance(verify=False)
            logger.error("Failed to get repo")
            return
        
    async def get_classification(self):
        self.classification = await get_folder_list(self.repo)
        
    async def get_all_apis(self):
        summary = 0
        self.apis
        for folder in self.classification:
            current_files = await get_file_list(self.repo, "main", folder)
            self.apis[folder] = []
            for file in current_files:
                if file.endswith(".api.json"):
                    logger.info(f"Getting {file} content...")
                    summary += 1
                    paths = file.split("/")
                    api_name = paths[-1].split(".")[0]
                    api_content = await get_file_content(self.repo, file, "main")
                    self.apis[folder].append({"name": api_name, "content": api_content, "category": folder})
                    yield {"name": api_name, "content": api_content, "category": folder}
        self.apis["//summary"] = summary
        
    async def search_api(self, filter_text: str):
        query = f"repo:{REPO_NAME} filename:api.json"
        search_results = await asyncio.to_thread(self.github_instance.search_code, query)
        print(f"已搜索 {search_results.totalCount} 个 API 文件")
        batch_size = 10
        files = list(search_results)

        for i in range(0, len(files), batch_size):
            batch = files[i:i+batch_size]
            tasks = []
            for file in batch:
                tasks.append(self._process_search_file(file, filter_text))
                
            results = await asyncio.gather(*tasks)
            for content in results:
                if content is not None:
                    yield content
                    
    async def _process_search_file(self, file, filter_text):
        api = str(file.name)
        try:
            content = await asyncio.to_thread(
                lambda: json.loads(file.decoded_content.decode('utf-8'))
            )
        except Exception:
            return None
            
        if filter_text:
            filter_text_lower = filter_text.lower()
            name_match = filter_text_lower in api.lower()
            friendly_match = filter_text_lower in content.get("friendly_name", "").lower()
            intro_match = filter_text_lower in content.get("intro", "").lower()
            link_match = filter_text_lower in content.get("link", "").lower()
            
            if not (name_match or friendly_match or intro_match or link_match):
                return None
                
        return content
            
# if __name__ == "__main__":
#     markets = Markets()
#     asyncio.run(markets.init())
#     asyncio.run(markets.get_classification())
#     print(asyncio.run(markets.get_all_apis()))