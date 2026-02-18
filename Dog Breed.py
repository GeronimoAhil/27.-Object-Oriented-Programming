class Dog:

    animal = 'dog'
    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour

labrador = Dog("labrador", 'Gold')
poodle = Dog("poodle", "cream")

print("Labrador is a {}". format(labrador.animal))
print("Poodle is also a {}". format(poodle.animal))
print("{} is a {} colour dog".format(labrador.breed, labrador.colour))
print("{} is a {} colour dog".format(poodle.breed, poodle.colour))