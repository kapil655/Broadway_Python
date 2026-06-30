def add(*sum):
    print(type(sum))
    print(sum)
    return sum

add(1,2,3,4,5,6)
add(1,2,3,4,5,6,7,8,9)
add(1,2,3,4,5,6,"kapil","hello")
print("------------------------------------")
a=[1,2,3,4,5,6,7,8,9]
print(sum(a))

print("=======================================")

def add_num(*data):
    print(data)
    total=0
    for i in data:
        total+=i
    return total

add_num(1,2,3,4,5,6,7,8,9)


print("////////////////////////")
#add only positive number

def add_positive(*data):
    print(data)
    total=0
    for i in data:
        if i <= 0:
            continue
            total+=i
        
    return total


add_positive(1,2,3,4,5,6,-8,-6)


def info (**args):
    print(args)
    return len(args)
    

info(name="kapil",greet="hello",age=23,roll=19)
info(name="kapil",greet="hello")
info(name="kapil")
