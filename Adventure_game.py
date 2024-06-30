import time
import random


def print_pause(*txt):
    txt = ''.join(txt)
    print(txt)
    time.sleep(2)


def intro():
    print_pause(
        "You find yourself as Kratos 'the god of war' ",
        "standing in an open field,",
        " filled with volcanos and weird looking monsters.",
    )
    print_pause(
        "Rumor has it that a danger is somewhere around here,",
        "and has been terrifying the nearby villages.",
    )

    print_pause("...")


def fight(enemy, damage, weapon):
    # Things that happen when the player fights
    print_pause(f"you withdraw {weapon[0]} and the shines of it blind {enemy}")
    print_pause(f"you take advantage in this moment and hit {enemy}")
    print_pause(f"{enemy} is now full of rage hitting you so fast")
    print_pause(f"{enemy} managed to hit you and obtain a damage to you")
    print_pause(f"{enemy} damaged you by {damage}%")
    health = 100
    health = health - damage
    if health == 0:
        print_pause(f"{enemy} hit you so hard!!")
        print_pause(f"you are defeated !!!!")
    else:
        print_pause(f"your health is {health}%")
        print_pause(f"you get angry and full of rage hitting {enemy}",
                    " so hard that he can't block you")
        print_pause(f"congratulations Kratos you are indeed the god of war")
        print_pause(f"{enemy} has been defeated")
        print_pause(f"Kratos wins !!!!!")


def cave(enemy, damage, weapon):
    # Things that happen to the player goes in the cave
    if "Blades of Chaos" in weapon:
        print_pause("you already have the Blades of Chaos")
        print_pause("you return to the field , nothing to do here")
        field(enemy, damage, weapon)
    else:
        print_pause("you find a shiny tool what is that!!")
        print_pause("you remmeber this weapon you used it in the past")
        print_pause(
            "In your hand you hold the Blades of Chaos,"
            "very powerful weapon given to you by Ares."
        )
        print_pause("you head back to the field")
        weapon.append("Blades of Chaos")
        field(enemy, damage, weapon)


def field(enemy, damage, weapon):
    # Things that happen when the player runs back to the field
    print_pause(
        "You find yourself standing in an open field,"
        " filled with volcanos and rocks"
    )
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("Enter 1 to knock on the door of the house. ")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    while True:
        choice = input("(Please enter 1 or 2).\n")
        if choice == "1":
            house(enemy, damage, weapon)
            break
        elif choice == "2":
            cave(enemy, damage, weapon)
            break
        else:
            pass


def house(enemy, damage, weapon):
    # Things that happen to the player in the house
    print_pause(f"you walk into the house and find {enemy}",
                " full of rage and anger")
    while True:

        print_pause(f"Do you want to fight {enemy}")
        choice = (input("Enter yes(y) or no(n) \n")).lower()
        if choice == "y":
            if "Blades of Chaos" in weapon:
                fight(enemy, damage, weapon)
                break
            else:
                print_pause(
                    "yes you are Kratos but without any weapons",
                    f" you give leverege to {enemy}"
                )
                print_pause("you are defeated!")
                break
        elif choice == "n":
            print_pause("you walk a way slowly and head back to the field")
            field(enemy, damage, weapon)
            break
        else:
            print_pause("Sorry i didn't understand!!")
            pass


def main():
    enemy = ["Odin", "Thor", "Zeus"]
    enemy = random.choice(enemy)
    damage = random.randint(20, 100)
    weapon = []

    intro()
    field(enemy, damage, weapon)
    print_pause("game over!!")
    while True:
        choices = (input("Would you like to play again! (y/n) ")).lower()
        if choices == "y":
            main()
        elif choices == "n":
            break
        else:
            print_pause("Sorry i don't understand")
            pass
    print_pause("Thanks for playing :) ")


main()
