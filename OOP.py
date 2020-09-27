# classes represent something. you can instansiate classes into objects. So we define a structure in a class and use that class to create objects.
# objects are examples of classes.

class Customer:
    def __init__(self, name, membership_type): #this is the constrcutor or initialiazer. self is the equivlant of "this" in JavaScript.
        self.name = name
        self.membership_type = membership_type

    def update_membership(self, new_membership): #anytime you want to a method to appear on an instatiated object you need to add "self" as an attribute. not using "self" renders the method un-envokeable -> you will be a TypeError stating that "0 positional arguments but 1 was given". 
        self.membership_type = new_membership

    def __str__(self): #this is going to be envoked anytime we try to convert an object into a string
        print("converting into a string")
        return self.name + " " + self.membership_type

# stattic methods (the methods inside a class that don't have "self" as a parameter): they are methods that are not attached to any object created but instead are envoked on the class itself. 


customer1 = Customer('Bella', 'Gold')
print(customer1.name, customer1.membership_type)

customer2 = Customer('Snowball', 'Silver')
print(customer2.name, customer2.membership_type)


customers_a = [customer1, customer2]

# or 
customers_b = [Customer('Maruysa', 'Gold'), Customer('Zeno', 'Bronz')]
print(customers_b[0].name)
customers_b[1].verified = False # you can always add attributed anywhere after the constructor. It is best practice to add it in the constructor
print(customers_b[1].verified)

print(customers_b[1].membership_type) #this is the old membership type
customers_b[1].membership_type = 'Silver'
print(customers_b[1].membership_type) # this is the updated membership type that we updated using the update_membership method in the class

# before envoking the __str__ method:
print(customers_b[0])
# after envoking the __str__method:
print(customers_b[0])

# continue here tomorrow