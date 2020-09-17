# dictionary is a data collection type that is unordered, mutable nad key-value pairs. its like an object in JS.

my_dic = {"name" : "Leah" , "age" : 21, "city" : "New York"}

print(my_dic)

# or

my_dic2= dict(name = "Jane", age = 23, city = "Boston") # no need for quotes for your keys here

print(my_dic2)

# to access the vlaues use the key in a []

val = my_dic["name"]
print(val)

#  to add a key value pairs

my_dic["email"] = "example@gmail.com"
print(my_dic)

# if the key value pair is duplicated it will be overwritten

my_dic["email"] = "nice_example@gmail.com"
print(my_dic)

# to delete items
# 1- use del statement

del my_dic["age"]
print(my_dic)

# 2- use the pop method
my_dic.pop("city")
print(my_dic)

# 3- use the popitem() method -> wich will remove the last item
my_dic.popitem()
print(my_dic)

# to check if a key is present in a dic you can use the if in statment

if "name" in my_dic:
    print(my_dic["name"])

#  or use the try except statement

try:
    print(my_dic["last_name"])
except:
    print("not there")

#  to loop in a dictionary

# for keys
for key in my_dic2.keys():
    print(key)

# for values
for value in my_dic2.values():
    print(value)

# for both 
for key, value in my_dic2.items():
    print(key, value)

#  to copy a dictionary

my_dic_copy = my_dic2 # copying this way will pair them -> when you chnage any one of them they will both change
print(my_dic_copy)

# to make an actual copy -> they are separate
my_dic2_copy = my_dic2.copy()
print(my_dic2_copy)

#  or use the dict and as anrgument use the dict you want to copy

another_dict_copy = dict(my_dic2_copy)
print(another_dict_copy)

# to merge 2 dicts you can use the update method. if the key is duplicated it will be overwriteen. if the key is not present, it will be added.

first_dict = {"name" : "Bella", "age" : 9, "email" : "awesome@dog.com"}
second_dict = dict(name = "Snowball", age = 7, city= "New York")

first_dict.update(second_dict)
print(first_dict)

# key types: can use any immutable type, like numbers or tuples. you can't use a list though because it is mutable and hashable

number_dict = { 3: 9, 6:36, 9:81}
print(number_dict)

my_tuple = (8 , 7)
tuple_dict =  {my_tuple : 15}
print(tuple_dict)