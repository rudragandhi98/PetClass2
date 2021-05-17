# I have added dataclasses and exception handling

import datetime
from dataclasses import dataclass

@dataclass
class Pet:

    def __init__(self, name, species, breed, color, gender, owner, address, birthdate, age):
        self.name = name
        self.species = species
        self.breed = breed
        self.color = color
        self.gender = gender
        self.owner = owner
        self.address = address
        self.birthdate = birthdate
        self.age = int(age)

    def getDate(self):
        return datetime.datetime(self.birthdate)

    def getAge(self):
        return int(self.age)

    def description(self):
        return f"{self.name} is {self.getAge()} and is a {self.species} and is {self.color}"


@dataclass
class Dog(Pet):
    species: str = 'Canis Familiaris'
    name: str = None
    breed: str = None
    color: str = None
    gender: str = None


@dataclass
class Puppy(Dog):
    def __init__(self, name, breed, color, gender, age):
        self.name = name
        self.breed = breed
        self.color = color
        self.gender = gender
        self.age = age

    # Exception Handling
    def getAge(self):
        try:
            return f"{self.age * 12} months old"
        except TypeError:
            return None

    def play(self):
        return("(___()'`;\n      /,    /`\n      \\\\\"--\\\\")


def main():
    name = "Danny"
    species = Dog.species
    breed = "Golden Retriever"
    color = "golden"
    gender = "female"
    owner = "Ishant"
    address = "San Jose, CA"
    birthdate = datetime.datetime(2010, 4, 14)
    age = 7

    pet_specs = Pet(name, species, breed, color, gender, owner, address, birthdate, age)
    pet_specs1 = Dog(species, breed, color, gender)
    pet_specs2 = Puppy(name, breed, color, gender, age)

    print(pet_specs.description())
    print(pet_specs1.species)
    print(pet_specs.birthdate)
    print(pet_specs2.play())
    print(pet_specs2.getAge())
    print(pet_specs2.description())



main()

