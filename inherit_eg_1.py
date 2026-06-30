class parent():
    a=10
    b=20
    def display(self):
        return "I am from parent class"
    
class parent1():
    def display(self):
        return "i am from parent1 class"

class child(parent,parent1):
    a=30

obj=child()
print(obj.display())