# a=[1,2,3,4,5]
# print(a)
# print(type(a))
# print(a[-1])
# print(a[-2])
# print(a[-3])
# print(a[-4])


# name=["kapil","dev",1,2,3,4,5,6]
# print(name[1:3])
# print(name[:])
# print(name[::2])
# print(name[-1:0])



data1=["kapil","dev"]
data1.append("joshi")
data1.append("mahendranagar")
data1.append("kapil")
print("append...................",data1)

#insert
data=[1,2,3,4,5]
data.insert(0,90)
print("insert...................",data)
data.insert(100,500)
print("insert...................",data)

#extend
a = [1, 2, 3]
b = [4, 5, 6]

a.extend(b)
print("extend.......................", a)

print(a)

#concat(+)
print("concat.................",a+b)


#del,remove,pop,clear
data=[1,2,3,4,5,6]
del data[0]
print("del.....................",data)

data.remove(6)
print("Remove.................",data)

data.pop(3)
print("pop ..............",data)



#clear
data.clear()
print(data)