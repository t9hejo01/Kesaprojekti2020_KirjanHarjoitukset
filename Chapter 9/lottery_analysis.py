from random import choice

pool = ['0', '1', '2', '3', '4','5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E']

active = True
count = 0

while active:
    my_ticket = ""
    for _ in range(4):
        my_ticket += choice(pool)

    lotto = ""
    for _ in range(4):
        lotto += choice(pool)

    if my_ticket == lotto:
        active = False

    count += 1

print(f"After {count} rounds, you win the prize!")
