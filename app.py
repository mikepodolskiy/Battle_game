# import required libraries and modules
from typing import Type
from flask import Flask, render_template, request, redirect, url_for

from base import Arena
from classes import unit_classes
from equipment import Equipment
from unit import BaseUnit, PlayerUnit, EnemyUnit

# starting app
app = Flask(__name__)

# defining dict with rivals
heroes: dict[str, BaseUnit] = {
    "player": Type[BaseUnit],
    "enemy": Type[BaseUnit]
}

# initializing Arena class instance
arena = Arena()


# view of main page according to template
@app.route("/")
def menu_page():
    return render_template("index.html")


# endpoint fight defining
@app.route("/fight/")
def start_fight():
    """
    starts game, passes heroes to template, returns data according template
    """
    arena.start_game(player=heroes["player"], enemy=heroes["enemy"])

    return render_template("fight.html", heroes=heroes)


@app.route("/fight/hit")
def hit():
    """
    hit button definition, refreshing template according to game status in required template
    """

    if arena.game_is_running:
        result = arena.player_hit()
    else:
        result = arena.battle_result
    return render_template("fight.html", heroes=heroes, result=result)


@app.route("/fight/use-skill")
def use_skill():
    """
    use skill button definition, the same as hit button
    """
    if arena.game_is_running:
        result = arena.player_use_skill()
    else:
        result = arena.battle_result
    return render_template("fight.html", heroes=heroes, result=result)


@app.route("/fight/pass-turn")
def pass_turn():
    """
    pass the turn button definition, the same as hit and use skill, but with next turn in case of game is running
    """
    if arena.game_is_running:
        result = arena.next_turn()
    else:
        result = arena.battle_result
    return render_template("fight.html", heroes=heroes, result=result)


@app.route("/fight/end-fight")
def end_fight():
    """
    end game button definition, returns to main menu
    """
    arena._end_game()
    return render_template("index.html", heroes=heroes)


@app.route("/choose-hero/", methods=['post', 'get'])
def choose_hero():
    """
    choose hero menu, on GET method getting data from forms, on POST method creates player object, equips it,
    and redirect to enemy choose endpoint
    """
    equipment = Equipment()
    if request.method == "GET":
        header = "Choose Hero"
        weapons = equipment.get_weapons_names()
        armors = equipment.get_armors_names()
        result = {
            "header": header,
            "classes": unit_classes,
            "weapons": weapons,
            "armors": armors
        }
        return render_template("hero_choosing.html", result=result)


    elif request.method == "POST":
        name = request.form["name"]
        unit_class_title = request.form["unit_class"]
        weapon = request.form["weapon"]
        armor = request.form["armor"]

        player = PlayerUnit(name=name, unit_class=unit_classes.get(unit_class_title))

        player.equip_weapon(Equipment().get_weapon(weapon))
        player.equip_armor(Equipment().get_armor(armor))

        heroes["player"] = player

        return redirect(url_for("choose_enemy"))


@app.route("/choose-enemy/", methods=['post', 'get'])
def choose_enemy():
    """
    the same as choose player, but redirect to start fight endpoint in case of POST
    """
    equipment = Equipment()
    if request.method == "GET":
        header = "Choose Rival"
        weapons = equipment.get_weapons_names()
        armors = equipment.get_armors_names()
        result = {
            "header": header,
            "classes": unit_classes,
            "weapons": weapons,
            "armors": armors
        }
        return render_template("hero_choosing.html", result=result)


    elif request.method == "POST":
        name = request.form["name"]
        unit_class_title = request.form["unit_class"]
        weapon = request.form["weapon"]
        armor = request.form["armor"]

        enemy = EnemyUnit(name=name, unit_class=unit_classes.get(unit_class_title))

        enemy.equip_weapon(Equipment().get_weapon(weapon))
        enemy.equip_armor(Equipment().get_armor(armor))

        heroes["enemy"] = enemy

        return redirect(url_for('start_fight'))
