#while loop
count = 10 #set 1st value
while count <= 15:
    print(count)
    count +=1

#program 2
number = 105
while number >= 100:
    print("number is", number)
    number-=1

#for loop
for num in range(20,60):
    print(num)

languages=["python", "java", "C++", "javascript"]
for lang in languages:
    print(lang)

#functions/methods-block of code that does a specific task
#standard library functions
Y=max(45,78,89,43,2,456,7895,56)
print("the maximum number is", Y)
X=min(45,78,89,43,2,456,7895,56)
print("the minimum number is", X)

#user-defined functions
def name():
    print("Jeff")

name() #calling a function


def add():
    print(10+20)

add()

#parameter/variable
def dog(name,breed,age):
    print(name,breed,age)

dog("Bob", "German Shepherd", "5")
dog("Mary", "Chihuahua", "2")
dog("Peter", "Siberian Husky", "4")

#use a user defined function with the help of parameters and arguements.
#details- fullname, position, gender, age

def workers(fullname,position,gender,age)
    print(fullname,position,gender,age)

workers("Arnold","Secretary","Male","21"
workers("Merell","Receptionist","Female","19"
workers("Markeiff","CEO","Male","300"