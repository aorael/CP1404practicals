from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

print()
languages = [ProgrammingLanguage("Python", "Dynamic", True, 1991), ProgrammingLanguage("Ruby", "Dynamic", True, 1995), ProgrammingLanguage("Visual Basic", "Static", False, 1991)]
print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name) #printing the name only