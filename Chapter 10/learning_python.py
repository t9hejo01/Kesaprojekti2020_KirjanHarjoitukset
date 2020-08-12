filename = 'learning_python.txt'


with open(filename) as fhand:
    contents = fhand.read()

print(contents)


print("--------------------------------------")


with open(filename) as fhand:
    for line in fhand:
        print(line.rstrip())



print("--------------------------------------")


with open(filename) as fhand:
    lines = fhand.readlines()

for line in lines:
    print(line.rstrip())
