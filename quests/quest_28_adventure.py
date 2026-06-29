def start():
    print("You wake up in a forest. Two paths lie ahead.")
    print("Type 'left' or 'right' to choose your path.")
    choice = input("> ")

    if choice == "left":
        cave()
    elif choice == "right":
        river()
    else:
        print("Invalid choice. Game over.")

def cave():
    print("\nYou enter a dark cave and find a treasure chest.")
    print("Do you 'open' it or 'leave'?")
    choice = input("> ")

    if choice == "open":
        ending_good()
    elif choice == "leave":
        ending_bad()
    else:
        print("Invalid choice. Game over.")

def river():
    print("\nYou reach a river. A boat is tied to the bank.")
    print("Do you 'take' the boat or 'swim' across?")
    choice = input("> ")

    if choice == "take":
        ending_good()
    elif choice == "swim":
        ending_bad()
    else:
        print("Invalid choice. Game over.")

def ending_good():
    print("\nYou made a great choice and found your way home safely. YOU WIN!")

def ending_bad():
    print("\nThings didn't go your way. You are lost forever. GAME OVER.")

start()