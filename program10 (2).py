"""
Name: Adam Stafford in collaboration with Sean Boyle
Date: 11-27-2023
Program: Epic Battle! This program will allow users to choose between three playabale characters to fight in turn-based combat against an NPC outputting random attacks or defenses.
"""
#random function for NPC movements 
import random

class Character:
    #constructor for properties
    def __init__(self, name, class_type, hp, strength, defense):
        self._name = name
        self._class_type = class_type
        self._hp = hp
        self._strength = strength
        self._defense = defense
        
    #getters and setters accordingly
    def get_name(self):
        return self._name

    def get_class_type(self):
        return self._class_type
    #we utilize the round function to round the decimal to the nearest 2 decimal places
    def get_hp(self):
        return round(self._hp, 1)

    def set_hp(self, new_hp):
        self._hp = new_hp
    #methods accordingly
    #strength is a character's damage, the base damage is 40, so if the opponent has no defense, it will read as 1-0, and will multiply the damage output accordingly (1 * your strength)
    #calculates how much damage you will do to an enemy if enemcy is using defense or not. 
    def calculate_attack(self, opponent_defense):
        return round(self._strength * (1 - opponent_defense), 2)

    def is_still_alive(self):
        return self._hp > 0

#ChatGPT assisted us in creating a dictionary to hold character traits.
#We can now utilize keys to call upon the character traits we need throughout the rest of the program.
#We also learned that dictionaries are incredibly helpful tools!
character_types = {
    "Fighter": {"hp": 120, "strength": 40, "defense": 0.2},
    "Unicorn": {"hp": 80, "strength": 35, "defense": 0.6},
    "Battle Monk": {"hp": 100, "strength": 20, "defense": 0.42}
}

###MAIN PROGRAM###
# Creating player's character from the class
player_name = input("Enter your name: ")
print("Choose your character type: Fighter, Unicorn, Battle Monk")
player_type = input("Enter your battle class: ")
while player_type not in character_types:
    print("Invalid type. Choose from Fighter, Unicorn, Battle Monk.")
    player_type = input("Enter your battle class: ")

player_data = character_types[player_type]
player = Character(player_name, player_type, **player_data)

# Creating computer's character by accessing character types from the key in the dictionary written previosuly.
npc_name = random.choice(["Megabyte", "Hex", "Glitch"])
npc_type = random.choice(list(character_types.keys()))
npc_data = character_types[npc_type]
npc = Character(npc_name, npc_type, **npc_data)

print("{} the {}, your opponent is {} the {}!".format(player.get_name(), player.get_class_type(), npc.get_name(), npc.get_class_type()))

#The battle sequence and bulk of the program.
round_number = 1
while player.is_still_alive() and npc.is_still_alive():
    print("-Round {}-".format(round_number))
    player_action = input("Do you (a)ttack or (d)efend? ").lower() #lowercases anything outputted for cohesion 

    npc_action = random.choice(["attack", "defend"])
   
    if player_action == 'a':
        damage = player.calculate_attack(npc_data["defense"])
        npc.set_hp(npc.get_hp() - damage)
        print("{} the {} attacked {} the {}! \n{} now has {} HP.".format(player.get_name(), player.get_class_type(), npc.get_name(), npc.get_class_type(), npc.get_name(), npc.get_hp()))
    else:
        print("{} the {} is on guard.".format(player.get_name(), player.get_class_type()))
    
    if npc_action == 'attack':
        damage = npc.calculate_attack(player_data["defense"])
        player.set_hp(player.get_hp() - damage)
        print("{} the {} attacked {} the {}! \n{} now has {} HP.".format(npc.get_name(), npc.get_class_type(), player.get_name(), player.get_class_type(), player.get_name(), player.get_hp()))
    else:
        print("{} the {} is on guard.".format(npc.get_name(), npc.get_class_type()))

    round_number += 1

# Determines the winner of the epic battle!
if player.is_still_alive():
    print("{} the {} was defeated...".format(npc.get_name(), npc.get_class_type()))
    print("{} the {} wins!".format(player.get_name(), player.get_class_type()))
else:
    print("{} the {} was defeated...".format(player.get_name(), player.get_class_type()))
    print("{} the {} wins!".format(npc.get_name(), npc.get_class_type()))
    
    
