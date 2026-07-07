# Day 22 - Multi-Agent Workflow Foundations
# Objective: Demonstrate basic agent communication and logging

import datetime

# --- Agent Definitions ---
class AgentA:
    def fetch_data(self):
        # Simulate fetching data (e.g., from an API)
        return "The quick brown fox jumps over the lazy dog."

class AgentB:
    def analyze_data(self, data):
        # Simple analysis: count words and characters
        words = len(data.split())
        chars = len(data)
        return f"Data analyzed: {words} words, {chars} characters."

# --- Logging Function ---
def log_action(agent_name, action, result):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("agent_log.txt", "a") as log:
        log.write(f"[{timestamp}] {agent_name} - {action}: {result}\n")

# --- Workflow Execution ---
if __name__ == "__main__":
    agent_a = AgentA()
    agent_b = AgentB()

    data = agent_a.fetch_data()
    log_action("AgentA", "Fetched Data", data)

    analysis = agent_b.analyze_data(data)
    log_action("AgentB", "Analyzed Data", analysis)

    print("Workflow complete. Check 'agent_log.txt' for details.")
