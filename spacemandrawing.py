def drawSpaceMan(chancesLeft):
    if chancesLeft != 0:
        if chancesLeft < 7:
            print("   .")
            print("   _")
            print("  ___")
            print(" _____")
        if chancesLeft < 6:
            print("|  o  | Careful with your guesses")
        if chancesLeft < 5:
            print("| \|/ | Seriously")
        if chancesLeft < 4:
            print("|  |  | I'm not kidding!")
        if chancesLeft < 3:
            print("| / \ | Are you even trying?")
        if chancesLeft < 2:
            print(" _____  This is not funny!")
    else:
        print("   .")
        print("   _")
        print("  ___")
        print(" _____")
        print("|  o  |  AAaaahhhh")
        print("| \|/ |")
        print("|  |  |")
        print("| / \ |")
        print(" _____ ")
        print(" ^^^^^")
        print("/ \ / \ ")
        print("TAKEOFF!\n\n")
