#this is a choose your own adventure game

def intro():
    print("Hello player! Please input your name.")
    name = input()
    print(f"Good to meet you, {name}!")
    print("\nLet's get started.")
    print("\nYou are a black long-haired cat named Rusty. You live a quiet, cushy life at your home with your family.")
    print("One day, your human goes to work and you notice the front door is left ajar.")
    print("\nDo you:\n  A. Stay put - outside is scary!\n  B. Wander over to inspect.")
    choose_door() #this is a test to see if i can do git

def choose_door():
    while True:
        answerdoor = input().lower()
        if answerdoor == "a":
            print("Smart choice, although, not a very interesting one. \nGame Over.")
            return  # End the game if they choose to stay inside
        elif answerdoor == "b":
            print("----------")
            print("You slowly creep over to the open door. You smell fresh air. You squeeze through the open door to find yourself outside.")
            choose_path()
            break  # Continue the game if they inspect
        else:
            print("Rusty doesn't understand! Please choose 'A' or 'B'.")

def choose_path():
    print("You advance forward and see you're in an apartment complex. There are lots of cars in the parking lot.")
    print("You continue walking until you reach the entrance, where you see a path that forks left and right.")
    print("Which direction should you take? \n  A. Left \n  B. Right")
    
    while True:
        answerpath = input().lower()
        if answerpath == "a":
            go_left()
            break
        elif answerpath == "b":
            go_right()
            break
        else:
            print("Rusty doesn't understand! Please choose 'A' or 'B'.")

def go_left():
    print("----------")
    print("You decide to go left. As you walk, you find a hidden alley with mysterious glowing graffiti. What could it mean?")
    print("You walk up to the graffiti and inspect it by sniffing. As your nose touches the wall, you hear a noise. The bricks have started to shift!")
    print("You jump back in shock, ears down. The bricks have shifted to reveal a secret doorway.")
    print("You smell cool, damp, air coming through the doorway. It's dark and you can't see a thing, no matter how much you strain your eyes.")
    print("What do you do?")
    print("Do you:\n  A. Advance through the door?\n  B. Keep walking down the alley?")
    
    while True:
        answer_doorway = input().lower()
        if answer_doorway == "a":
            print("----------")
            print("You gingerly step through the open door, feeling a rush of chilly air surround you.")
            print("As you step forward, you hear the bricks shift again, and you are startled to discover that they've closed you inside.")
            print("No turning back now.")
            # Continue the story here or add another function
            break
        elif answer_doorway == "b":
            print("----------")
            print("There's no WAY you're going through that door. You don't know what could be in there!")
            print("You decide to turn around and head the other way.")
            go_right()
            break
        else:
            print("Rusty doesn't understand! Please choose 'A' or 'B'.")

def go_right():
    print("----------")
    print("You decide to go right. As you explore, you see a big tree with strange markings. A big raven watches you from a branch.")
    print("\nAs you walk around the tree, inspecting the markings, you notice a tunnel under one of the tree's big roots.")
    print("\nYou're just about to step into the tunnel, when all of a sudden you're lifted by the scruff off the ground by sharp claws, accompanied by the sound of wings beating.")
    print("\nThe raven squawks at you, 'Nobody may enter! Pass the test, pass the test!', as he drops you back on the ground.")
    # Continue the story or add another function
    # You can add more choices here, similar to the left path
    pass  # Placeholder for further story development

def main():
    intro()

main()

