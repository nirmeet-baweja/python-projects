import time  # Imports a module to add a pause
from playsound import playsound
# Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

# Grabbing objects
sword = 0
flower = 0

required = ("\nUse only A, B, or C\n")  # Cutting down on duplication

# The story is broken into sections, starting with "intro"


def intro():
    print("You wake up to the sound of waves crashing on the shore. "
          "Your head is throbbing and you are a bit disoriented. "
          "You have no recollection of how you reached here.")

    print("As you lie there, memories start to come back and in flashes. "
          "\nYou can feel the warm sand under your feet. "
          "\nYou can see that there was a God from other world "
          "took your twin brother and left you here.")

    time.sleep(1)

    print("To your east is a small hilly town. "
          "To your west is the vast ocean.")

    playsound('ocean-wave.mp3')

    print("\nA. Jump into the ocean and try to swim to reach the other side."
          "\nB. Lie down and wait to regain your strength."
          "\nC. Run towards the town.")

    choice = input("\n>>> ")  # Here is your first choice.
    print(choice)
    if choice in answer_A:
        option_swim()
    elif choice in answer_B:
        print("\nWelp, that was quick. "
              "\n\nYou died!")
    elif choice in answer_C:
        option_run()
    else:
        print(required)
        intro()


def option_swim():
    print("\nThe ocean is vast. And as soon you jump into it, "
          "the waves turn violent. You thrash and try to swim but "
          "you are powerless in comparison to the strong waves. "
          "soon you lose consciousness and die!")
    time.sleep(1)
    print("\nA. Run"
          "\nB. Throw another rock"
          "\nC. Run towards a nearby cave")
    choice = input("\n>>> ")
    if choice in answer_A:
        option_run()
    elif choice in answer_B:
        print("\nYou decided to throw another rock, as if the first "
              "rock thrown did much damage. The rock flew well over the "
              "orcs head. You missed. \n\nYou died!")
    elif choice in answer_C:
        option_cave()
    else:
        print(required)
        option_rock()


def option_cave():
    print("\nYou were hesitant, since the cave was dark and "
          "ominous. Before you fully enter, you notice a shiny sword on "
          "the ground. Do you pick up a sword. Y/N?")
    choice = input("\n>>> ")
    if choice in yes:
        sword = 1  # adds a sword
    else:
        sword = 0
    print("\nWhat do you do next?")
    time.sleep(1)
    print("\nA. Hide in silence"
          "\nB. Fight"
          "\nC. Run")
    choice = input("\n>>> ")
    if choice in answer_A:
        print("\nReally? You're going to hide in the dark? I think "
              "orcs can see very well in the dark, right? Not sure, but "
              "I'm going with YES, so...\n\nYou died!")
    elif choice in answer_B:
        if sword > 0:
            print("\nYou laid in wait. The shimmering sword attracted "
                  "the orc, which thought you were no match. As he walked "
                  "closer and closer, your heart beat rapidly. As the orc "
                  "reached out to grab the sword, you pierced the blade into "
                  "its chest. \n\nYou survived!")
        else:  # If the user didn't grab the sword
            print("\nYou should have picked up that sword. You're "
                  "defenseless. \n\nYou died!")
    elif choice in answer_C:
        print("As the orc enters the dark cave, you sliently "
              "sneak out. You're several feet away, but the orc turns "
              "around and sees you running.")
        option_run()
    else:
        print(required)
        option_cave()


def option_run():
    print("\nYou run as quickly as possible, but the orc's "
          "speed is too great. You will:")
    time.sleep(1)
    print("\nA. Hide behind boulder"
          "\nB. Trapped, so you fight"
          "\nC. Run towards an abandoned town")
    choice = input("\n>>> ")
    if choice in answer_A:
        print("You're easily spotted. "
              "\n\nYou died!")
    elif choice in answer_B:
        print("\nYou're no match for an orc. "
              "\n\nYou died!")
    elif choice in answer_C:
        option_town()
    else:
        print(required)
        option_run()


def option_town():
    print("\nWhile frantically running, you notice a rusted "
          "sword lying in the mud. You quickly reach down and grab it, "
          "but miss. You try to calm your heavy breathing as you hide "
          "behind a delapitated building, waiting for the orc to come "
          "charging around the corner. You notice a purple flower "
          "near your foot. Do you pick it up? Y/N")
    choice = input("\n>>> ")
    if choice in yes:
        flower = 1  # adds a flower
    else:
        flower = 0
    print("You hear its heavy footsteps and ready yourself for "
          "the impending orc.")
    time.sleep(1)
    if flower > 0:
        print("\nYou quickly hold out the purple flower, somehow "
              "hoping it will stop the orc. It does! The orc was looking "
              "for love. "
              "\n\nThis got weird, but you survived!")
    else:  # If the user didn't grab the sword
        print("\nMaybe you should have picked up the flower. "
              "\n\nYou died!")


intro()
