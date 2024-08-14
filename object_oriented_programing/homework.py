class Student():
    age = 13
    height = 170
    name = "george"
    school_name = "oldbury school"
    subjects = "sience"
    grade = 8
    transport = "car"
    form_teacher = "miss clarke"
    
    def __init__(self,age,height,name,school_name,subjects,grade,transport,form_teacher):
        print("constructor function called")
        self.age = age 
        self.height = height
        self.name = name
        self.school_name = school_name
        self.subjects = subjects
        self.grade = grade
        self.transport = transport
        self.form_teacher = form_teacher



george = Student(13,170,"george")
print(george.age)
print(george.height)
print(george.name)



david = Student(12,168,"david")
print(david.age)
print(david.height)
print(david.name)




    