equipment = {
  "weapons": [
   {
    "id": 1,
    "name": "топорик",
    "min_damage": 2.5,
    "max_damage": 4.1,
    "stamina_per_hit": 1.8
  },
  {
    "id": 2,
    "name": "ножик",
    "min_damage": 1.2,
    "max_damage": 2.5,
    "stamina_per_hit": 1.3
  },
  {
  "id": 3,
  "name": "ладошки",
  "max_damage": 1,
  "min_damage": 0.5,
  "stamina_per_hit": 1
  }
],
  "armors": [
  {
    "id": 1,
    "name": "футболка",
    "defence": 0,
    "stamina_per_turn": 0
    },
    {
    "id": 2,
    "name":"кожаная броня",
    "defence": 1.2,
    "stamina_per_turn": 1
    },
    {
    "id": 3,
    "name": "панцирь",
    "defence": 2.0,
    "stamina_per_turn": 1.6
    }
  ]
}

def get_weapons_names(object) -> list:
    return [weapon.name for weapon in object.weapons]

# print(get_weapons_names(equipment))

heroes = {
    "player": 1,
    "enemy": 2
}
print(heroes.keys())
