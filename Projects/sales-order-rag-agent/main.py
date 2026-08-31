import os
from dotenv import load_dotenv
from google import genai


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def search_policy(question):

    with open("sales_order_policy.txt", "r") as file:
        policy = file.read()

    question_words = question.lower().split()

    relevant_lines = []

    for line in policy.splitlines():

        for word in question_words:

            if len(word) > 3 and word in line.lower():
                relevant_lines.append(line)
                break

    return "\n".join(relevant_lines)

question = input("Enter your question: ")

result = search_policy(question)

print("\nRetrieved information:")
print(result)

#Take retrived information and give it to Gemini so Gemini can formulate the answer.
# For true semantic RAG system

prompt = f"""
Answer the user's question using only the information provided below.

User question:
{question}

Retrieved information:
{result}
"""


response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)


print("\nFinal answer:")
print(response.text)