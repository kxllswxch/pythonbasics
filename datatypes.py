age = 17 #integer
weight = 55.7 #float
greeting = "hi" #string
isMammal = True #boolean

#data structures: multiple elements in one variable
fruits = ["banana", "mango", "cherry"] #list-ordered and changeable
courses = ["MIT", "Data science", "Cybersecurity"] #array-similar data types
cars = ("ford", "g-wagon", "mazda", "mitsubishi") #tuple-ordered and unchangeable
countries = {"Tanzania", "India", "Italy"} #set-unordered and unchangeable
student = {
    "firstname" : "Jeff",
    "course" : "MIT",
    "age" : 17,
    "nationality" : "Kenyan/Togolese"
} #dictionary - key value pair


print("student is", age, "years old")
print(weight)
print("is animal a mammal?",isMammal)
print(countries)


#typecasting-converting one data type to another
print(float(age))
print(int(weight))