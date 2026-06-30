# Quest 22: The Personalized Scroll
# A function with parameters, called with the user's answers.

def personalized_greeting(name, quest):
    print("Hello,", name + "!")
    print("Your quest is to", quest + ".")


name = input("What is your name? ")
quest = input("What is your quest? ")

personalized_greeting(name, quest)
