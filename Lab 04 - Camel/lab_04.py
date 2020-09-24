import random

def main():

# Welcome
    print("Welcome to Camel!!")
    print()
    print("You have stolen an Ostrich!")
    print("Tarzan wants his ostrich back and is chasing you down!")
    print("Survive your desert trek and out run Tarzan.")

# Starting Variables
    miles_traveled = 0
    thirst = 0
    ostrichfatigue = 0
    canteen = 4
    oasis = random.randrange(20)
    natives_traveled = -15

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

        user_choice = input("What is your choice? ")

# Quit
        if user_choice.upper() == "Q":
            done = True
            print("You have left the game.")

# Drink from canteen
        if user_choice.upper() == "A":
            if canteen <= 0:
                print("Dust falls from your canteen. Seems you've run out of luck my friend.")
                thirst = 0
                print("You drink from your canteen.")
            else:
                print("You drink from your canteen.")
                canteen -= 1
                thirst = 0
                natives_traveled += random.randrange(3, 9)

# Moderate speed
        if user_choice.upper() == "B":
            moderate = random.randrange(5, 12)
            miles_traveled += moderate
            print("You run at a moderate speed and make a good about of distance.")
            print("You traveled",str(miles_traveled)+" miles.")

            thirst += 1
            ostrichfatigue += 1
            natives_traveled += random.randrange(3, 9)

# Full speed
        elif user_choice.upper() == "C":
            fast = random.randrange(18, 22)
            miles_traveled += fast

            if (fast <= 1):
                print("You tripped and hit your head! No distance was traveled.")

            else:
                print("You run full speed and run a great distance!")
                ostrichfatigue += 2
                natives_traveled += random.randrange(3, 9)
                thirst += 1

# Stop for the night
        if user_choice.upper() == "D":
            print("You have stopped for the night.")
            ostrichfatigue = 0
            natives_traveled += random.randrange(3, 9)
            thirst += 1

# Status check
        if user_choice.upper() == "E":
            print("You have traveled",str(miles_traveled)+" miles.")
            print("Your canteen has",str(canteen)+" drinks left.")
            print("Your ostrich is this tired:",str(ostrichfatigue)+".")
            print("Tarzan is",str(miles_traveled-natives_traveled)+" miles away from you.")

# Oasis
        if oasis == 20:
            print("You have found an oasis! Your canteen is now full and fatigue is at 0!")
            ostrichfatigue = 0
            thirst = 0
            canteen = 4

# Other
        if thirst == 1:
            print("You are becoming thirsty.")
        elif thirst == 2:
            print("You are really thirst.")
        elif thirst == 3:
            print("You are extremely dehydrated!")

        if natives_traveled >= miles_traveled:
            print("Tarzan has caught you!")
            done = True

        elif ostrichfatigue == 8:
            print("Tarzan has caught up to you. You are captured.")
            done = True

        elif thirst == 4:
            print("You are defeated by dehydration! Tarzan has caught you.")
            done = True

        elif miles_traveled >= 200:
            print("Your luck as seen you through this ordeal! You are now safe.")
            done = True


main()