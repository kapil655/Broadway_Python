def number_add(a,b):
    result = a+b
    return result


print(number_add(10,30))

def test():...#empty function

def test1():#empty function
    pass


a=[1,2,3,4,5,6]
print(type(a))

print(len(a))

a=()
print(type(a))

a=[1,2,3,4,5]
b=list(a)
b.append(10)
b[0]=5


print(b)
a=tuple(b)
print(a)

a={"hello","kapil","sisaiya","college",1,1,1,1,1,1,1,1,1,1,1}
a.remove(1)
print(a)
print(type(a))
a={}
print(type(a))
a=set()
print(type(a))


a=[1,2,3,4,5,6,1,2,3]
b=set(a)
print(b)
a=list(b)
print(type(a))
print(type(b))