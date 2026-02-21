def sum_all_numbers(*args):
    total = sum(args)
    print(f"Сумма переданных чисел {args} равна: {total}")





def print_student_info(**kwargs):
    print("Информация о студенте:")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")





sum_all_numbers(1, 2, 3)
sum_all_numbers(10, 20, 30, 40, 50)

print_student_info(name="Сара", major="Computer Science", gpa=3.8)