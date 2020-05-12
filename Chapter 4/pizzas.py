favorite_pizzas = ['pepperoni', 'opera special', 'dillinger', 'la caletta', 'siena', 'americana', 'milano', 'parco', 'speciale']
for pizza in favorite_pizzas:
    print(f"I like {pizza.lower()} pizza.\n")
print("I really love pizza.\n\n")

print("The first three items in the list are:")
for item in favorite_pizzas[:3]:
    print(item.lower())

print("Three items from the middle of the list are:")
for item in favorite_pizzas[6:]:
    print(item.lower())

print("The last three items in the list are:")
for item in favorite_pizzas[-3:]:
    print(item.lower())
