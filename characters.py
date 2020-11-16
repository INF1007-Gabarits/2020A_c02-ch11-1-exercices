"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import random

import utils


class Weapon:
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""

	UNARMED_POWER = 20

	def __init__(self, name, power, min_level):
		self.__name = name
		self.power = power
		self.min_level = min_level

	@property
	def name(self):
		return self.__name

	@classmethod
	def make_unarmed(cls):
		return cls("Unarmed", UNARMED_POWER, 1)


class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defence: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""

	def __init__(self, name, max_hp, attack, defence, level):
		self.name = name
		self.level = level
		self.max_hp = max_hp
		self.attack = attack
		self.defence = defence
		self.weapon = None
		self.hp = self.max_hp

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, val):
		self.__name = val

	@property
	def weapon(self):
		return self.__weapon

	@weapon.setter
	def weapon(self, val):
		if val is None:
			val = Weapon.make_unarmed()
		if val.min_level > self.level:
			raise ValueError(Weapon)
		self.__weapon = val

	@property
	def hp(self):
		return self.__hp

	@hp.setter
	def hp(self, val):
		self.__hp = utils.clamp(val, 0, self.max_hp)

	def compute_damage(self, other):
		level_factor = (2 * self.level) / 5 + 2
		weapon_factor = self.weapon.power
		atk_def_factor = self.attack / other.defence
		critical = random.random() <= 1/16
		modifier = (2 if critical else 1) * random.uniform(0.85, 1.0)
		damage = ((level_factor * weapon_factor * atk_def_factor) / 50 + 2) * modifier
		return int(round(damage)), critical

