import time
import sys

def slow_print(text, speed=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

achievements = [] 

slow_print('Remember you have only 1 chance')
slow_print("You are in the forest at night")
time.sleep(1)
slow_print("There is a strange old house")

choice = input("Do you wanna go inside? (yes/no): ")

if choice.lower() == "yes":
    slow_print("You made a correct decision")
    achievements.append("A brave one")
else:
    slow_print("You disappeared at the darkest night...")
    achievements.append("Instant death")
    sys.exit()              # ✅ GAME OVER

slow_print("\nThings to interact with:")
slow_print("A table,\nBookshelf,\nDark warehouse,\nA window")

print("\n1 - Interact with the door")
print("2 - Lock the door")
real_choice1 = input("Choose (1/2): ")

if real_choice1 == "2":
    slow_print("\nA safe guy ;)")
    achievements.append("A safe zone")
elif real_choice1 == "1":
    slow_print("\nYou died because of the cold coming from the door...")
    sys.exit()              # ✅ GAME OVER
else:
    slow_print("\nInvalid choice. The house eats you.")
    sys.exit()

slow_print("\nNow you can interact safely")

print("\n1 - Table")
print("2 - Bookshelf")
print("3 - Dark warehouse")
print("4 - Window")
real_choice2 = input("Interact with (1/2/3/4): ")

if real_choice2 == "1":
    slow_print("There is nothing here...")
elif real_choice2 == "4":
    slow_print("Locked...\nWrong choice.\nThe end.")
    sys.exit()
elif real_choice2 == "3":
    slow_print("You fell and died at the stairs!")
    achievements.append("Dead in a funny pose")
    sys.exit()
elif real_choice2 == "2":
    slow_print("There are only old books...")
    slow_print("You made a correct decision")
else:
    slow_print("You cannot hack the system!")
    sys.exit()

slow_print("\nYou found a teleportation device!")
answer_final = input("Do you want to press it (Y/N)?: ")

if answer_final.lower() == "y":
    slow_print("You made it!")
else:
    slow_print("You barely survived in this home without sleeping...")
    achievements.append("INSOMNIAC")
    sys.exit()

slow_print("\nTHE GAME HAS ENDED")
slow_print("Found achievements:\n")

for a in achievements:
    slow_print(a, 0.04)
