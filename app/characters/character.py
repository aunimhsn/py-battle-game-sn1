from typing import Self
from gears.armor import Armor
from gears.weapon import Weapon

class Character:

    def __init__(self, 
                 name:str, 
                 hp:int, 
                 armor:Armor, 
                 weapon:Weapon) -> Self:
        self.name = name
        self.hp = hp
        self.armor = armor
        self.weapon = weapon

    def attack(self, target:Self) -> None:
        damage_done = self.weapon.damage * (1 - (target.armor.defense / 100))
        damage_done_rounded = int(round(damage_done, 0))
        target.hp -= damage_done_rounded

        # Bilan
        print(f'{self.name} a attaqué {target.name} et a infligé {damage_done_rounded} de dégâts')
