
# Create a file with a local variable, function, and User class (w/ name attribute & Hello greeting function)
local_val = "magical unicorns"
def square(x):
    return x * x
class User:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        return "Hello"

# Print the variable, the square of 5, and the name and greeting of a new User instance
print(local_val)
print(square(5))
user = User("Anna")
print(user.name)
print(user.say_hello())

# This statement makes a certain print statement if the original file is ran, and a different statment if any imports run it.
if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)