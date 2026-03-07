import re

txt = "The rain in Spain"

x = re.split(r"\s", txt)
print(f"Full split: {x}") 

y = re.split(r"\s", txt, 1)
print(f"Maxsplit 1: {y}")
