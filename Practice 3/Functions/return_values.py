
def check_even_odd(number):
    if number % 2 == 0:
        return "Четное"
    else:
        return "Нечетное"




def get_math_operations(a, b):
    sum_val = a + b
    diff_val = a - b
    return sum_val, diff_val





result = check_even_odd(7)
print(f"Число 7 - {result}")





total, difference = get_math_operations(10, 4)
print(f"Сумма: {total}, Разность: {difference}")