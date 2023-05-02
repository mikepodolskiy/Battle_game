# import required class
from typing import Optional

from unit import BaseUnit


# defining singleton class with constructor
class BaseSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


# defining Arena class from BaseSingleton
class Arena(metaclass=BaseSingleton):
    STAMINA_PER_ROUND = 1
    player = None
    enemy = None
    game_is_running = False
    battle_result: Optional[str] = None

    def __init__(self):
        self.instance = None

    def start_game(self, player: BaseUnit, enemy: BaseUnit):
        """
        starts game, defines player, enemy and game is running value
        """

        self.player = player
        self.enemy = enemy
        self.game_is_running = True

    def _check_players_hp(self):
        """
        checks players hp, checking if condition for win are satisfied, returns battle result or None if game goes on
        """
        if self.player.hp <= 0:
            if self.enemy.hp > 0:
                self.battle_result = "Игрок проиграл битву"
            else:
                self.battle_result = "Ничья"
        else:
            if self.enemy.hp <= 0:
                self.battle_result = "Игрок выиграл битву"
            else:
                return None

        return self._end_game()

    def _stamina_regeneration(self):
        """
        checks stamina status and possibility for regeneration, regenerates
        """
        if self.player.stamina + self.STAMINA_PER_ROUND < self.player.unit_class.max_stamina:
            self.player.stamina += self.STAMINA_PER_ROUND
        else:
            self.player.stamina = self.player.unit_class.max_stamina
        if self.enemy.stamina + self.STAMINA_PER_ROUND < self.enemy.unit_class.max_stamina:
            self.enemy.stamina += self.STAMINA_PER_ROUND
        else:
            self.enemy.stamina = self.enemy.unit_class.max_stamina

    def next_turn(self) -> Optional[str]:
        """
        checks if game is running, execute actions if yes, checks if battle result, show it, otherwise regenerates
        stamina and returns action result
        """

        if self.game_is_running:
            hit_result = self.enemy.hit(self.player)
            result = self._check_players_hp()
            if result:
                return result
            self._stamina_regeneration()
            return hit_result

    def _end_game(self) -> Optional[str]:
        """
        makes parameters for end game as it should be
        """

        self.instance = {}
        self.game_is_running = False
        return self.battle_result

    def player_hit(self) -> str:

        """
        hit action defining, calls hit method for player, calls next turn, shows result, rival's action
        """
        result = self.player.hit(self.enemy)
        turn_result = self.next_turn()
        return f"{result} <br> {turn_result}"

    def player_use_skill(self):
        """
        use skill action defining, calls hit method for player, calls next turn, shows result, rival's action
        """
        result = self.player.use_skill(self.enemy)
        turn_result = self.next_turn()
        return f"{result} <br> {turn_result}"
