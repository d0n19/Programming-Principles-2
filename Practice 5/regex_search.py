import re

txt = "The rain in Spain"
x = re.search("\s", txt)
if x:
    print("The first white-space character is located in position:", x.start())
else:
    print(None)