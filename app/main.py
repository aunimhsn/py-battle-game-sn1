from gears.armor import Armor
from gears.weapon import Weapon
from characters.character import Character

diamond_plate = Armor('Diamond Plate', 18)
iron_plate = Armor('Iron Plate', 11)

diamond_sword = Weapon('Diamond Sword', 33)
iron_scepter = Weapon('Iron Scepter', 22)

character_1 = Character('Berdan', 100, diamond_plate, iron_scepter)
character_2 = Character('Antoine', 100, iron_plate, diamond_sword)

character_2.attack(character_1)
