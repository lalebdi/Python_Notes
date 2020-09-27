# OOP pillers are:
# Encapsulation. -> you can hide the inner details of a class or certain data and share what is needed. So, instead of people accessing some data directly, they access it through setters and getters. In Python, this is done using "Property". 
# Inheritence. -> allows us to have certain attributes for objects because they defined in a base class. 
# polymorphisim -> we can treat objects as the same thing. 

# Property: is a normal attribute but it is not a variable. It has an extra layer that abstract away the variable itself using methods. So, allows us to add functionality. 

class User:
    def log(self):
        print(self)

class Teachers(User): #this is an example of polymorphism
    def log(self):
        print("I am the Teacher")

class Customer(User): #the Customer class is inhereting from the User class. 
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

    def log(self):
        print("I am the Customer")

    # I'm going to make "name" a property. I'm gonna need 2 methods.

    @property
    def name(self):
        print("Getting name")
        return self._name # when you see something prefixed with an "_". it means that this is private so don't touch it if you are outside of the class. 

    @name.setter
    def name(self, name):
        print("Setting name")
        self._name = name

    @name.deleter
    def name(self): # this is to delete names
        del self._name

    def update_membership(self, new_membership):
        print('Calcualting Costs')
        self.membership_type = new_membership

    def __str__(self):
        return self.name + " " + self.membership_type

    def print_all_customers(customers):
        for customer in customers:
            print(customer)

    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return True

        return False

    __hash__ = None

    __repr__ = __str__


customers = [Customer('Bella', 'Gold') , Customer('Snowball', 'Silver'), Customer('Maruysa', "Bronze"), Teachers()]
users = [Customer('Bella', 'Gold') , Customer('Snowball', 'Silver'), Customer('Maruysa', "Bronze"), Teachers()]

print(customers)

customers[0].log()
customers[3].log()

# below is to use the log method to all the people
for user in users:
    user.log() #the log method is envoked on everyone
