class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """


    def __init__(self, name: str, power: str, health: int):
        # TODO: Initialize the superhero's attributes here
        self.name = name
        self.power = power
        self.health = health


# TODO: Create Superhero instances
Hero = SuperHero("Batman", "Intelligence", 100)
Hero1 = SuperHero("Superman", "Strength", 150)


# TODO: Print out the attributes of each superhero
print(Hero.name)
print(Hero.power)
print(Hero.health)
print(Hero1.name)
print(Hero1.power)
print(Hero1.health)

