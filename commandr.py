#module for easy api calls to cohere
import cohere, os, json
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("COHERE_API")

bot = cohere.Client(api_key)

def getJSON(preamble, prompt):
    api_message = bot.chat(
        model='command-r-08-2024',  
        message = prompt,
        temperature=0.3,  
        preamble=preamble
    )

    readable_message = api_message.json()
    response_data = json.loads(readable_message)['text']
    text_data = response_data.strip() 
    print(text_data)
    message_part = json.loads(text_data)

    return message_part