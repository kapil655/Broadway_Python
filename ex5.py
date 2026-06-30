def average_even(*args):
    total = 0
    count = 0

    for i in args:
        if i % 2 == 0:
            total += i
            count += 1

    if count == 0:
        return None

    return total / count

print(average_even(1, 2, 3, 4, 5))  # 3.0
