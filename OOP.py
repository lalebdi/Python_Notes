# classes represent something. you can instansiate classes into objects. So we define a structure in a class and use that class to create objects.
# objects are examples of classes.

class Customer:
    def __init__(self, name, membership_type): #this is the constrcutor or initialiazer. self is the equivlant of "this" in JavaScript.
        self.name = name
        self.membership_type = membership_type

    def update_membership(self, new_membership): #anytime you want to a method to appear on an instatiated object you need to add "self" as an attribute. not using "self" renders the method un-envokeable -> you will be a TypeError stating that "0 positional arguments but 1 was given". 
        self.membership_type = new_membership

    def __str__(self): #this is going to be envoked anytime we try to convert an object into a string. Without this method we would get a memory refernce when we print a customer.
        print("converting into a string")
        return self.name + " " + self.membership_type
    
    def print_all_customers(customers):
        for customer in customers:
            print(customer)

    def __eq__(self, other): # "other" refers to what we are comparing the customers to. if we did not over ride the equals method, we would get comparsions by memory location.
        if self.name == other.name and self.membership_type == other.membership_type:
            return True
        
        return False
        
    __hash__= None # this isn't going to break anything. the only thing of this is not going to be able to use Customers in a hashable datastructures

    __repr__ = __str__ # this is for representation. it will override 


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


Customer.print_all_customers(customers_b)
print(customers_b[0] == customers_b[1])

print(customers_b)

