def student_mark(*args, **kwargs):
    total = sum(args)
    percentage = total / len(args)
    return f'{kwargs["name"]} percentage is {percentage:.2f}%'


print(student_mark(100, 40, 50, 60, 70, 80, name="hari"))
print(student_mark(100, 40, 50, 60, 70, 80, 90, 75, 85, name="subash"))