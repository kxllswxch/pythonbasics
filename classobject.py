#claass is a blueprint of an object.
#object is an instance of a class

class Student:
    name="Joy"
    age=23
    gender="female"
    course="MIT"

#behaviour/functions
    def study(self):
        print("student is studying")

student1=Student()#creating an object
student1.study()
print(student1.name)