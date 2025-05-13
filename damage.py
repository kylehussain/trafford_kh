import random
import sys
import time



def battle():
    PlayerHP = 10
    EnemyHP = 10
    while EnemyHP or PlayerHP > 0:
        print("[1] Attack [2] Defend [3] Run")
        choice = input("> ").strip()
        if choice == '1':
            EnemyATK, PlayerATK = random.sample(range(1,5),2)
            print("You swing your sword.")
            EnemyHP = EnemyHP - PlayerATK
            print("You hit the enemy.")
            print(f"You dealt {PlayerATK} damage.")
            print(f"The enemy's HP is now: {EnemyHP}")
            time.sleep(1)
            print("The enemy swings their sword at you.")
            PlayerHP = PlayerHP - EnemyATK
            print(f"The enemy hits you for {EnemyATK} damage.")
            print(f"Your HP is {PlayerHP}.")
            time.sleep(1)
            if EnemyHP <= 0:
                print("You defeat the enemy.")
                exit()
            elif PlayerHP <= 0:
                print("The enemy defeats you.")
                exit()

def main():
    battle()

main()
    