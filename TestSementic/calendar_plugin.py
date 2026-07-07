from semantic_kernel.functions import kernel_function

class CalendarPlugin:

    @kernel_function(description="Check available calendar slots")
    def check_availability(self) -> str:
        return "Tomorrow 2 PM - 3 PM is available."

    @kernel_function(description="Create a meeting")
    def create_meeting(self, time: str) -> str:
        return f"Meeting scheduled at {time}"