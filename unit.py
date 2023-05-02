# import required libraries and modules
from __future__ import annotations
from abc import ABC, abstractmethod
from equipment import Weapon, Armor
from classes import UnitClass
from random import randint, uniform
from typing import Optional


# creates BaseUnit class, defines common methods for all units
class BaseUnit(ABC):

    def __init__(self, name: str, unit_class: UnitClass):
        """
        При инициализации класса Unit используем свойства класса UnitClass
        """
        self.name: str = name
        self.unit_class: UnitClass = unit_class
        self.hp: float= unit_class.max_health
        self.stamina: float = unit_class.max_stamina
        self.weapon: Optional[Weapon] = None
        self.armor: Optional[Armor] = None
        self._is_skill_used: bool = False

    @property
    def health_points(self) -> float:
        return round(self.hp, 1)

    @property
    def stamina_points(self) -> float:
        return round(self.stamina, 1)

    def equip_weapon(self, weapon: Optional[Weapon]) -> str:
        self.weapon = weapon
        return f"{self.name} экипирован оружием {self.weapon.name}"

    def equip_armor(self, armor: Optional[Armor]) -> str:
        self.armor = armor
        return f"{self.name} экипирован броней {self.weapon.name}"

    def _count_damage(self, target: BaseUnit) -> float:

        # attacker stamina check, if stamina is enough calculate damage considering unit type and weapon type,
        # otherwise damage is 0
        if self.stamina > self.weapon.stamina_per_hit:
            weapon_damage = uniform(self.weapon.min_damage, self.weapon.max_damage) * self.unit_class.attack
            self.stamina -= self.weapon.stamina_per_hit
            # defender stamina check, if stamina is enough - calculate defence considering unit type and armor type,
            # otherwise armor is 0
            if target.stamina > target.armor.stamina_per_turn * target.unit_class.stamina:
                target_armor = target.armor.defence * target.unit_class.armor
                target.stamina -= target.armor.stamina_per_turn * target.unit_class.stamina
            else:
                target_armor = 0

            damage = weapon_damage - target_armor
        else:
            damage = 0

        target.get_damage(damage)
        return round(damage, 1)

    def get_damage(self, damage: float) -> Optional[float]:
        """
        Calculating hp according to damage that was done
        """
        if damage > 0:
            if self.hp - damage > 0:
                self.hp -= damage
            else:
                self.hp = 0
        return self.hp

    @abstractmethod
    def hit(self, target: BaseUnit) -> str:
        """
        abstract method tbd
        """
        pass

    def use_skill(self, target: BaseUnit) -> str:
        """
        Method describes skill using, returns message that skill was used, or applies action of skill and defines
        flag of skill using
        """
        if self._is_skill_used:
            return "Навык использован"
        else:
            self._is_skill_used = True
            return self.unit_class.skill.use(user=self, target=target)


# creates player class
class PlayerUnit(BaseUnit):

    def hit(self, target: BaseUnit) -> str:
        """
        Method for hit, checks stamina for action, calculates damage and shows message relative to stamina / damage
        status
        """
        if self.stamina < self.weapon.stamina_per_hit:
            return f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."
        damage = self._count_damage(target)
        if damage > 0:
            return f"{self.name} используя {self.weapon.name} пробивает {target.armor.name} " \
                   f"соперника и наносит {damage} урона."
        if damage <= 0:
            return f"{self.name} используя {self.weapon.name} наносит удар, но {target.armor.name} cоперника " \
                   f" его останавливает."


class EnemyUnit(BaseUnit):

    def hit(self, target: BaseUnit) -> str:
        """
        Method for hit, checks stamina for action, calculates damage and shows message relative to stamina / damage
        status
        """

        if not self._is_skill_used and self.stamina > self.unit_class.skill.stamina and randint(1, 10) == 1:
            return self.use_skill(target)

        if self.stamina < self.weapon.stamina_per_hit:
            return f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."
        damage = self._count_damage(target)
        if damage > 0:
            return f"{self.name} используя {self.weapon.name} пробивает {target.armor.name} " \
                   f"и наносит Вам {damage} урона."
        if damage <= 0:
            return f"{self.name} используя {self.weapon.name} наносит удар, но Ваш(а) {target.armor.name}" \
                   f" его останавливает."
