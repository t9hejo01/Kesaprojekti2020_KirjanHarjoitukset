pets = {
    'dog': {
        'pet': 'husky',
        'owner': 'johan'
        },

    'parrot': {
        'pet': 'grey parrot',
        'owner': 'john'
        },

    'cat':{
        'pet': 'american curl',
        'owner': 'hayley'},
    }

for pet, pet_info in pets.items():
    print(f"\nPet: {pet}")
    pet_info = f"{pet_info['pet']} {pet_info['owner']}"


    print(f"\t Full info: {pet_info.title()}") 

    


   


