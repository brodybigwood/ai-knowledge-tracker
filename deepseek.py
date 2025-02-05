
import requests, json, os
from dotenv import load_dotenv

load_dotenv()

model_name = "deepseek-r1-distill-llama-70b-websearch"
url = f"https://deadlock.p.nadles.com/{model_name}/completion"


api_token = os.getenv("DEEPSEEK_API")

headers = {
    "Content-Type": "application/json",
    "x-billing-token": api_token
}

def getJSON(preamble, prompt):
    data = {
        "messages": [
            {
                "role": "user",
                "content": preamble+' '+prompt
            }
        ],
        "max_tokens": 2048,
        "temperature": 0.7,
        "top_p": 0.9,
        "stream": False,
        "search_web": False
    }

    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()
    print(response_json)
    content = response_json["model_response"]["choices"][0]["message"]["content"]

    if response.status_code == 200:
    
        # just in case the ai forgets to write it in plaintext
        json_start = content.find("```json") + len("```json")
        json_end = content.find("```", json_start)
        json_str = content[json_start:json_end].strip()


        result = json.loads(json_str)

 
        return json.dumps(result, indent=2)
    else:
        print("Error:", response.status_code, response.text)
        return 'Network Error'
    