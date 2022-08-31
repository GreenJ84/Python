num1 = 42    #Variable Declaration/ Type: Number(INT)
num2 = 2.3    #Variable Declaration/ Type: Number(Float)
boolean = True    #Variable Declaration/ Type: Boolean
string = 'Hello World'    #Variable Declaration/Type: String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']    #Variable Declaration/Type: List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}    #Variable Declaration/Type: Dictionary
fruit = ('blueberry', 'strawberry', 'banana')    #Variable Declaration/Type: Tuple
print(type(fruit))    #Log(Print) Statement
print(pizza_toppings[1])    #Log(Print) Statement
pizza_toppings.append('Mushrooms')    #List/ AddValue
print(person['name'])    #Log(Print) Statement
person['name'] = 'George'    #Dictionary/ Change Value
person['eye_color'] = 'blue'    #Dictionary/ Change Value
print(fruit[2])    #Log(Print) Statement

if num1 > 45:    #Start: IfElse Statement
    print("It's greater")    #Log(Print) Statement
else:    #End: IfElseStatement
    print("It's lower")    #Log(Print) Statement

if len(string) < 5:    #Start: IfELse Statement/ Length Check
    print("It's a short word!")    #Log(Print) Statement
elif len(string) > 15:    #2nd Condition: IfElse Statement/ Length Check
    print("It's a long word!")    #Log(Print) Statement
else:    #End: IfElse Statement
    print("Just right!")    #Log(Print) Statement

for x in range(5):    #For Loop/ Range up to 5
    print(x)    #Log(Print) Statement
for x in range(2,5):    #For Loop./ Range 2-5
    print(x)    #Log(Print) Statement
for x in range(2,10,3):    #For Loop/ Range 2-10/ Increment 3
    print(x)    #Log(Print)-Statement
x = 0    #Variable Value Assignment
while(x < 5):    #While Loop
    print(x)    #Log(Print)-Statement
    x += 1    #Loop Increment

pizza_toppings.pop()    #List/ Delete Last Value
pizza_toppings.pop(1)    #List/ Delete Value at index 1

print(person)    #Log(Print)-Statement
person.pop('eye_color')    #Dictionary/ Delete Eye Color Key Pair
print(person)    #Log(Print)-Statement

for topping in pizza_toppings:    #For Loop/
    if topping == 'Pepperoni':    #If Statement
        continue    #Continue
    print('After 1st if statement')    #Log(Print)-Statement
    if topping == 'Olives':    #If Statement
        break    #Break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')    #Log(Print)-Statement

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)