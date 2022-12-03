import time
import random
import enemy_creature


def print_pause(message):
    print(message)
    time.sleep(1)


def intro(name):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + name + " is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) "
                "dagger.\n")


def replay(items):
    replay_question = input("Would you like to play again? (y/n)").lower()
    if replay_question == "n":
        print_pause("Thanks for playing! See you next time.")
        quit()
    elif replay_question == "y":
        items.clear()
        items.append("dagger")
        print_pause("Excellent! Restarting the game ...")
        play_game()
    else:
        print_pause("Type in y or n")
        replay(items)


def get_sword_in_the_cave(items):
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    print_pause("You discard your silly old dagger and take the sword"
                " with you.")
    print_pause("You walk back out to the field.\n")
    items.append("sword")
    items.remove("dagger")


def cave(items):
    print_pause("You peer cautiously into the cave.")
    if "sword" in items:
        print_pause("You've been here before, and gotten all the "
                    "good stuff. It's just an empty cave now.")
    else:
        get_sword_in_the_cave(items)


def fight_with_sword(name, items):
    response1 = input("Would you like to (1) fight or (2) run away?")
    if response1 == "1":
        print_pause("As the " + name + " moves to attack, "
                    "you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand "
                    "as you brace yourself for the attack.")
        print_pause("But the " + name + " takes one look at your "
                    "shiny new toy and runs away!")
        print_pause("You have rid the town of the " + name + ". You are"
                    " victorious!")
        replay(items)
    elif response1 == "2":
        print_pause("You run back into the field. Luckily, "
                    "you don't seem to have been followed.\n")
        field()
        choose_house_or_field(items, name)
    else:
        print_pause("Type 1 or 2")
        fight_with_sword(name, items)


def fight_without_sword(name, items):
    response1 = input("Would you like to (1) fight or (2) run away?")
    if response1 == "1":
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the " + name + ".")
        print_pause("You have been defeated!")
        replay(items)
    elif response1 == "2":
        print_pause("You run back into the field. Luckily, "
                    "you don't seem to have been followed.\n")
        field()
        choose_house_or_field(items, name)
    else:
        print_pause("Type 1 or 2")
        fight_without_sword(name, items)


def attack_from_enemy_creature(name):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens "
                "and out steps a " + name + ".")
    print_pause("Eep! This is the " + name+"\'s house!")
    print_pause("The " + name + " attacks you!")


def house(items, name):
    attack_from_enemy_creature(name)
    if "sword" in items:
        fight_with_sword(name, items)
    else:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")
        fight_without_sword(name, items)


def field():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")


def choose_house_or_field(items, name):
    response = input("(Please enter 1 or 2.)\n")
    if response == "1":
        house(items, name)
    elif response == "2":
        cave(items)
        field()
        choose_house_or_field(items, name)
    else:
        choose_house_or_field(items, name)


def play_game():
    name = random.choice(enemy_creature.words)
    items = ["dagger"]
    intro(name)
    field()
    choose_house_or_field(items, name)


play_game()
