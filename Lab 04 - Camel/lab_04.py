import random

def main():

# Welcome
    print("Welcome to Camel!!")
    print()
    print("You have stolen an Ostrich!")
    print("Tarzan wants his ostrich back and is chasing you down!")
    print("Survive your desert trek and out run Tarzan.")

# Starting Variables
    milestraveled = 0
    thirst = 0
    ostrichfatigue = 0
    canteen = 4
    oasis = -1
    nativestraveled = -15
    native_up = random.randrange(0, 12)
    full_speed = random.randrange(10, 20)
    moderate_speed = random.randrange(5, 12)

# Game loop
    done = False

    while not done:
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        print()

# Players choice
        user_choice = input("What is your choice? ")

# Quit
        if user_choice.upper == "Q":
            done = True
        print("You have left the game.")

# Drink from canteen
        if user_choice == "A":
            if (0 <= canteen):
                canteen -= 1
                thirst = 0
                print("You drink from your canteen.")
            else:
                print("Dust falls from your canteen. Seems you've run out of luck my friend.")

# Moderate speed
        if user_choice == "B":
            miles = random.randrange(5, 12)
            milestraveled += miles
            thirst += 1
            ostrichfatigue += 1
            nativestraveled += random.randrange(3, 12)
            oasis =random.randrange()
            if oasis == -1:



main()