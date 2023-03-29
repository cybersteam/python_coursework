class Pizza:
    def __init__(self, name, price, ingredients, isveg=False):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.isveg = isveg

    def display(self):
        VEG = ""
        if self.isveg:
            VEG = "- VEGETARIAN"
        print(f"PIZZA {self.name} : €{self.price} : " + VEG)
        print(" - ".join(self.ingredients))
        print()

class CustomPizza(Pizza):
    BASE_PRICE = 10
    PRICE_PER_INGREDIENT = 1.2
    last_number = 0

    def __init__(self):
        CustomPizza.last_number += 1
        self.number = CustomPizza.last_number
        super().__init__("Custom " + str(self.number), 0, [])
        self.ask_user_for_ingredient()                      #calls the method below
        self.compute_price()                                #calls the method below
        

    def ask_user_for_ingredient(self):
        print()
        print(f"Enter your ingredients for pizza number {self.number}")
        while True:
            ingredient = input(f"Add your ingredient(or press ENTER to finish)")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print(f"You have {len(self.ingredients)} ingredient(s) : {', '.join(self.ingredients)}")

    def compute_price(self):
        self.price = self.BASE_PRICE + len(self.ingredients) * self.PRICE_PER_INGREDIENT
    

pizzas = (
    Pizza( "Hawain", 30.99, ("ham", "pineapple")),
    Pizza( "Vegetarian", 25.50, ("mushroom", "tomato", "spinach"), True),
    Pizza( "Mexican", 40.60, ("mince", "mushroom", "chilli")),
    Pizza( "Happy", 30.20, ("onion", "peppers", "olives"), True),
    CustomPizza(),
    CustomPizza()
)

def pizza_sort(e):
    return len(e.ingredients)

#pizzas.sort(key=pizza_sort)

for i in pizzas:
    i.display()
    #if i.isveg:
        #i.display()
    #if not i.isveg:
        #i.display()
    #if "tomato" in i.ingredients:
        #i.display()
    #if i.price < 30:
        #i.display()




