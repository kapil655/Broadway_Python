# Loop
for i in "kapil":
    print(i)


a = {
    "program":"c",
    "type":"compiler"
}

for i in a.values():
    print(i)

for i,j in a.items():
    print(i,j)
print("========================================================================")
for i in [1,2,3,4,5,6]:
    if i== 4 :
        break
    print(i)
print("========================================================================")
for i in [1,2,3,4,5,6]:
    if i== 4 :
        continue
    print(i)

print("========================================================================")
for i in [1,2,3,4,5,6,7,8,9,10]:
    if i%2==0:
        print(i)
        break

    elif i %2 !=0:
        print(i)


print("========================================================================")
#range
for i in range(1,10):
    print(i)
print("------------------------------------------------")
for i in range (1,10,2):
    print(i)



for i in range(1,11):
    print(f"2*{i}=",2*i)
    # print("2 X",i,"=",2*i)

name = input(" enter any name ")
print(type(name))

num=int(input(" enter "))
print(type(num))




#nested for
print("-----------------------")
for i in [1,2,3]:
    for j in [4,5,6]:
        print(i,j,end="\n")
    print("--------------")


