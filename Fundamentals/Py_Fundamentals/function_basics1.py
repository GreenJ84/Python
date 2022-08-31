# #1
# def number_of_food_groups():
#     return 5    #returns 5
# print(number_of_food_groups())    #prints returned value
# #*Prints the number 5
# #*The value reurned in the function


# #2
# def number_of_military_branches():
#     return 5    #Returns 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())    #number_of_days_in_a_week_silicon_or_triangle_sides() Doesnt Exist
# # #*Error? The first function call is calling a function that has not been defined


# #3
# def number_of_books_on_hold():
#     return 5    #Reutrns 5, ends function
#     return 10
# print(number_of_books_on_hold())
# #*Prints the Number 5.
# #*The first return ends the function as it returns the 5 value.


# #4
# def number_of_fingers():
#     return 5    #Returns 5, ends function
#     print(10)
# print(number_of_fingers())
# #*Prints the Number 5,
# #*Same reason as previous problem


# #5
# def number_of_great_lakes():
#     print(5)    #Prints 5
# x = number_of_great_lakes()    #Sets x equal to a unefined value
# print(x)    #Tries printing an undefined value
# #*Prints 5 for the function print statement.
# #*Creates an error? Function returns no value which means x would be undefined?
# #!No error, returned none when printing the empty x variable

# #6
# def add(b,c):
#     print(b+c)    #Prints the sum each time function called
# print(add(1,2) + add(2,3))    #Tries to print some of 2 undefined valueds (nothing returned)
# #*Prints 3 and 5 respective to the inner print during function calls.
# #*Creates error? Can't print a value for the functions as nothing is returned
# #!empty function calls are "non-type" (not undefined.)
# #!Error, can't operate with "non-type"

# #7
# def concatenate(b,c):
#     return str(b)+str(c)    #Prints the string type concatenation of given arguemnts
# print(concatenate(2,5))
# #*Returns a string "25"



# #8
# def number_of_oceans_or_fingers_or_continents():
#     b = 100    #Defines variable b
#     print(b)    #Prints b
#     if b < 10:    #b is not less than 10
#         return 5
#     else:
#         return 10    #Returns 10 value, ends function
#     return 7
# print(number_of_oceans_or_fingers_or_continents())
# #*Prints 100
# #*Prints 10


# #9
# def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# #*Prints 7 for the first function call/return
# #*Prints 14 for the second function call/return
# #*Prints 21 as a sum of the first and second function calls



# #10
# def addition(b,c):
#     return b+c    #Retruns the paramater sum and ends function
#     return 10
# print(addition(3,5))
# #*Prints 8


# #11
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
# print(b)
# foobar()
# print(b)
# #*Prints 500
# #*Prints 300?
# #!Weird, Why is this 500? Because its within the function indention?
# #*Prints 300?
# #!yet this is 300? because the function unindented but the block hadn't ended?
# #*Prints 500?


# #12
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# foobar()
# print(b)
# #*Prints 500
# #*Prints 500
# #*Prints 300
# #*Prints 300
# #!Got me, it returned a vlue but wasnt saved anywhere /.-


# #13
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=foobar()
# print(b)
# #*Prints 500
# #*Prints 500
# #*Prints 300
# #*Prints 300


# #14
# def foo():
#     print(1)
#     bar()
#     print(2)
# def bar():
#     print(3)
# foo()
# #*Prints 1
# #*Prints 3
# #*Prints 2


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#*Prints 1
#*Prints 3
#*Prints 5 (bar() returned value)
#*Prints 10 (foo() returned value)
