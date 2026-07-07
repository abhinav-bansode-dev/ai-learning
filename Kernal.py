import requests
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from langchain_core.prompts import PromptTemplate
from langchain import LLMChain
from langchain_openai import ChatOpenAI
from autogen import AssistantAgent

# -----------------------------
# Step 1: Fetch Invoices (Northwind OData)
# -----------------------------
url = "https://services.odata.org/V4/Northwind/Northwind.svc/Invoices"
response = requests.get(url, headers={"Accept": "application/json"})
data = response.json()
invoices = data["value"][:5]  # take first 5 invoices

# -----------------------------
# Step 2: Semantic Kernel orchestration
# -----------------------------
kernel = Kernel()
kernel.add_text_completion_service(
    "openai", OpenAIChatCompletion("gpt-4", api_key="YOUR_KEY")
)

# Register ERP fetch as a skill
def fetch_invoices():
    return invoices

kernel.register_semantic_function("erp", "fetch_invoices", fetch_invoices)

# -----------------------------
# Step 3: LangChain summarization
# -----------------------------
llm = ChatOpenAI(model="gpt-4", api_key="YOUR_KEY")

prompt = PromptTemplate(
    input_variables=["data"],
    template="Summarize these invoices:\n{data}"
)

chain = LLMChain(llm=llm, prompt=prompt)
summary = chain.run(data=invoices)
print("LangChain Summary:\n", summary)

# -----------------------------
# Step 4: AutoGen two-agent setup
# -----------------------------
fetcher = AssistantAgent(name="Fetcher", llm_config={"model":"gpt-4"})
def fetcher_func(msg):
    return invoices
fetcher.register_function("get_invoices", fetcher_func)

analyzer = AssistantAgent(name="Analyzer", llm_config={"model":"gpt-4"})

analyzer.initiate_chat(
    fetcher,
    message="Please provide invoices and generate a summary report."
)
