#!/usr/bin/python3
# Quest 15: The Nested Riddle
# Mini-adventure with nested choices.

direction = input("You reach a fork. Do you go 'left' or 'right'? ")

if direction == "left":
    action = input("A river blocks the path. Do you 'swim' or 'wait'? ")
    if action == "swim":
        print("You swim across and find a chest of glittering treasure!")
    else:
        print("You wait by the river until nightfall and find nothing.")
else:
    print("You go right and walk straight into a sleeping dragon. Run!")
