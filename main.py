import os
import openai


openai.api_key =  os.getenv('API-KEY')


response = openai.Completion.create(engine="davinci", prompt="This is", max_tokens=5)

# returns an object 
