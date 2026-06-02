# Writing to a file
with open("skills.txt", "w") as f:
    f.write("Python\n")
    f.write("Git\n")
    f.write("AI\n")

# Reading from a file
with open("skills.txt", "r") as f:
    content = f.read()
    print("File content:\n", content)

# Reading line by line
with open("skills.txt", "r") as f:
    for line in f:
        print("Skill:", line.strip())
