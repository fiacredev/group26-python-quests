#!/usr/bin/python3
# Quest 13: The Maze of Many Choices
# Grade a score from 0 to 100.

score = int(input("Enter your score (0-100): "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Needs Improvement")
