#print("Hello World.Its Run")

# region Exercise 1

# x = 1
# if x == 1:
#     print("x is 1")

# endregion

# region Exercise 2

# myint=8
# print(myint)

# endregion

# region Exercise 3

# myfloat=0.7
# print(myfloat)
# myfloat=float(7)
# print(myfloat)

# endregion

# region Exercise 4

# mystring='hello'
# print(mystring)
# mystring="Hello World"
# print(mystring)


# endregion

# region Exercise 5

# mystring="don't worry "
# print(mystring)

# endregion

# region Exercise 6

# firstNumber = 5
# secondNumber = 6
# SumOfNumbers = firstNumber+secondNumber
# print(SumOfNumbers)

# hello = "Hello"
# world = "World"
# helloWorld = hello + ' '+world
# print(helloWorld)


# endregion

# region Exercise 7

# a, b = 3, 4
# print(a, b)

# endregion

# region Exercise 8

# mystring = "hello"
# myfloat = float(10.0)
# myint = 5

# if(mystring == "hello"):
#     print("String: %s" % mystring)
# if isinstance(myfloat, float) and myfloat == 10.0:
#     print("Float: %f" % myfloat)
# if isinstance(myint,int) and myint==5:
#     print("Integer: %d" % myint)


# endregion

# region Exercise 9

# mylist = []
# mylist.append(1)
# mylist.append(2)
# mylist.append(3)
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])

# for x in mylist:
#     print(x, end=" ")

# endregion


# region Exercise 10

# numbers = [1, 2, 3]
# names=["hello","world"]

# print(numbers)
# print(names)

# endregion


# region Exercise 11

# number = 1+2*3/4.0
# print(number)

# endregion


# region Exercise 12

# reminder = 11 % 3
# print(reminder)

# squared = 7**2
# cubed = 2**3
# print(squared)
# print(cubed)

# lotsofHello = " hello"*10
# print(lotsofHello)

# even_numbers = [2, 4, 6, 8]
# odd_numbers = [1, 3, 5, 7]
# all_numbers = odd_numbers+even_numbers
# print(all_numbers)
# print('{} - {}'.format(even_numbers, odd_numbers))

# number = int(input("Enter an integer: "))
# if number < 100:
#     print("Your number is smaller than 100")
# else:
#     print("Your number is greater than 100")

# endregion


# region Exercise 13

# class Student(object):

#     def __init__(self, name, branch, year):
#         self.name = name
#         self.branch = branch
#         self.year = year
#         print("A Student object is created")

#     def print_details(self):

#         print("Name:", self.name)
#         print("Branch:", self.branch)
#         print("Year:", self.year)

# student = Student()
# dir(student)

class Person(object):
    """
    Returns a ```Person``` object with given name.

    """
    def __init__(self, name):
        self.name = name

    def get_details(self):
        "Returns a string containing name of the person"
        return self.name


class Student(Person):
    """
    Returns a ```Student``` object, takes 3 arguments, name, branch, year.

    """
    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year

    def get_details(self):
        "Returns a string containing student's details."
        return "%s studies %s and is in %s year." % (self.name, self.branch, self.year)


class Teacher(Person):
    """
    Returns a ```Teacher``` object, takes a list of strings (list of papers) as
    argument.
    """
    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers

    def get_details(self):
        return "%s teaches %s" % (self.name, ','.join(self.papers))


person1 = Person('Sachin')
student1 = Student('Kushal', 'CSE', 2005)
teacher1 = Teacher('Prashad', ['C', 'C++'])

print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())

# endregion
