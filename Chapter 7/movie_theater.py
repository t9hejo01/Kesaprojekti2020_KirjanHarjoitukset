prompt = "\nPlease enter your age:"
prompt += "\n(Enter 'quit' when finished) "

while True:
    age = int(input("How old are you?"))
   
 
    if age <= 3:
        print("The ticket is free.")

    elif age == 3 or age <= 12:
        print("The ticket is $10.")

    age = input(prompt)
    if age == 'quit':
        break
    

    else:
        print("The ticket is $15.")







    
        
