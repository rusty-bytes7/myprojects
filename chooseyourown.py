#this is a choose your own adventure game
from time import sleep

def intro():
    print("Hello player! Please input your name.")
    name = input()
    print(f"Good to meet you, {name}!")
    print("\nLet's get started.")
    sleep(3)
    print("\nYou are a black long-haired cat named Rusty. You live a quiet, cushy life at your home with your family.")
    print("One day, your human goes to work and you notice the front door is left ajar.")
    print("\nDo you:\n  A. Stay put - outside is scary!\n  B. Wander over to inspect.")
    choose_door() #this is a test to see if i can do git

def choose_door():
    while True:
        answerdoor = input().lower()
        if answerdoor == "a":
            print("----------")
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
            print("\nAs you step forward, you hear the bricks shift again, and you are startled to discover that they've closed you inside.")
            print("\nNo turning back now.")
            sleep(3)
            print("----------")
            print("You use your whiskers and your sense of smell to navigate down a pitch-black hallway. It's narrow, but you're able to fit.")
            print("\nYou start to wonder if you'll ever make it out of this strange tunnnel, when suddenly you see a faint light in the distance.")
            print("\nYou pick up the pace, and the light grows brighter and warmer before you.")
            print("\nYou follow the light until you reach a cavernous room, and realize you're in a gigantic library.")
            # Continue the story here or add another function
            break
        elif answer_doorway == "b":
            print("----------")
            print("There's no WAY you're going through that door. You don't know what could be in there!")
            print("\nYou decide to turn around and head the other way.")
            go_right()
            break
        else:
            print("Rusty doesn't understand! Please choose 'A' or 'B'.")

def go_right():
    print("----------")
    print("You decide to go right. As you explore, you see a big tree with strange markings. A big raven watches you from a branch.")
    print("\nAs you walk around the tree, inspecting the markings, you notice a tunnel under one of the tree's big roots.")
    sleep(3)
    print("\nYou're just about to step into the tunnel, when all of a sudden you're lifted by the scruff off the ground by sharp claws, accompanied by the sound of wings beating.")
    print("\nThe raven squawks at you, 'Nobody may enter! Pass the test, pass the test!', as he flies high into the air.")
    sleep(4)
    print("\nYou are lifted high above the city- the raven flies you to a clearing in some nearby woods. You get dropped into the clearning, and the raven alights on a branch. The air feels thick, and you feel uneasy.")
    print("\nThe raven chirps 'Something hunts you, but not all dangers are real.'")
    print("\nThe clearing starts to grow dark. You see the outline of a large, menacing shape moving in the trees. The creature’s growl sends shivers down your spine. It's bigger than any dog you've ever seen. It circles closer, but remains hidden in the shadows.")

    # Continue the story or add another function
    # You can add more choices here, similar to the left path
    pass  # Placeholder for further story development


def main():
    intro()

main()

