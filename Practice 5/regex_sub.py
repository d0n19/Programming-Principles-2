import re

txt = "The rain in Spain"

res_all = re.sub(r"\s", "9", txt)
print(f"Total sub: {res_all}") 

res_limited = re.sub(r"\s", "9", txt, 2)
print(f"First to subs: {res_limited}")
