n=lambda x,y : x+y
print(n(1,5))

a=[1,2,3,4,5,6,7,8,9]
output=[]
for i in a:
    output.append(i)
print(output)

data=[i * i for i in a]
print(data)

n=lambda *a :[i*i for i in a]
print(n(1,2,3,4,5,6))
