my_list = ["apple", "banana", "cherry"]
my_iter = iter(my_list)

print("First item:", next(my_iter))
print("Second item:", next(my_iter))


print("\nLooping through the rest:")
for item in my_iter:
    print(item)







class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
print("\nCustom Iterator:")
for num in iter(myclass):
    print(num)







def countdown(num):
    print("Starting countdown...")
    while num > 0:
        yield num
        num -= 1

print("\nGenerator Function:")
for val in countdown(3):
    print(val)









gen_expr = (x ** 2 for x in range(4))
print("\nGenerator Expression:")
print(next(gen_expr)) # 0
print(next(gen_expr)) # 1
print(next(gen_expr)) # 4
