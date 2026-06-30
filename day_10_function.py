#function 
#positional argument
def add(a,b):
    c=a+b
    print("sum is :",c)
add(10,20)

#keyword argument
def user_info(fname, lname):
    return f'my name is {fname } {lname}'

print(user_info(fname="kapil",lname="joshi"))


def add1():
    return 1,"hello",105,'c',[1,2,3,5]


#default agument
def area(r,pie=3.14):
    return pie * r*r

print(area(7))
print(area(7,4))

def add_no(data):
        global sum
        sum=0
        for i in data:
            sum= sum+i
        
            return data
    

print(add_no([1,2,3,4,5]))
print(sum)