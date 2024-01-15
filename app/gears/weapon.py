from typing import Self

class Weapon:
    def __init__(self, name:str, damage:int) -> Self:
        self.name = name
        self.damage = damage