

# class Employee:
#     # 声明一个类的变量
#     pay_raist_amount = 1.2
#     # 创建一个构造器
#     def __init__(self,first,last,pay,domain="funcat.com"):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first+last+"@"+domain

#     # 创建一个方法

#     def fullname(self):
#         return self.first+self.last

#     def new_pay0(self):
#         # return self.pay * Employee.pay_raist_amount
#         return self.pay * self.pay_raist_amount

#     def new_pay1(self):
#         return self.pay * Employee.pay_raist_amount
# # 创建一个类的实例
# emp1 = Employee("xiaoming","wang",10000,"baidu.com")
# emp2 = Employee("xiaohong",'zhang',20000)
# Employee.pay_raist_amount = 1.4
# print(emp1.new_pay0())
# print(emp1.new_pay1())
# print(emp2.new_pay0())
# print(emp2.new_pay1())
# emp1.pay_raist_amount = 1.5
# print("emp1. raise, emp1.newpay0()",emp1.new_pay0())
# print(emp1.new_pay1())
# print(emp2.new_pay0())
# print(emp2.new_pay1())
# emp2.pay_raist_amount = 1.6
# print(emp1.new_pay0())
# print(emp1.new_pay1())
# print(emp2.new_pay0())
# print(emp2.new_pay1())




# 声明一个Employee 类
# class Employee:
#     # 声明一个类的变量
#     pay_raist_amount = 1.2

#     __weight = 40
#     # 创建一个构造器
#     def __init__(self,first,last,pay,weight,domain="funcat.com"):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first+last+"@"+domain
#         self.__weight = weight

#     def __say(self):
#         print("helloworld {}".format(self.__weight))

#     def Isay(self):
#         self.__say()

#     # 创建一个方法
#     def fullname(self):

#         return '{}-{}-{}'.format(self.first,self.last,self.pay)

#     def new_pay0(self):
#         # return self.pay * Employee.pay_raist_amount
#         return self.pay * self.pay_raist_amount



# # 创建一个类的实例
# emp1 = Employee("xiaoming","wang",10000,50,"baidu.com")

# # emp1.__weight = 60
# # emp1.__say()
# emp1.Isay()
# # emp2 = Employee("xiaohong",'zhang',20000)
# # print(emp1.fullname())



# #类定义
# class People:
#     #定义基本属性
#     name = ''
#     age = 0
#     #定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#     #定义构造方法
#     def __init__(self,n,a,w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#     def speak(self):
#         print("%s 说: 我 %d 岁。" %(self.name,self.age))

# class Student(People):

#     def __init__(self,n,a,w,grade):
#         # People.__init__(self,n,a,w)
#         super().__init__(n,a,w)
#         self.grade = grade

#     # 方法重写
#     def speak(self):
#         print("%s 说: 我 %d 岁, %d 年级" %(self.name,self.age,self.grade))



# s = Student('xiaoming',20,50,5)
# s.speak


# class people:
#     #定义基本属性
#     name = ''
#     age = 0
#     #定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#     #定义构造方法
#     def __init__(self,n,a,w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#     def speak(self):
#         print("%s 说: 我 %d 岁。" %(self.name,self.age))

#     def __say(self):
#         print("++++++")

# #单继承示例
# class student(people):
#     grade = ''
#     def __init__(self,n,a,w,g):
#         #调用父类的构函
#         people.__init__(self,n,a,w)
#         self.grade = g
#     #覆写父类的方法
#     def speak(self):
#         print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))

    #调用私用方法— __say()

    # 调用私有变量  __weight

class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))

    def __say(self):
        print("{}说：我{}千克".format(self.name,self.__weight))

#单继承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构函
        people.__init__(self,n,a,w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))

class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))

class sample(student,speaker):
    a =''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)

e = sample("xiaoming",10,100,5,"Python")
e.speak()














