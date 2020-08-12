from random import randint

class Dice():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        return randint(1, self.sides)

d6 = Dice()

results = []
for roll_num in range(10):
    result = d6.roll_dice()
    results.append(result)
print("10 rolls of a 6-sided dice:")
print(results)


d10 = Dice(sides=10)

results = []
for roll_num in range(10):
    result = d10.roll_dice()
    results.append(result)
print("\n10 rolls of a 10-sided dice:")
print(results)


d20 = Dice(sides=20)

results = []
for roll_num in range(10):
    result = d20.roll_dice()
    results.append(result)
print("\n10 rolls of a 20-sided dice:")
print(results)
