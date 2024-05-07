import requests

def send_request(api_key, user_input):
    url = "https://api.openai.com/v1/moderations"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "input": user_input
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()

# 使用示例
api_key = "sk-"
user_input = "操你妈"

result = send_request(api_key, user_input)
### 为true表示触达敏感词，false表示正常语句.
print(result["results"][0]['flagged'])
