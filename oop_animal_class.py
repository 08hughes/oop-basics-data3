
class Animal:

    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
        self.alive = True
        self.number_animal_eaten = 0

    def sleep(self):
        return "Zzzzzzzz"

    def eat(self, food):
        self.number_animal_eaten += 1
        return "nom nom"

    def shout_own_name(self):
        return "MY NAME IS " + self.name.upper()






