import json

# Sample data (like ERP records or AI config)
employee = {
    "name": "Abhinav",
    "role": "AI Engineer",
    "skills": ["Python", "ERP", "Agentic AI"],
    "experience": 8
}

# --- Write JSON to file ---
with open("employee.json", "w") as f:
    json.dump(employee, f, indent=4)

# --- Read JSON from file ---
with open("employee.json", "r") as f:
    data = json.load(f)

print("Employee Name:", data["name"])
print("Role:", data["role"])
print("Skills:", ", ".join(data["skills"]))
print("Experience:", data["experience"], "years")
