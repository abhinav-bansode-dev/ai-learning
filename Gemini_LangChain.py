from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
from openai import api_key


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model = "gemini-3.5-flash",
    temperature=0.7,
    google_api_key = api_key
)

#First section for 'Simple Prompt' with 'ChatGoogleGenerativeAI' model.

prompt = "Suggest me a skill that is in demand?"
response = llm.invoke(prompt)
print(" Suggested Skill:\n", response)

#Second section for 'dynamic prompt where {year} can be replaced with input values.

template = "Give me 3 career skills that are in high demand in {year}."
prompt_template = PromptTemplate.from_template(template)

parser = StrOutputParser() #Parser object

chain = prompt_template | llm | parser

response = chain.invoke({"year": "2026"})
print("\n Career Skills in 2026:\n", response)