def check_skill(skill):
    if skill == "Python":
        return "Core programming skill"
    elif skill == "AI":
        return "Future-focused skill"
    elif skill == "GitHub":
        return "Collaboration skill"
    else:
        return "Other useful skill"

skills = ["Python", "Git", "GitHub", "AI", "Excel"]

for skill in skills:
    print(skill, "->", check_skill(skill))
