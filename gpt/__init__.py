import openai
import os

key = os.environ.get("OPEN_API_KEY")
if key:
    openai.api_key = key
    model = openai.ChatCompletion()
    print("Openai API Activated!")
else:
    print("No Key Founded!")