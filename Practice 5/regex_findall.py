import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(f"Matches found: {x}") 

y = re.findall("Portugal", txt)

if not y:
    print("No matches found, returned an empty list:", y)
else:
    print("Matches found:", y)