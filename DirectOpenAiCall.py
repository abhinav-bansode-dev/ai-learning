from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

try:
    response = client.responses.create(
        model="gpt-5-mini",
        input="Tell me a joke"
    )

    print(response.output_text)

except Exception as e:
    print(e)