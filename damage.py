import random
import time

def battle():
    PlayerHP = 10
    EnemyHP = 10
    while EnemyHP > 0 and PlayerHP > 0: 
        print("[1] Attack [2] Defend [3] Run")
        choice = input("> ").strip()
        if choice == '1':
            PlayerATK = random.randint(1, 5) #Initiate random attack inside the loop to ensure random number generation is truly random
            EnemyATK = random.randint(1, 5)

            print("You swing your sword.")
            EnemyHP -= PlayerATK
            print(f"You dealt {PlayerATK} damage.")
            print(f"The enemy's HP is now: {EnemyHP}")
            time.sleep(1)

            if EnemyHP <= 0:
                print("You defeat the enemy.")
                break

            print("The enemy swings their sword at you.")
            PlayerHP -= EnemyATK
            print(f"The enemy hits you for {EnemyATK} damage.")
            print(f"Your HP is now: {PlayerHP}")
            time.sleep(1)

            if PlayerHP <= 0:
                print("The enemy defeats you.")
                break
        if choice == '2':
            EnemyATK = random.randint(1, 3)
            print("You fortify yourself.")
            print("The enemy swings their sword at you.")
            PlayerHP -= EnemyATK
            print(f"The enemy hits you for {EnemyATK} damage.")
            print(f"Your HP is now: {PlayerHP}")
            time.sleep(1)

            if PlayerHP <= 0:
                print("The enemy defeats you.")
                break

        if choice == '3':
            print("You flee from battle.")
            break


def main():
    battle()

main()

    