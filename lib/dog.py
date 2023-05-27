#!/usr/bin/env python3

class Dog:

    # breed = "Mutt"

    def __init__(self, dog_name, breed = "Mutt"):
        self.name = dog_name
        self.breed = breed

dog = Dog(dog_name="Bosco", breed="German")
# bosco = Dog(dog_name="Bosco", breed="breed")
print(dog.breed)
