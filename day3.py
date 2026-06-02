# Function to greet
def greet(name):
    return f"Hello, {name}!"

# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Function to show tools
def show_tools(tools):
    for tool in tools:
        print("Tool:", tool)

# --- Using functions ---
skills = ["Python", "Git", "GitHub", "AI"]

for skill in skills:
    print(greet(skill))

print("Sum of 5 and 7 is:", add_numbers(5, 7))

tools = ["VS Code", "Git", "Python"]
show_tools(tools)
