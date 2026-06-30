def filter_strings(**kwargs):
    result = {}

    for key, value in kwargs.items():
        if isinstance(value, str):
            result[key] = value

    return result

print(filter_strings(name="kapil", surname="joshi", roll=20, age=23))


def all_args(data,*args,**kwargs):
    print(args)
    print(kwargs)
    print(data)
print("------------------")
all_args(1,2,3,2,2,2,2,2,22,2,2,5,58,85556,5,555,5,5,5,name="kapil")