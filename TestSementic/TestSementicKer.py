import os
import asyncio

from dotenv import load_dotenv

from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

from weather_plugin import WeatherPlugin
from calendar_plugin import CalendarPlugin

load_dotenv()


async def TestSementicker():

    kernel = Kernel()

    kernel.add_service(
        OpenAIChatCompletion(
            service_id="chat",
            api_key=os.getenv("OPENAI_API_KEY"),
            ai_model_id="gpt-5-mini"
        )
    )

    kernel.add_plugin(
        WeatherPlugin(),
        plugin_name="Weather"
    )

    kernel.add_plugin(
        CalendarPlugin(),
        plugin_name="Calendar"
    )

    prompt = """
    User request:
    {{$input}}

    Use available tools when needed.
    """

    function = kernel.add_function(
        plugin_name="Assistant",
        function_name="HandleRequest",
        prompt=prompt
    )

    result = await kernel.invoke(
        function,
        input="""
        Find today's weather in Mumbai,
        check my calendar,
        and schedule a meeting tomorrow if it's not raining.
        """
    )

    print(result)


asyncio.run(TestSementicker())