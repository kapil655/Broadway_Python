class Parent:
    a = 10
    b = 20

    def display(self):
        return "Hello this is return"

    def add(self):
        return self.a + self.b


class Child(Parent):
    a = 5
    c = 30
    d = 40

# Object creation must be outside the class
obj = Child()

print(obj.a)
print(obj.c)
print(obj.d)
print(obj.b)
print(obj.display())
print(obj.add())













