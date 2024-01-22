from character import Player, Enemy
from weapon import weapons
import random
import time
import sys


def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <player_1_name> <player_2_name>")
        sys.exit(1)

    player_1_name = sys.argv[1]
    enemy_name = sys.argv[2]

    player_1 = Player(name=player_1_name, health=100)
    enemy = Enemy(name=enemy_name, health=100)

    while player_1.health > 2 and enemy.health > 2:
        player_1.equip(random.choice(weapons))
        enemy.equip(random.choice(weapons))
        player_1.attack(enemy)
        enemy.attack(player_1)

        player_1.health_bar.draw()
        enemy.health_bar.draw()
        # sleeper to notice fight progress in bash #
        time.sleep(0.75)
        print()
    if player_1.health > enemy.health:
        print(f'-----|    {player_1_name.upper()} won!  Drink young Viking! SKÅL!!    |-----')
    else:
        print(f'-----|    {enemy_name.upper()} won!  Drink young Viking! SKÅL!!    |-----')


if __name__ == "__main__":
    main()
