# there's a built in module that makes working with JSON easy.
# here we will incode and decode json data



# Below I'm converting a dict into a JSON format (encoding or serialization)
import json

person = {"name" : "Jessica", "age" : 20, "city" : "NYC", "hasChildren" : False, "titles" : ["engineer", "programmer"]}

personJSON = json.dumps(person, indent=4) # will dump our object into a JSON string. avoid using separators. use sote keys to sort them alphabetically
print(personJSON) #note the False in the terminal is in lower case so its in JSON format

#  to convert into a file
with open('person.json', 'w') as file:
    json.dump(person, file, indent= 4)

#  to convert JSON data into a python object (deserialization or decoding)
person = json.loads(personJSON)
print(person) #note the F in False. its in capital now so its in dict mode

# to do the same conversion above but from a file 
with open('person.json', 'r') as file:
    person = json.load(file)
    print(person)

# now lets do the above but with a custom class

    class User:

        def __init__(self, name, age):
            self.name = name
            self.age = age


user = User("Bella" , 9)

# now we will covert the above into a JSON format

# before dumps it we need to write a custom encoding function
def encode_user(o):
    if isinstance(o, User):
        return { 'name' : o.name, 'age' : o.age, o.__class__.__name__ : True}
    else:
        raise TypeError ('Object of type User is not JSON serializable')

# now that the encoding function. it should work
userJSON = json.dumps(user, default=encode_user)
print(userJSON)

# Another way of doing the above is by letting the JSONencoder override the function
from json import JSONEncoder

class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):
            return { 'name' : o.name, 'age' : o.age, o.__class__.__name__ : True}
        return JSONEncoder.default(self, o)


userJSON2 = json.dumps(user, cls=UserEncoder)
print(userJSON2)
# or let the encoder handle the whole thing
userJSON3 = UserEncoder().encode(user)
print(userJSON3)

# Now I'm decoding the object back

user2 = json.loads(userJSON3)
print(user2)
print(type(user2))
# to decode this into a dictionary you have to first to write a custome method
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct

user3 = json.loads(userJSON3, object_hook=decode_user)
print(user3)
print(user3.name)
print(type(user3))