def second_largest(*args):
    unique_nums = list(set(args))
    if len(unique_nums) <2:
        return None
    unique_nums.sort()
    return unique_nums[-2]

print(second_largest(10, 5, 8, 20, 15))     
print(second_largest(1, 2, 3, 3, 2, 1))   
print(second_largest(5, 5, 5))
print(second_largest(5, 5))

