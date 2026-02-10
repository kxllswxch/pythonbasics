class employee:

    def __init__(self,fullname,position,status,age):
        self.fullname=fullname
        self.position=position
        self.status=status
        self.age=age

    def work(self):
        print(self.fullname,"is working")

employee1 = employee("Kenneth", "MD", "Married", 47)
employee2 = employee("Kennedy", "HR", "Married", 44)
employee3 = employee("Kenny", "Intern", "Single", 212)

print(employee1.fullname, employee1.position, employee1.status, employee1.age,"is working")
print(employee2.fullname, employee2.position, employee2.status, employee2.age,"is working")
print(employee3.fullname, employee3.position, employee3.status, employee3.age,"is working")
