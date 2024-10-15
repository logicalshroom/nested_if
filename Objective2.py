# Objective 2

# Task 1: Code Correction

#I commented out the bad code.

# attendees = input("Enter number of attendees: ")
# venue = "large hall" if attendees > 100 else "conference room"
# print(venue)

# Running the code as is gives us a TypeError.

print("Begin Task 1.")

attendees = input("Enter number of attendees: ")
attendees = int(attendees) #we need to add a line that converts the data type
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# Task 2: Venue Selection

# Based on the corrected code from Task 1, further enhance your code to recommend additional things like "audio system" or "projector" based on the number of attendees.

print("Begin Task 2.")

attendees = input("Enter number of attendees: ")
attendees = int(attendees)
venue = "large hall" if attendees > 100 else "conference room"
add_on = "projector" if attendees > 150 else "audio system" #The program will now recommend a projector if there are over 150 atendees, and an audio system if there are fewer.

print(venue)
print(add_on)

# Task 3: Ask user if they are vegetarian. If they are, recommend the appropriate vegetarian caterer.

print("Begin Task 3.")

veg_opt = input("Do you prefer meat-less catering? (yes/no) ")
caterer = "Veggie Delight Caterers" if veg_opt == "yes" else "Gourmet Meals Caterers"

print(caterer)