"""
Chapitre 11.1
"""


import math
from inspect import *

from characters import *


def deal_damage(attacker, defender):
	damage, crit = attacker.compute_damage(defender)
	defender.hp -= damage
	print(f"{attacker.name} used {attacker.weapon.name}")
	if crit:
		print("  Critical hit!")
	print(f"  {defender.name} took {damage} dmg")

def run_battle(c1, c2):
	attacker = c1
	defender = c2
	turn = 1
	print(f"{attacker.name} starts a battle with {defender.name}!")
	while True:
		deal_damage(attacker, defender)
		if defender.hp == 0:
			print(f"{defender.name } is sleeping with the fishes.")
			break
		attacker, defender = defender, attacker
		turn += 1
	return turn


def main():
	try:
		os.mkdir("output")
	except:
		pass

	c1 = Character("Äpik", 200, 150, 70, 70)
	c2 = Character("Gämmor", 250, 100, 120, 60)

	bfg = Weapon("BFG", 100, 69)
	stick = Weapon("OoT Stick", 120, 1)

	c1.weapon = bfg
	c2.weapon = stick

	turns = run_battle(c1, c2)
	print(f"The battle ended in {turns} turns.")

if __name__ == "__main__":
	main()

