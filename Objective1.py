# Objective 1

# Task 1

# Code Correction, I've commented out the bad code

# place = input("Choose a place: forest or cave? ")
# 
# if place = "forest":
#     action = input("climb a tree or cross a river?")
#     if action = "climb a tree":
#         print("You found a bird's nest!")
#     else action = "cross a river":
#         print("You found a boat!")
# elif place = "cave":
#     print("You find a hidden treasure!")

print("Begin Task 1.")

place = input("Choose a place: forest or cave? ")

# All the logical operators need to be fixed, so I'll do that first. 

if place == "forest":
    action = input("Choose an action: climb a tree, or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river": #Big Syntax Error fixed
        print("You found a boat!")
if place == "cave": #This needs to be another if statement
    print("You find a hidden treasure!")


# Task 2

# Add a game path through the cave where if you light a torch or proceed in the 

print("Begin Task 2.")

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("Choose an action: climb a tree, or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
if place == "cave":
    action = input("Choose an action: light a torch, or proceed in the dark?")
    if action == "light a torch":
        print("You found an empty cave!")
    elif action == "proceed in the dark":
        print("You trip on a stalagmite and fall down.")

# Task 3

# Add in pass keywords to proceed if the user fails to input correctly

# All we have to do for this is add a pass statement for each if loop

print("Begin Task 3.")

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("Choose an action: climb a tree, or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
if place == "cave":
    action = input("Choose an action: light a torch, or proceed in the dark?")
    if action == "light a torch":
        print("You found an empty cave!")
    elif action == "proceed in the dark":
        print("You trip on a stalagmite and fall down.")
    else:
        pass