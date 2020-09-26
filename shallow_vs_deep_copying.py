# the assignment operator:
org = 10
copy_org = org # this is not a real copy. This will make a new variable with the same refrence (both variables point to the same number) 
print(copy_org)
# if the vaiable is re-assigned, it will create a new refernce. This is for immutable data types
copy_org = 20
print(copy_org)

# In cases of mutable data types. e.g. lists
org_list = [11, 12, 14, 15, 16]
copy_list = org_list
print(copy_list)
copy_list[2] = 13
print(copy_list) 
print(org_list) # notice here that the original changed as well. This is because they have the same refernce.

# to make an actual copy of a mutable data type. use the copy module
import copy

# the copy module can do a shallow and a deep copy.
# shallow copy: one level deep, only refernces of nested child objects. 
# deep copy: full indepenent copy. 

# shallow copy
num_list = [5, 6, 7, 8]
num_copy = copy.copy(num_list)
num_copy[0] = 4
print(num_copy)
print(num_list) # notice here the original was unchanged.
#  other ways to make copies of lists:
num_copy2 = num_list.copy()
print(num_copy2)
# or use the list method to make a shallow copy
num_copy3 = list(num_list)
print(num_copy3)
# or use the list slicer ":"
num_copy4 = num_list[:]
print(num_copy4)

# for nested lists :
bacon = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9]]
bacon_copy = copy.copy(bacon)
bacon_copy[0][1] = 10
print(bacon_copy)
print(bacon) # both the copy and the original have changed -> this is becuse we used a shallow copy. to avoid this use the deep copy method.
bacon_copy2 = copy.deepcopy(bacon)
bacon_copy2[0][2] = 19
print(bacon_copy2)
print(bacon)

# we can use the deep copy for dict, tuples and custom objects 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Bella', 11)
# making a copy of person 1 
p2 = p1
print(p2.age)
p2.age = 9
print(p2.age)
print(p1.age) # notice here the age changed to 9 because this is not an actual copy.

p3 = copy.copy(p1)
p3.age = 5
print(p3.age)
print(p1.age) # since we use the copy method the original (p1) was di not change.

class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee


boss1 = Person('Vica', 50)
boss2 = Person('Ella', 33)

company = Company(boss1, boss2)

# making a clone of this
company_clone = copy.copy(company)
company_clone.boss.age = 46
print(company_clone.boss.age)
print(company.boss.age) # both changed here -> this is only a shallow copy and the age is on level 2
# to make them independent of each other make a deep copy of them

# making a deep clone of this
company_clone2 = copy.deepcopy(company)
company_clone2.boss.age = 55
print(company_clone2.boss.age)
print(company.boss.age) 
