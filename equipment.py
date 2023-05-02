# import required libraries and modules
from dataclasses import dataclass
from typing import Optional
from random import uniform
import marshmallow_dataclass
import marshmallow
import json


# creating Armor dataclass according to flow
@dataclass
class Armor:
    id: int
    name: str
    defence: float
    stamina_per_turn: float


# creating Weapon dataclass according to flow
@dataclass
class Weapon:
    id: int
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    @property
    def damage(self):
        """
        method for real damage in required range
        """
        actual_damage = round(uniform(self.min_damage, self.max_damage), 1)
        return actual_damage


# creating Equipment class fo lists of possible weapons and armors from the source
@dataclass
class EquipmentData:
    weapons: list[Weapon]
    armors: list[Armor]


# creating Equipment class
class Equipment:

    def __init__(self):
        self.equipment = self._get_equipment_data()

    def get_weapon(self, weapon_name) -> Optional[Weapon]:
        """
        method for getting weapon object by name
        """
        for item in self.equipment.weapons:
            if item.name == weapon_name:
                return item
        return None

    def get_armor(self, armor_name) -> Optional[Armor]:
        """
        method for getting armor object by name
        """
        for item in self.equipment.armors:
            if item.name == armor_name:
                return item
        return None

    def get_weapons_names(self) -> list:
        """
        method for getting list of weapons names
        """
        return [item.name for item in self.equipment.weapons]

    def get_armors_names(self) -> list:
        """
        method for getting list of weapons names
        """
        return [item.name for item in self.equipment.armors]

    @staticmethod
    def _get_equipment_data() -> EquipmentData:
        """
        method for loading data from file to Equipment data instance
        """
        with open("./data/equipment.json") as f:
            data = json.load(f)
            equipment_schema = marshmallow_dataclass.class_schema(EquipmentData)
        try:
            return equipment_schema().load(data)
        except marshmallow.exceptions.ValidationError:
            raise ValueError
