#Python code with Semantic Kernel

import asyncio
import os
from dotenv import load_dotenv

from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

load_dotenv()

async def main():
    kernel = Kernel()

    kernel.add_service(
        OpenAIChatCompletion(
            service_id="chat",
            api_key=os.getenv("OPENAI_API_KEY"),
            ai_model_id="gpt-5-mini"
        )
    )

    prompt = "Answer the following question: {{$input}}"

    chat_function = kernel.add_function(
        plugin_name="ChatPlugin",
        function_name="Answer",
        prompt=prompt
    )

    result = await kernel.invoke(
        chat_function,
        input="What is today?"
    )

    print(result)

asyncio.run(main())