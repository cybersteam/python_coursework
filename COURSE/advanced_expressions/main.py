# # for loops inline
# # any
# # any sub
# # zip functions

# class Pizza:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price


# pizzas = [
#     Pizza("hawain", 10.50),
#     Pizza("4 cheese", 10.50),
#     Pizza("ham", 7.50)
# ]

# #####################################
# # pizza_names = []
# # for pizza in pizzas:
# #     pizza_names.append(pizza.name)
# #pizza_names = [i.name for i in pizzas]
# pizza_names = [i.name for i in pizzas if len(i.name) < 6]

# #(the same as the above code)
# #####################################

# print(pizza_names)

# # any : will return True if any item is True
# #print(any([False, False, True]))

# expensive_pizza_exists = any([i.price > 11 for i in pizzas])
# print(expensive_pizza_exists)

# #sum
# #print(sum([5,6,9]))
# # the "1" here is the output if the condition on the right is met in each of the i's in the list 
# # - if more than one it will add 1 + 1 etc..
# expensive_pizza_nm = sum([1 for i in pizzas if i.price  > 10])
# print(expensive_pizza_nm)

###ZIP function
pizza_names = ("hawain", "4cheese", "regina")
pizza_prices = ("10.50", "8.50", "9.50")

names_and_prices = list(zip(pizza_names, pizza_prices))
unzipper = list(zip(*names_and_prices))

print(names_and_prices)
print(unzipper)