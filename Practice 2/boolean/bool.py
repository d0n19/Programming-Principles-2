print(10 > 9)
print(10 == 9)
print(10 < 9)


print(bool("Привет"))
print(bool(15))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

def is_ready():
  return True

if is_ready():
  print("Готово!")
else:
  print("Не готово!")

x = 200
print(isinstance(x, int))