name = "Stefan"
print(name)
name = "Stefan is a man"
print(name)

print("works because I create a NEW string, namecap:")
nameCap = name.upper()
print("Did I capitalize: " + nameCap)


print("\n does not work because the upper() returns a new string but we did not captue it in a new variable:")
name.upper()
print("Did I capitalize: " + name)

'''
# Works in the python shell!
>>> name = "stefan"
>>> name.upper()
'STEFAN'
>>> name
'stefan'
>>> clear()
'''
