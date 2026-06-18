#OpenAI Python SDK Test

from openai import OpenAI
from dotenv import load_dotenv
import os


# Load variables from .env
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


'''client = OpenAI(
  api_key="KEY-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
)'''

response = client.responses.create(
  model="gpt-5.4-mini",
  input="How to say hello?",
  store=True,
)

print(response.output_text);
