# Coding Challenge 4
# Name:
# Student No:

# A Text Adventure Game

import time  # Imports a module to add a pause

# Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

# global state variables
asked_turles = False
asked_octopus = False

# to check if the user's response is a valid answer
required = ("\nUse only A, B, or C\n")
required_ab = ("\nUse only A, or B\n")


# The story is broken into sections, starting with "intro"


def intro():
    print("\n\nOn a sandy, luxurious beach a pirate in his huge ship landed "
          "on the shore. He was frantically running around looking "
          "for something while counting his steps. In his hand he held "
          "a long, golden scroll. ")

    print("\nHe dropped to his knees at ‘x marks the spot’ and appeared very "
          "sad for some reason! His treasure had been discovered and taken "
          "by someone or something…")

    print("\nThe pirate looked closely at where his treasure would have been, "
          "the sand was wet and squelchy. He thought for a while and believed "
          "that the sea had swept his treasure away, how would he ever be able "
          "to search deep in the blue sea? All of a sudden, the pirate jumped "
          "up to his feet as he had an idea.")

    print("\nYears ago while on his pirate travels he came across an "
          "abandoned yellow submarine! After an almighty struggle, "
          "he managed to get the submarine in his pirate ship and "
          "it’s been left there till this day.")

    print("\nAlso on one of his pirate missions he had acquired an ATV. "
          "Which was still lying on the deck. What should the pirate do now:\n")

    time.sleep(1)

    print("""  A. Grab the ATV and venture further into the island to look for the treasure.
  B. Take the submarine deep into the ocean in search of the treasure.
  C. Give up""")

    choice = input(">>> ")  # Here is your first choice.

    # check if the user's response is a valid answer
    if choice in answer_A:
        option_atv()
    elif choice in answer_B:
        option_submarine()
    elif choice in answer_C:
        print("You gave up! Game over")
    else:  # call the same function again
        print(required)
        intro()


def option_atv():
    print("\nSo the pirate quickly returned to his ship and restarted the "
          "red ATV with the special key he found inside. Soon he was on "
          "his way deep into the island. While travelling he crossed path "
          "with his enemy pirates and got killed in the ambush.")

    print("\nGame Over! You lost!")


def option_submarine():
    print("\nSo the pirate quickly returned to his ship and restarted the "
          "yellow submarine with the special key he found inside. The blades "
          "started to spin and the submarine slowly sank into the deep blue "
          "ocean. The pirate had lived on the sea all his life but had never "
          "seen what laid beneath. He was amazed as he looked through the "
          "porthole, he could see thousands of different colours, seaweed "
          "dancing and a range of sea creatures rushing around him.")

    print("\nSoon the pirate saw a school of sharks, a bale of turtles, "
          "and a solitary octopus. What should the pirate do now:\n")

    time.sleep(1)

    print("""  A. Approach the school of sharks.
  B. Approach the bale of turtles.
  C. Approach the octopus.""")

    choice = input(">>> ")

    # check if the user's response is a valid answer
    if choice in answer_A:
        option_sharks()
    elif choice in answer_B:
        option_turtles()
    elif choice in answer_C:
        option_octopus()
    else:  # call the same function again
        print(required)
        option_submarine()


def option_turtles():
    global asked_turles

    if not asked_turles:
        asked_turles = True
        print("\nHe swam to the turtles, they were very arrogant and said him "
              "not to bother them. They said that he should have asked the "
              "sharks for their help instead.")

        print("\nWhat should the pirate do now:\n")

        time.sleep(1)

        print("""  A. Trust the arrogant turtles and approach the dangerous school of sharks.
  B. Approach the solitary octopus.""")

        choice = input(">>> ")

        # check if the user's response is a valid answer
        if choice in answer_A:
            option_sharks()
        elif choice in answer_B:
            option_octopus()
        else:
            print(required_ab)
            asked_turles = False
            option_turtles()
    else:  # call the same function again
        print("\nHe swam again towards the turtles. This the turtles were "
              "angry for he did not listen to them the first time. And now "
              "the school of sharks is long gone. The pirate lost his chance "
              "at retrieving his treasure because of his bad decisions.")

        print("\nGame Over! You Lost!")


def option_octopus():
    global asked_octopus

    if not asked_octopus:
        asked_octopus = True
        print("\nHe swam to the octopus. But old grumpy octopus did not pay "
              "any heed to the pirate and just ignored him.")

        print("\nNow there are only two options left for the pirate:\n")

        time.sleep(1)

        print("""  A. Approach the school of sharks.
  B. Approach the bale of turtles.""")

        choice = input(">>> ")

        # check if the user's response is a valid answer
        if choice in answer_A:
            option_sharks()
        elif choice in answer_B:
            option_turtles()
        else:
            print(required_ab)
            asked_octopus = False
            option_octopus()
    else:  # call the same function again
        print("\nHe swam again towards the octopus. The turtles had "
              "suggested the pirate to ask the sharks. But he did not trust "
              "the turtles. The octopus wouldn't even listen to the pirate. "
              "And continued to ignore him. Meanwhile the school of sharks is "
              "long gone. The pirate lost his chance at retrieving his "
              "treasure because of his lack of trust.")

        print("\nGame Over! You Lost!")


def option_sharks():
    print("\nHe quickly put on his diving essentials and swam out to the "
          "sharks. He approached the sharks cautiously but soon realised "
          "they were very friendly when they gave him a big welcome. The "
          "sharks asked what brought him to visit under the sea, so he "
          "explained what happened to his treasure. The sharks told him "
          "that he should look for his treasure at the bottom of the ocean. "
          "As he started to swim towards the ocean bed, he suddenly saw a "
          "sparkle deep at the bottom of the ocean.")

    print("\nWhat should the pirate do now:\n")

    time.sleep(1)

    print("""  A. Go near the source of sparkle.
  B. Use the crossbow and hook to grab the shiny substance.""")

    choice = input(">>> ")

    # check if the user's response is a valid answer
    if choice in answer_A:
        option_go_near()
    elif choice in answer_B:
        option_grab()
    else:  # call the same function again
        print(required_ab)
        option_sharks()


def option_grab():
    print("\nThe pirate aimed his crossbow directly at the shiny thing "
          "and fired the hooked rope at it. It struck its mark. When he "
          "tried to drag it up to him. He found that it was the most "
          "stunning, beautiful and shiny fish the pirate had ever seen. "
          "And his hook from the crossbow had killed him. He felt awfully "
          "guilty for killing an innocent creature. And it was the last "
          "lead the pirate had. So, he has nothing more to carry on.")

    print("\nGame Over! You Lost!")


def option_go_near():
    print("\nHe darted like lightening down to the bottom to see if it was "
          "his treasure. But unfortunately when he reached the bottom he "
          "found the most stunning, beautiful and shiny fish the pirate had "
          "ever seen. The pirate asked, “Well if you happen to know anything "
          "about my missing treasure from the beach, I would be very "
          "grateful’. Rainbow Fish replied, \"The Whale of the ocean must "
          "have gobbled up your treasure.\" The pirate got straight back "
          "into his submarine and followed the calls of the whales. He popped "
          "up out of the sea in his submarine when he appeared to be near "
          "the pod of whales.")

    print("\nWhat should he do next:\n")

    time.sleep(1)

    print("""  A. Request humbly to the humongous whale if it would be generous to return his treasure.
  B. Get ready to blow up the whale with the missile in your submarine and retrieve your treasure like a real pirate you are.""")

    choice = input(">>> ")

    # check if the user's response is a valid answer
    if choice in answer_A:
        option_request()
    elif choice in answer_B:
        option_missile()
    else:  # call the same function again
        print(required_ab)
        option_go_near()


def option_request():
    print("\nWhales are generous creatures. And since, the pirate was polite "
          "to them and asked nicely. The whale decided to return him his "
          "long lost treasure, for the whale did not know that it belonged "
          "to him. Seeing the good nature of the whale, the pirate decided "
          "to share his treasure with the whale. And everyone was happy.")

    print("\nGame Over! You Won!")


def option_missile():
    print("\nPirate's submarine and its missiles are no match for the massive "
          "whale. The whale became angry by the attack and with one swing "
          "of its fin it broke the submarine and and sent the pirate flying "
          "into the sky.")

    print("\nGame Over! You Lost!")


intro()

# Sources : The storyline has been adapted from -
# https://www.westwood.leeds.sch.uk/the-lost-treasure-adventure-story/
