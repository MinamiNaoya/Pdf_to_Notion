import requests
import json

class Notion:
    def __init__(self, notion_token):
        self.headers = {
            'Notion-Version': '',
            'Authorization': 'Bearer ' + notion_token
        }
    headers = {
        'Notion-Version': '2023-04-23'
    }
    BASE_URL = "https://api.notion.com/v1"
    
        
    @staticmethod    
    def response_or_error(response, key: str = None):
        response_json = response.json()
        
        if "message" in response.json():
            message = response_json["message"]
            return {
                "code": response.status_code,
                "error": message
            }
        
        json_response = response_json()
        
        if key is not None:
            return json_response[key]
        
        return json_response    
      
    @classmethod   
    def search_page(self, page_title: str = None):
        url = self.BASE_URL + "/search"
        body = {}
        if page_title is not None:
            body["query"] = page_title
        # responseはpageのプロパティやidを含む
        response = requests.request("POST", url, headers=self.headers, params=body)
        return self.response_or_error(response)
    
    # 空白のブロックの追加
    @classmethod
    def append_child_blocks(self, parent_id: str, children:dict):
        url = self.BASE_URL + f"/blocks/{parent_id}/children"
        response = requests.request(
            "PATCH",
            url, 
            headers=self.headers,
            json={"children": children}
        )
        return response
    
    @classmethod
    def text_append(self, parent_id: str, text: str):
        text_block = {
            "type": "paragraph",
            "paragraph":{
                "text":[{
                    "type": "text",
                    "text":{
                        "content": text
                    }
                }]
            }
        }
        return self.append_child_blocks(parent_id, children=[text_block])
    
    @classmethod
    def update_block(self, block_id: str, content:dict):
        url = self.BASE_URL + f"/blocks/{block_id}"
        response = requests.request("PATCH", url, headers=self.headers, json=content)
        return self.response_or_error(response)
    
    @classmethod
    def text_set(self, block_id: str, new_text: str):
        block = self.get_block(block_id)
        type = block["type"]
        block[type]["text"][0]["text"]["content"] = new_text
        return self.update_block(block_id, block)
    
    
    # URLとimage fileを紐づけた状態で渡さなければならない。
    @classmethod
    def image_add(self, parent_id: str, image_url: str):
        append_children = [
            {
                "type": "image",
                "image": {
                    "type": "external",
                    "external":{
                        "url": image_url
                    }
                }
            }
        ]
        return self.append_child_blocks(parent_id, append_children)
      
    @classmethod    
    def delete_block(self, block_id: str):
        url = self.BASE_URL + f"/blocks/{block_id}"
        response = requests.request("DELETE", url, headers=self.headers)
        return response
    
    @classmethod
    def update_image(self, old_image_block_id: str, parent_id: str, new_image_url: str):
        self.delete_block(old_image_block_id)
        self.image_add(parent_id, new_image_url)
        
    def createPage(self, databaseId, headers):
        createUrl = 'https://api.notion.com/v1/pages'
        newPageData = {
            "parent": { "database_id": databaseId },
            "properties": {
                "Description": {
                    "title": [
                        {
                            "text": {
                                "content": "Review"
                            }
                        }
                    ]
                },
                "Value": {
                    "rich_text": [
                        {
                            "text": {
                                "content": "Amazing"
                            }
                        }
                    ]
                },
                "Status": {
                    "rich_text": [
                            {
                            "text": {
                                "content": "Active"
                            }
                        }
                    ]
                }
            }
        }
    
        data = json.dumps(newPageData)
        # print(str(uploadData))
        response = requests.request("POST", createUrl, headers=headers, data=data)
        return self.response_or_error(response)
    
    def updatePage(self, pageId, headers):
        updateUrl = f"https://api.notion.com/v1/pages/{pageId}"
        
        updateData = {
            "properties": {
                "Value": {
                    "rich_text": [
                        {
                            "text": {
                                "content": "Pretty Good"
                            }
                        }
                    ]
                }
            }
        }
        
        data = json.dumps(updateData)
        
        response = requests.request("PATCH", updateUrl, headers=headers, data=data)
        
        return self.response_or_error(response)


