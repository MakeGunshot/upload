class Employee:
    
    pay_amount = 1.2
    num_emps = 0

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = first + last +"@123.com"
        self.pay = pay
        Employee.num_emps += 1
    
    def fullname(self):
        return ('{} {}'.format(self.first,self.last))
    
    def pay_raise(self):
        self.pay =self.pay * self.pay_amount

    @classmethod
    def set_raise_amount(cls,amount):
        cls.pay_amount = amount
    @classmethod
    def from_str(cls,str):
        (first,last,pay) = str.split('-')
        return cls(first,last,pay)
    
    @staticmethod
    def  is_workday(day):
        if day.weekday() == 5 or day.weekday()==6:
            return False
        else:
            return True
# import datetime
# nowday = datetime.datetime(2018,4,14)
# print(Employee.is_workday(nowday))
            

class Devloper(Employee):
    pay_amount = 1.10
    pass

class Manager(Employee):
    
    def __init__(self,first,last,pay,employees = None):
        super().__init__(first,last,pay)
        if employees == None :
            # self.employees == []
        else:
            
            self.employees = employees
    def print_employees(self):
        for emp in self.employees:
            print(emp.fullname(),emp.email)
        # print(self.employees)


dev_1 = Devloper('hello','hesss',3000)
dev_2 = Devloper('hello','hfkjsa',3000)
# print(dev_1.fullname())
# print(dev_1.pay_amount)

manager_01 = Manager('hob','sadd',50000,[dev_1,dev_2])
print(manager_01.fullname(),manager_01.email)
manager_01.print_employees()

# emp_1 = Employee('hello','world',1000)
# emp_2 = Employee('test','world',2000)

# Employee.set_raise_amount(1.5)

# emp1_str = 'jpho-h111-2000'
# emp2_str = 'shhs-lai-3000'

# new_emp1 = Employee.from_str(emp1_str)
# new_emp2 = Employee.from_str(emp2_str)
# print(new_emp1.fullname())
# print(new_emp2.fullname())


# (first,last,pay) = emp1_str.split('-')
# new_emp1 = Employee(first,last,pay)
# print(new_emp1.fullname())



# print(emp_1.pay_amount)
# print(emp_2.pay_amount)
# print(Employee.num_emps)






