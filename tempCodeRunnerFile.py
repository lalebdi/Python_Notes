def __str__(self): #this is going to be envoked anytime we try to convert an object into a string
        print("converting into a string")
        return self.name + " " + self.membership_type