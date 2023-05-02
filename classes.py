from dataclasses import dataclass
from abc import ABC, abstractmethod

from skills import Skill, FuryPunch, HardShot

#
# class Resource(ABC):
#     @abstractmethod
#     def meth1(self):
#         pass
#
#     def meth2(self):
#         pass

@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill



Warrior = UnitClass(
    name="Warior",
    max_health=60.0,
    max_stamina=30.0,
    attack=0.8,
    stamina=0.9,
    armor=1.2,
    skill=FuryPunch()
    )

Thief = UnitClass(
name="Thief",
    max_health=50.0,
    max_stamina=25.0,
    attack=1.5,
    stamina=1.2,
    armor=1.0,
    skill=HardShot()
    )





unit_classes = {
    Thief.name: Thief,
    Warrior.name: Warrior
}
