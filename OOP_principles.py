# OOP pillers are:
# Encapsulation. -> you can hide the inner details of a class or certain data and share what is needed. So, instead of people accessing some data directly, they access it through setters and getters. In Python, this is done using "Property". 
# Inheritence. -> allows us to have certain attributes for objects because they defined in a base class. 
# polymorphisim -> we can treat objects as the same thing. 


class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

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


customers = [Customer('Bella', 'Gold') , Customer('Snowball', 'Silver'), Customer('Maruysa', "Bronze")]

print(customers)

