dinner_guests = ['taneli', 'juhana', 'hannu', 'mauno-ville', 'marja', 'visa']
print(dinner_guests)

message1 = f"{dinner_guests[0].title()}, kutsun sinut paivalliselle."
print(message1)

message2 = f"{dinner_guests[1].title()}, kutsun sinut paivalliselle."
print(message2)

message3 = f"{dinner_guests[2].title()}, kutsun sinut paivalliselle."
print(message3)

message4 = f"{dinner_guests[3].title()}, kutsun sinut paivalliselle."
print(message4)

message5 = f"{dinner_guests[4].title()}, kutsun sinut paivalliselle."
print(message5)

message6 = f"{dinner_guests[5].title()}, kutsun sinut paivalliselle."
print(message6)




print("Loysin isomman poydan.")

dinner_guests.insert(6, 'pekka')
dinner_guests.insert(7, 'hannes')
dinner_guests.append('aaron')
print(dinner_guests)

message1 = f"{dinner_guests[0].title()}, kutsun sinut paivalliselle."
print(message1)

message2 = f"{dinner_guests[1].title()}, kutsun sinut paivalliselle."
print(message2)

message3 = f"{dinner_guests[2].title()}, kutsun sinut paivalliselle."
print(message3)

message4 = f"{dinner_guests[3].title()}, kutsun sinut paivalliselle."
print(message4)

message5 = f"{dinner_guests[4].title()}, kutsun sinut paivalliselle."
print(message5)

message6 = f"{dinner_guests[5].title()}, kutsun sinut paivalliselle."
print(message6)

message7 = f"{dinner_guests[6].title()}, kutsun sinut paivalliselle."
print(message7)

message8 = f"{dinner_guests[7].title()}, kutsun sinut paivalliselle."
print(message8)

message9 = f"{dinner_guests[8].title()}, kutsun sinut paivalliselle."
print(message9)





print("Isompi poyta ei ehdi saapua ajoissa, tilaa on vain kahdelle")

message1 = f"Olen pahoillani {dinner_guests[0].title()}, en voi kutsua sinua paivalliselle."
dinner_guests.pop(0)
print(message1)
print(dinner_guests)

message2 = f"Olen pahoillani {dinner_guests[0].title()}, en voi kutsua sinua paivalliselle."
dinner_guests.pop(0)
print(message2)
print(dinner_guests)

message3 = f"Olen pahoillani {dinner_guests[1].title()}, en voi kutsua sinua paivalliselle."
dinner_guests.pop(1)
print(message2)
print(dinner_guests)

message4 = f"Olen pahoillani {dinner_guests[1].title()}, en voi kutsua sinua paivalliselle."
dinner_guests.pop(1)
print(message4)
print(dinner_guests)

message5 = f"Olen pahoillani {dinner_guests[2].title()}, en voi kutsua sinua paivalliselle."
dinner_guests.pop(2)
print(message5)
print(dinner_guests)

message6 = f"Olen pahoillani {dinner_guests[2].title()}, en voi kutsua sinua paivalliselle."
dinner_guests.pop(2)
print(message6)
print(dinner_guests)

message7 = f"Olen pahoillani {dinner_guests[0].title()}, en voi kutsua sinua paivalliselle."
dinner_guests.pop(0)
print(message7)
print(dinner_guests)

del dinner_guests[0]
print(dinner_guests)

del dinner_guests[0]
print(dinner_guests)


