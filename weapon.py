class Weapon:
    def __init__(self, name, weapon_type, damage, value) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value


weapons = [
    Weapon(name='Iron Sword', weapon_type='sharp', damage=5, value=10),
    Weapon(name='Two-handed Sword', weapon_type='sharp', damage=9, value=10),
    Weapon(name='Axe', weapon_type='sharp', damage=8, value=10),
    Weapon(name='Short Bow', weapon_type='ranged', damage=3, value=2),
    Weapon(name='Long Bow', weapon_type='ranged', damage=6, value=5),
    Weapon(name='Fist', weapon_type='blunt', damage=2, value=1),
    Weapon(name="Toddler's Fist", weapon_type='blunt', damage=0.7, value=0),
]
