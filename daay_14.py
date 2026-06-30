#Encapsulation
class Test:
    __password = "Kapil!joshi@#EDFFCD"
    __name="Kapil joshi"
    password = __password
    name=__name

    def login(self):
        pwd = self.__password
        print("Password:", pwd)
        return True
    
    def data(self):
        return self.login()
    
    def name(self):
        nm=self.__name
        print("name is :",nm)
        return True

class test1(Test):
    def display(self):
        return self.password, self.data()

obj = Test()
print(obj.password)