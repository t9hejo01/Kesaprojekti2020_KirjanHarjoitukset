
prompt = "\nPlease enter a series of pizza toppings:"
prompt += "\n(Enter 'quit' when you are finished) "

while True:
    pizza_topping = input(prompt)


    if pizza_topping == 'quit':
        break
    else:
        print(f"I will add that {pizza_topping.lower()} to your pizza.")




pizza_topping = ""
while pizza_topping != 'quit':
    pizza_topping = input(prompt)

    if pizza_topping != 'quit':
        print(pizza_topping)



active = True
while active:
    pizza_topping = input(prompt)

    if pizza_topping == 'quit':
        active = False
    else:
        print(pizza_topping)
 
