
import os
import openai
from dotenv import load_dotenv
from prompt import completion_prompt


load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")



def completion_api_predict(comment) -> str:
  response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt= completion_prompt + f"Comment - {comment}",
    temperature=0,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  return response["choices"][0]["text"]