class HashTable:
    def __init__(self) -> None:
        self.collection = {}
    
    def hash(self, string: str) -> int:
        total = 0
        for character in string:
            number = ord(character)
            total += number
        return total

    def add(self, key, value):
        key_hashed = self.hash(key)

        if not key_hashed in self.collection:
            self.collection[key_hashed] = {}

        self.collection[key_hashed][key] = value
            
    def remove(self, key):
        key_hashed = self.hash(key)
        if key_hashed in self.collection:
            if key in self.collection[key_hashed]:
                del self.collection[key_hashed][key]
        else:
            print("It doesn't exist")

    def lookup(self, key):
        key_hashed = self.hash(key)
        if key_hashed in self.collection:
            if key in self.collection[key_hashed]:
                return self.collection[key_hashed][key]
        return None


# ----- My Experiment -----
# My thought on how to solve the problem, step by step

collection = {}

string = 'cfc'
value = "This belongs to cfc"
total = 0
for character in string:
    number = ord(character)
    total += number
print(total)

final_key = total

collection[final_key] = value

print(collection)

# Case where the string is also 'fcc' and the total = 300

string = 'fcc'
value = "This belongs to fcc"
total = 0
for character in string:
    number = ord(character)
    total += number
print(total)

final_key = total

collection[final_key] = value
print(collection)

collection.clear()
print(collection)
# It would be overwritten here

print('\n')
string1 = 'fcc'
string2 = 'cfc'

value1 = 'this belongs to fcc'
value2 = 'this belongs to cfc'

total1 = 0
for character in string1:
    number = ord(character)
    total1 += number

final_key1 = total1

total2 = 0
for character in string2:
    number = ord(character)
    total2 += number

final_key2 = total2

collection[final_key] ={}
print(collection)

collection[final_key1][string1] = value1
collection[final_key2][string2] = value2
print(collection)


string3 = 'new'
value3 = "book"

total3 = 0
for character in string3:
    number = ord(character)
    total3 += number

final_key3 = total3

if final_key3 in collection:
    print("True")
else:
    collection[final_key3] = {}
    collection[final_key3][string3] = value3

print(collection)

