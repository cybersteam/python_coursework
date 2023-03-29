#Tuples are immutable
#lists are mutable, ad delete

a =5
b = "Foo"

persons = ["Brian", "Bob", "Alice", "Jean"]
print(persons[1:2])

for i in range(0, len(persons)):
    print(persons[i])
   


print(persons[-1]) #gives the last element
new = "boobs"
persons.append(new)
print(persons)
print(new[2])

 

def things(name, size, direction):
    print(f"Name = {name}, Size = {size}, Direction: {direction}")

infos = things()
print(infos)
things(*infos)
