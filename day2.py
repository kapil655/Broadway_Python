# Type casting 
a="123"
b=int(a)
print(type(a))
print(b)
print(type(b))

#type validation
num=100
print(isinstance(num,int))
print(isinstance(num,str))

name="kapil"
print(isinstance(name,str))
print(isinstance(name,int))


# operator 
a=int(input("enter the power size:"))
b=int(input("enter the number:"))
print("the power is",b**a)

c=11
d=2
print(c/d)
print(c*d)
print(c+d)
print(c-d)


#operator in string
print("kapil "+" joshi")
print("kapil "*2)

#comparison
print(5<5)
print(2>4)
print(6==3)
print(5!=5)
print(5<=5)
print(2>=4)
print("10//3 is",10//3)

print("comparison op",5==3 and 4==4)
print(5 and 0)
print(0 and 3)
print(0 or 6)
print(not 0)