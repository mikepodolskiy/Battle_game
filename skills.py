# import required libraries
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from unit import BaseUnit

# creates abstract class from ABC
class Skill(ABC):
    """
    Defines abstract methods
    """
    user = None
    target = None

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def stamina(self):
        pass

    @property
    @abstractmethod
    def damage(self):
        pass

    @abstractmethod
    def skill_effect(self) -> str:
        pass

    def _is_stamina_enough(self):
        return self.user.stamina >= self.stamina

    def use(self, user: BaseUnit, target: BaseUnit) -> str:
        """
        checks if stamina enough for some action, applies action, shows required message
        """
        self.user = user
        self.target = target
        if self._is_stamina_enough():
            return self.skill_effect()
        return f"{self.user.name} попытался использовать {self.name} но у него не хватило выносливости."


# creating special skills classes from Skill class, defines its effects
class FuryPunch(Skill):
    name = "Fury punch"
    stamina = 6
    damage = 12

    def skill_effect(self):
        self.user.stamina -= round(self.stamina, 1)
        self.target.get_damage(round(self.damage, 1))

        return f"{self.user.name} использует {self.name} и наносит {self.damage} урона сопернику."


class HardShot(Skill):
    name = "Hard shot"
    stamina = 5
    damage = 15

    def skill_effect(self):
        self.user.stamina -= round(self.stamina, 1)
        self.target.get_damage(round(self.damage, 1))

        return f"{self.user.name} использует {self.name} и наносит {self.damage} урона сопернику."
