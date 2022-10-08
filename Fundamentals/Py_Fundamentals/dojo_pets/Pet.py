# Pet class created to be used as module
class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(this):
        this.energy += 25

    def eat(this):
        this.energy += 5
        this.health += 10

    def play(this):
        this.health += 5

    def noise(this):
        print('Bark Bark')