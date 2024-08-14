#creating blueprint(class)
#class consists of 2 things - propertys and function    
class Person():
    #propertys
    age=26
    height=180
    name=""

    #creating constructor function
    def __init__(self,age,height,name):
        print("constructor function called")
        self.age = age 
        self.height = height
        self.name = name

    def update_details(self):
        self.age = input("what is your age?  :")
        self.height = input("what is your height(cm)? : ")
        self.name = input("what is your name? : ")

    def show_details(self):
        print(f"my age is {self.age}")
        print(f"my height is {self.height}")
        print(f"my name is {self.name}")


#creating the object using the person class
sarbjit = Person(30,170,"sarbjit")
print(sarbjit.age)
#calling the funtions-using object name.funtion name
sarbjit.show_details()
sarbjit.update_details()
sarbjit.show_details()bbvbnbgn  3

#creating another object
gurasees = Person(13,155,"gurasgcvvcccrvfgfgghghhghgfdeees")
print(gurasees.height)
gurasees.show_details()
gurasees.update_details()
gurasees.show_details()






if x=*/ypr then */*to if med controldd
