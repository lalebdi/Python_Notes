my_list= ["banana", "cherry", "apple"]

print(my_list)

my_list2 = list() # creates an empty list to append items
print(my_list2)

# to iterate over a list use a for in loop
for i in my_list:
    print(i)

# to check if an item is in a list use if
if "banana" in my_list:
    print("yes")
else:
    print("no")

# to check the length of a list
print(len(my_list))

# to add an item to a list use append
my_list.append("lemon")
print(my_list)

# to insert an item in specific index use insert
my_list.insert(1,"blueberry")
print(my_list)

# to remove item use pop and returns it
item = my_list.pop()
print(item)
print(my_list)

# to remove a specific element use remove it does not retun the item
item2 = my_list.remove("blueberry")
print(item2)
print(my_list)

# copying a list. if the new "copy" list is modified the original list will be modified too!! because they are referred to in the same memory
my_list_copy = my_list
print(my_list_copy)

# to make an actual "separate" copy of a list use the copy method
my_list_copy2 = my_list.copy()
# or
my_list_copy3 = list(my_list)
# or
my_list_copy4 = my_list[:]

# if you want to create a sorted new list place the list in a variable and pass in the list in the sort mehtod
new_list = sorted(my_list)
print(new_list)

# a list can be sorted using sort. it changes your original list
my_list.sort()
print(my_list)


# a list can be reversed using reverse
my_list.reverse()
print(my_list)

# to remove all elemnets in a list use clear
my_list.clear()
print(my_list)

# to create a new list with multiple similar elements, such as [0,0,0,0,0]
my_list3 = [0] * 5
print(my_list3)

# to concat 2 list use the + 
my_list4 = [3] * 5
concat_list = my_list4 + my_list3
print(concat_list)

# slicing
my_list5 = [1,2,3,4,5,6,7,8,9]

a = my_list5[1:5] # start at index 1 and end at 5 non inclusive to the end. if the start or the end are not specified it will go all the way
b = my_list5[::2] # start at index 0 with a step two for evey second item. can use a negative index to start reverse
print(a)
print(b)

#  list comprehension [ expression with a for in loop]
list_original = [ 1, 2, 3, 4, 5, 6, 7 ]
# going to create a new list with the square numbers of the above
list_square = [i*i for i in list_original]
print(list_square)