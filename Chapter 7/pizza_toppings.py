prompt = "\nPlease enter a series of pizza toppings:"
prompt += "\n(Enter 'quit' when you are finished) "

while True:
    pizza_topping = input(prompt)


    if pizza_topping == 'quit':
        break
    else:
        print(f"I will add that {pizza_topping.lower()} to your pizza.")
    
