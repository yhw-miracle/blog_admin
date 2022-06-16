import os
import sys
import math
import json
import requests


def get_data(api_base_url = "http://121.5.42.99:8002"):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    apis = [
        {"name": "home", "url": f"{api_base_url}/"},
        {"name": "category", "url": f"{api_base_url}/category/"},
        {"name": "tag", "url": f"{api_base_url}/tag/"},
        {"name": "reading_notes", "url": f"{api_base_url}/reading_notes/"},
    ]
    for api in apis:
        response = requests.get(url=api["url"], headers=headers)
        if response.content:
            data = response.json()
            if api["name"] == "home":
                home_data = dict()
                pagesize = 10
                count = data["count"]
                page_count = math.ceil(count / pagesize)
                home_data[1] = data
                for current_page in range(1, page_count):
                    res = requests.get(url=api["url"], params={"currentPage": current_page + 1}, headers=headers)
                    if res.content:
                        home_data[current_page + 1] = res.json()
                save_file(api["name"], home_data)

                articles_by_hash = dict()
                for page, page_content in home_data.items():
                    for article in page_content["articles"]:
                        res = requests.get(url=f"{api_base_url}/article/", params={"id": article["hash"]})
                        if res.content:
                            if article["hash"] not in articles_by_hash.keys():
                                articles_by_hash[article["hash"]]= res.json()
                save_file("articles_by_hash", articles_by_hash)
                
                res = requests.get(url=api["url"], params={"by_year": True}, headers=headers)
                if res.content:
                    articles_by_year = res.json()
                    save_file("articles_by_year", articles_by_year)
            else:
                save_file(api["name"], data)
    
def save_file(name, data):
    if os.path.exists(os.path.join(os.getcwd(), "blog_data")) is False:
        os.makedirs(os.path.join(os.getcwd(), "blog_data"))
    
    with open(os.path.join(os.getcwd(), "blog_data", f"{name}.json"), "w", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False))


if __name__ == "__main__":
    # print(sys.argv)
    get_data()
