# import required libraries and modules
from dataclasses import dataclass

from skills import Skill, FuryPunch, HardShot


# defining dataclass Unitclass according to flow
@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


# defining Warrior class from Unitclass according to flow
Warrior = UnitClass(
    name="Warrior",
    max_health=60.0,
    max_stamina=30.0,
    attack=0.8,
    stamina=0.9,
    armor=1.2,
    skill=FuryPunch()
)

# defining Thief class from Unitclass according to flow
Thief = UnitClass(
    name="Thief",
    max_health=50.0,
    max_stamina=25.0,
    attack=1.5,
    stamina=1.2,
    armor=1.0,
    skill=HardShot()
)

# creating dict of objects
unit_classes = {
    Thief.name: Thief,
    Warrior.name: Warrior
}
