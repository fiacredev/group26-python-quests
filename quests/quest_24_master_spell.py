# Quest 24: The Master Spell
# Use the result from one function in another function.

def ask_for_age():
    age = int(input("How old are you? "))
    return age


def can_they_vote(age):
    if age >= 18:
        print("You are old enough to vote.")
    else:
        print("You are not old enough to vote yet.")


age = ask_for_age()
can_they_vote(age)
