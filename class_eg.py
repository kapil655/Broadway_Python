class Test():
    a=10
    b=11

obj1=Test()
print(obj1)
obj1.name="kapil"
print(obj1.name)


obj2=Test()
print(obj2)
obj2.c=100

print(obj2.c)
print(obj1.c) #shows an error
print(obj1 == obj2) 
