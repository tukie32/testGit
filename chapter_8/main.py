# cars = ["audi", "ferrari", "ford focus", "toyota sienna hybrid"]
# groceries = ["grapes", "oragnes", "bannans"]


# def car_adder(thing_to_add, target_list):
#     if thing_to_add[0].lower() in 'abcdefg':
#         print("This car starts with A-G")
#         target_list.append(thing_to_add)
#     else:
#         print("This car starts with H-Z and we are not allowing it in our club")
#     for item in target_list:
#         if len(item) <= 5:
#             target_list.remove(item)
#             print(f"{item} was not added because it has too few characters")

# car_adder("bmw", cars)
# car_adder("honda", cars)
# car_adder("cinnamon", groceries)
# car_adder("zapples", groceries)

# print(cars)
# print(groceries)

def addTwo(num):
    return num + 2

def addThree(num):
    return num + 3

print(addThree(addTwo(5)))

def namePrinter(first, last, middle= ''):
    return f"The name's {last}, {first} {middle} {last}"

# print(namePrinter("James", "Bond", "Freddie"))

def giveMeMyGroceries(thing_to_add):
    grocery_list = ["grapes", "oragnes", "bannans"]
    grocery_list.append(thing_to_add)
    return grocery_list
print(giveMeMyGroceries("spaghetti").append("tomato sauce"))