# ----PART 1
# person = {"name": "ivan", "age": "44", "height": "88"}
# print(person["name"])
# person["name"] = "brian"
# print(person["name"])
# person["job"] = "developer"
# print(person)
# purchases = ("eggs", "cheese", "ham")
# person["purchases"] = purchases
# print(person)
# for i in person:
#     print(i + "-" + str(person[i]))
#     print(f"Key: {i} Value {person[i]}")

#-----PART 2
# USING A LIST YOU HAVE TO ITERATE THROUGH WHICH IS EXPENSIVE PROCESSSING. DICTIONARIES HAVE DIRECT ACCESS...
persons = [
    ("Ivan", 44, 1.8),
    ("Candy", 44, 1.5),
    ("Simon", 44, 1.12),
    ("Ant", 44, 1.8)
]

def get_infos(name, l):
    for i in l:
        if i[0] == name:
            return i
    return None

infos = get_infos("Simon", persons)
print(infos)
print()

persons_dict = {
    "Ivan": (44, 1.8),
    "Candy": (50, 1.5),
    "Simon": (40, 1.12),
    "Ant": (52, 1.8)
}

# Using "get" here is simpler than a try/except block.
infos = persons_dict.get("Jack")
if infos == None:                                           #same as "if not infos:"
    print("The key you have requested was not found.")
else:
    print(infos)
