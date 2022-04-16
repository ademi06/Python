# You can use this workspace to write and submit your adventure game project.
import time
import random

enemy_creature = random.choice([
                "Pirate", "Troll", "Wizard", "fairie", "Agent",
                "Batman", "Alien", "Golem", "Giant"])
strong_weapon = "Sword"
weapon = []


def game_desc(message_player):
    # function to display game description to player
    print(message_player)
    time.sleep(2)


def gen_message():
    game_desc(
            "You find yourself standing in an open field,"
            "filled with grass and yellow wildflowers."
             )
    game_desc(
            f"Rumor has it that a wicked {enemy_creature} is somewhere "
            "around here, and has been terrifying the nearby village."
            )
    game_desc("In front of you is a house.")
    game_desc("To your right is a dark cave.")
    game_desc(
            "In your hand you hold your trusty"
            " (but not very effective) dagger.\n"
            )
    choice()


def choice():
    game_desc("Enter 1 to knock on the door of the house.")
    game_desc("Enter 2 to peer into the cave. ")
    game_desc("What would you like to do? ")
    choice_message()


def house():
    game_desc("You approach the door of the house.")
    game_desc(
            f"You are about to knock when the door"
            f" opens and out steps a {enemy_creature}."
            )
    game_desc(f"Eep! This is the {enemy_creature}'s house!")
    game_desc(f"The {enemy_creature} attacks you!\n")


def cave():
    game_desc("You peer cautiously into the cave.")
    game_desc("It turns out to be only a very small cave.")
    game_desc("Your eye catches a glint of metal behind a rock.")
    game_desc(f"You have found the magical {strong_weapon} of Ogoroth!")
    game_desc(
            "You discard your silly old dagger and take the "
            f"{strong_weapon} with you."
            )
    game_desc("You walk back out to the field.\n")


def valid_input(prompt, choice1, choice2):
    while True:
        response = input(prompt)
        if choice1 == response:
            house()
            fight()

        elif choice2 == response:
            cave()
            weapon.append("Sword")
            choice()
        else:
            return wrong_input()


def choice_message():
    while True:
        response = valid_input("(Please enter 1 or 2). \n ", "1", "2")


def wrong_input():
    response = valid_input("(Please enter 1 or 2)\n", "1", "2")
    if "1" or "2" not in response:
        print("(Please enter 1 or 2)")


def fight():
    while True:
        response = input("Would you like to (1) fight or (2) run away?\n")
        if response == "1":
            if "Sword" not in weapon:
                game_desc(
                        "You feel a bit under-prepared for this,"
                        " what with only having a tiny dagger.\n"
                        )
                defeat()
            else:
                win()
            play_again()
        elif response == "2":
            game_desc(
                    "You run back into the field. Luckily,"
                    " you don't seem to have been followed. \n"
                    )
            choice()


def play_again():
    while True:
        response = input("Would you like to play again? (y/n): ")
        if response == "y".lower():
            game_desc("Excellent! Restarting the game ... \n")
            start_game()
        elif response == "n".lower():
            game_desc("Thanks for playing! See you next time.")
            exit(0)


def defeat():
    if "sword" not in weapon:
        game_desc("You do your best...")
        game_desc("but your dagger is no match for the gorgon.")
        game_desc("You have been defeated!\n")
    else:
        win()


def win():
    game_desc(
            f"As the wicked {enemy_creature} moves to attack,"
            " you unsheath your new sword"
            )
    game_desc(
            "The Sword of Ogoroth shines brightly in your hand"
            " as you brace yourself for the attack."
            )
    game_desc(
            "But the wicked fairie takes one look at your"
            " shiny new toy and runs away!"
            )
    game_desc(
            "You have rid the town of the wicked fairie."
            " You are victorious!"
            )
    game_desc("GAME OVER")


def start_game():
    gen_message()
    fight()


start_game()
