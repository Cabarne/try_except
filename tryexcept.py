def getData(index):
    data = [10,20,30,40,50]
    return data[index]

# Situation A
try:
    index = int(input("Enter an index: "))
    print(getData(index))
except ValueError:
    print("Index cannot be something else than an integer")


# Situation B
try:
    index = 1000
    print(getData(index))
except IndexError:
    print("An index value cannot be outside the list")




