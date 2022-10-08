# Import pet class to use here
import Pet

# Ninja class created with constructors for having a pet
class Ninja:
    def __init__(self, first_name, last_name, pet, pet_food, treats):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.pet_food = pet_food
        self.treats = treats

# Class method invokes pet method
    def walk(this):
        print('Going on a walk')
        this.pet.play()

# Class method invokes pet method
    def feed(this):
        print("Here is some food boy")
        this.pet.eat()

# Class method invokes pet method
    def bathe(this):
        this.pet.noise()
        print('Sorry but you have to get clean')

# Created sub-class of pets via inheritance
class ninjaPet(Pet.Pet):
    def __init__(self, name, type, tricks, health, energy):
        super().__init__(name, type, tricks, health, energy)
        super().sleep()
        super().play()
        super().eat()
        super().noise()

# Created a pet instance from import
pet1 = Pet.Pet('Ryder', 'Belgian Sheep Dog', ['slober', 'eat', 'sleep'], 80, 60)

# Created pet instance from inherited sub-class
pet2 = ninjaPet('Tank', 'Pitbull', ['slober', 'eat', 'sleep'], 100, 100)


# Created Ninja instances using our newly created pets
ninja1 = Ninja('Jane', 'Doe', pet1, 'Purina', 'Bacon Bits')
ninja2 = Ninja('Steve', 'Hill', pet2, 'Raw Meat', 'Bacon Bits')

# Invoking ninja methods then invoke the imported pet class methods
ninja1.walk()
ninja1.feed()
ninja1.bathe()

ninja2.walk()
ninja2.feed()
ninja2.bathe()