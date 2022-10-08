import Pet

class Ninja:
    def __init__(self, first_name, last_name, pet, pet_food, treats):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.pet_food = pet_food
        self.treats = treats

    def walk(this):
        print('Going on a walk')
        this.pet.play()

    def feed(this):
        print("Here is some food boy")
        this.pet.eat()

    def bathe(this):
        this.pet.noise()
        print('Sorry but you have to get clean')

class ninjaPet(Pet.Pet):
    def __init__(self, name, type, tricks, health, energy):
        super().__init__(name, type, tricks, health, energy)
        super().play()
        super().eat()
        super().noise()

pet1 = ninjaPet('Ryder', 'Belgian Sheep Dog', ['slober', 'eat', 'sleep'], 80, 60)

ninja1 = Ninja('Jane', 'Doe', pet1, 'Purina', 'Bacon Bits')

ninja1.walk()
ninja1.feed()
ninja1.bathe()