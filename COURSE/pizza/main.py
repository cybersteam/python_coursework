def custom_sort(e):
    return len(e)

#create a display function with that takes the object "collection"
def display(collection, n_first_element = -1):
    c = collection
    
    if not n_first_element == -1:
        c = collection[:n_first_element]

    c.sort(key=custom_sort)  #can add both - reverse=True, key=custum_sort
    nb_pizzas = len(c)
    print(f"We have ({nb_pizzas}) pizza's")
    if nb_pizzas == 0:
        print("Error, there is no pizza in the oven")
        return

    for i in c:
        print(i)
    print()
    print(f"First pizza: {c[0]}")
    print(f"Last pizza: {c[-1]}")

#create a add user pizza function that appends to the collection object
def add_user_pizza(collection):
    user_pizza = input("Add your pizza: ")
    if user_pizza.lower() in collection:
        print("Error this pizza already exists.")
    else:
        collection.append(user_pizza)

# "e" is a new element we are checking to see if it is inside the collection
def pizza_exists(e, collection):
    for i in collection:
        if e == i:
            return True
    return False
          


pizza = ["4 cheeses", "hawain", "oregano"]
#empty = ()

#first let's us add our pizza to the collection
add_user_pizza(pizza)

#inserts the pizza list into the collection object and displays it
display(pizza, 2)




