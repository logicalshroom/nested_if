# Objective 2

# Task 1: Code Correction

#I commented out the bad code.

# attendees = input("Enter number of attendees: ")
# venue = "large hall" if attendees > 100 else "conference room"
# print(venue)

attendees = input("Enter number of attendees: ")
attendees = int(attendees)
venue = "large hall" if attendees > 100 else "conference room"
print(venue)