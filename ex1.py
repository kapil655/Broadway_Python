def duplicate(*data):
    result = []

    for i in data:
        if i in result:
            print("Duplicate found:", i)
            return True
        result.append(i)

    return False

print(duplicate(1, 2, 3, 1, 2, 1, 5, 5, 5, 5))