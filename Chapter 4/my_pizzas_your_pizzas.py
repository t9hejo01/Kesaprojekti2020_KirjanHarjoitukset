my_pizzas = ['pepperoni', 'opera special', 'dillinger', 'la caletta', 'siena', 'americana', 'milano', 'parco', 'speciale']
friend_pizzas = my_pizzas[:]

my_pizzas.append('vesuvio')
friend_pizzas.append('cacciatora')

print("My favorite pizzas are:")
for my_pizza in my_pizzas:
    print(my_pizza)

print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
