from semantic_kernel.functions import kernel_function

class WeatherPlugin:

    @kernel_function(description="Get weather for a city")
    def get_weather(self, city: str) -> str:
        return f"{city}: Sunny, 32°C, no rain expected."