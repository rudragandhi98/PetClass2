import datetime
from datetime import date
from dataclasses import make_dataclass, dataclass


@dataclass
class Pet:
    breed: str
    name: str
    color: str
    gender: int
    species: str
    owner: str
    address: str
    birthday: datetime

    def setSpecies(self, new_species):
        self.species = new_species
    def setBreed(self, new_breed):
        self.breed = new_breed
    def setName(self, new_name):
        self.name = new_name
    def setColor(self, new_color):
        self.color = new_color
    def setGender(self, new_gender):
        self.gender = new_gender
    def setOwner(self, new_owner):
        self.owner = new_owner
    def setAddress(self, new_address):
        self.address = new_address
    def setBirthday(self, new_birthday):
        if type(new_birthday) == date:
            self.birthday = new_birthday
    def displayGender(self):
        if self.gender == 1:
            print('Male')
        elif self.gender == 0:
            print('Female')
        else:
            print('Unkonwn Gender')
    def getAge(self):
        try:
            now = date.today()
            return (now - self.birthday).days // 365
        except TypeError:
            return None
    def displayAge(self):
        if self.getAge() == None:
            print("Unknow Age")
        else:
            print(self.name + " is " + str(self.getAge()) + " year old.")


@dataclass
class Dog(Pet):
    species: str = 'Canis Familiaris'
    owner: str = None
    address: str = None
    birthday: datetime = None

    def getAge(self):
        try:
            now = date.today()
            return (now - self.birthday).days
        except TypeError:
            return None
    def displayAge(self):
        if self.getAge() == None:
            print("Unknow Age")
        else:
            print(self.name + " is " + str(self.getAge()) + " day old.")


@dataclass
class Puppy(Dog):
    def play(self):
        return "(___()'`;\n      /,    /`\n      \\\\\"--\\\\"
    def getAge(self):
        try:
            now = date.today()
            return (now - self.birthday).days // 30
        except TypeError:
            return None
    def displayAge(self):
        if self.getAge() == None:
            print("Unknow Age")
        else:
            print(self.name + " is " + str(self.getAge()) + " month old.")


# Testing the classes and functions
pet = Pet('Beaglier','Bella','White',0b1,'Dog','Sally','123 Campus Dr, San Jose, CA 91231',date(2018,5,17))
print(pet)
print()
pet.displayAge()
print()
print("Address is "+pet.address)
print("Owner is "+pet.owner)
pet.setOwner('Mary')
print('Change the owener to '+pet.owner)
print('\nGender: ')
pet.displayGender()

dog = Dog('Beaglier','Bella','White',0b0)
print(dog)
print()
dog.setBirthday(date(2016,1,2))
dog.displayAge()
print()
dog.setColor('Brown')
print('Change the color to '+dog.color)
print()
print('Gender: ')
dog.displayGender()


puppy = Puppy('Beaglier','Bella','White',12)
print(puppy)
print()
puppy.displayAge()
puppy.displayGender()