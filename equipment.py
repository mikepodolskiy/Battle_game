import random
from dataclasses import dataclass
from typing import List, Optional
from random import uniform
import marshmallow_dataclass
import marshmallow
import json


@dataclass
class Armor:
    id: int
    name: str
    defence: float
    stamina_per_turn: float



@dataclass
class Weapon:
    id: int
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float


    @property
    def damage(self):
        actual_damage = uniform(low=self.min_damage, high=self.max.damage, size=None)
        return actual_damage


@dataclass
class EquipmentData:
    # TODO содержит 2 списка - с оружием и с броней
    weapons: list[Weapon]
    armors: list[Armor]


class Equipment:

    def __init__(self):
        self.equipment = self._get_equipment_data()

    def get_weapon(self, weapon_name) -> Optional[Weapon]:
        for item in self.equipment.weapons:
            if item.name == weapon_name:
                return item
        return None

    def get_armor(self, armor_name) -> Optional[Armor]:
        # TODO возвращает объект брони по имени
        for item in self.equipment.armors:
            if item.name == armor_name:
                return item
        return None

    def get_weapons_names(self) -> list:
        return [item.name for item in self.equipment.weapons]

    def get_armors_names(self) -> list:
        return [item.name  for item in self.equipment.armors]

    @staticmethod
    def _get_equipment_data() -> EquipmentData:
        # TODO этот метод загружает json в переменную EquipmentData
        with open("./data/equipment.json") as f:
            data = json.load(f)
            equipment_schema = marshmallow_dataclass.class_schema(EquipmentData)
        try:
            return equipment_schema().load(data)
        except marshmallow.exceptions.ValidationError:
            raise ValueError



