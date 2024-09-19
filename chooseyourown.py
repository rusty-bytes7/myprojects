#this is a choose your own adventure game about Rusty the cat!

#import stuff
from time import sleep
import random


#start the game
def intro():
    print("Hello player! Please input your name.")
    name = input()
    print(f"Good to meet you, {name}!")
    print("\nLet's get started.")
    sleep(3)
    print("\nYou are a black long-haired cat named Rusty. \nYou have bright green eyes and cute, crinkly ears. \nYou live a quiet, cushy life at your home with your family.")
    print("One day, your human goes to work and you notice the front door is left ajar.")
    print("\nDo you:\n  A. Stay put - outside is scary!\n  B. Wander over to inspect.")
    choose_door()

#choose to go outside or stay inside- if you stay inside the game ends
#going outside takes you to the path
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

#player chooses a path direction
def choose_path():
    print("----------")
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

#player chose to go left- wall with strange graffiti
def go_left():
    print("----------")
    print("\nYou decide to go left. As you walk, you find a hidden alley with mysterious glowing graffiti. What could it mean?")
    print("\nYou walk up to the graffiti and inspect it by sniffing. As your nose touches the wall, you hear a noise. The bricks have started to shift!")
    print("\nYou jump back in shock, ears down. The bricks have shifted to reveal a secret doorway.")
    print("\nYou smell cool, damp, air coming through the doorway. It's dark and you can't see a thing, no matter how much you strain your eyes.")
    print("\nWhat do you do?")
    print("Do you:\n  A. Advance through the door?\n  B. Keep walking down the alley?")
    
    while True:
        answer_doorway = input().lower()
        #going through the doorway leads player to secret library
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
            library()
            # Continue the story here or add another function
            break
        
        #not going through the door leads player other way to tree
        elif answer_doorway == "b":
            print("----------")
            print("There's no WAY you're going through that door. You don't know what could be in there!")
            print("\nYou decide to turn around and head the other way.")
            go_right()
            break
        else:
            print("Rusty doesn't understand! Please choose 'A' or 'B'.")

#rusty finds himself in a cavernous library- happens after going through doorway of graffiti wall
def library():
    pass #add more story here

#player chooses go right or does not enter door in graffiti wall- weird tree with runes
def go_right():
#maybe make the printed text easier to read
    print("----------")
    print("You decide to go right. As you explore, you see a big tree with strange markings. A big raven watches you from a branch.")
    print("\nAs you walk around the tree, inspecting the markings, you notice a tunnel under one of the tree's big roots.")
    print("----------")
    print("\nYou're just about to step into the tunnel, when all of a sudden you're lifted by the scruff off the ground by sharp claws, accompanied by the sound of wings beating.")
    print("\nThe raven squawks at you, 'Nobody may enter! Pass the test, pass the test!', as he flies high into the air.")
    print("----------")
    print("\nThe raven flies you to a clearing in some nearby woods. You get dropped into the clearing, and the raven alights on a branch. The air feels thick, and you feel uneasy.")
    print("\nThe raven chirps 'Something hunts you, but not all dangers are real.'")
    print("\nThe clearing starts to grow dark. You see the outline of a large, menacing shape moving in the trees. The creature’s growl sends shivers down your spine. \nIt's bigger than any dog you've ever seen. It circles closer, but remains hidden in the shadows.")

    # Continue the story or add another function
    print("\nWhat do you do?")
    print("\nA. Stand your ground. \nB. Run.")

    while True:
        answermonster = input().lower()
        if answermonster == "a":
            standground()
            print("----------")
            #stands ground and gets led back to tree
            print("\nThe raven leads you back to the base of the tree with the strange runes. He allows you to enter the tunnel.")
            print("\n'Good luck brave one,' the raven squawks.")
            print("\nYou step into the tunnel. It's very dark, and it smells like fresh earth.")
            tunnel()
            break
        
        elif answermonster== "b":
        #player basically has to choose a to face the monster, otherwise will loop around
            runfrom_monster()
        else:
            print("Rusty doesn't understand! Please choose 'A' or 'B'.")

#standing ground in face of monster
def standground():
    print("----------")
    print("\nYou see the creature's glowing red eyes in the trees.")
    print("\nThe hair on your back stands up, but something tells you to stay put.")
    print("\nYou let out a hiss as the dark entity speeds directly at you- and then vanishes in a puff of smoke and hot air.")
    print("\nThe raven lands on the ground in front of you.")
    print("\n'*squawk* Very good, very brave!' he says.")
    print("\n'You passed the test!'")
    print ("\n \n")

#running from monster- will not go anywhere, player has to fight monster
def runfrom_monster():
    print("----------")
    print("\nPanic sets in, and you run as fast as you can. But no matter how quickly you move, the predator stays close.")
    print("\nEventually, you find yourself back where you started, exhausted and frightened.")
    print('\n"Running will not save you," the bird warns. "Try again. Face your fears."')
    print("----------")
    print("\nWhat do you do?")
    print("\nA. Stand your ground. \nB. Run.")

#rusty has passed the test of bravery and is allowed to enter the tunnel
def tunnel():
    print("----------")
    print("\nAs you begin your trek through the dark tunnel, you begin to see faint symbols on the walls.")
    print("\nYou realize the walls have the same faintly glowing runes as the tree.")
    print("\nThe light grows dimmer the farther you walk, and it begins to feel as though you've been pulled into another realm entirely.")
    print("\nSuddenly, the ground begins to shake. The floor underneath gives way, and to your surprise, you slide down into a hidden underground chamber.")
    print("----------")
    print("\nAs you shake off the dust from your fur, you take note and see the underground cavern is filled with glowing muchrooms and crystals that illuminate the room.")
    print("\nThere is a strange shimmering portal on the far wall.")
    print("\nYou try to go over and inspect, but suddenly, the shadows start to swirl and change shape.")
    print("\nYou realize you may have to fight your way to the portal.")
    
    #create monster to fight
    shadowmonster = weakmonster()
    shadowmonster.name = "Shadow Monster"
    print(shadowmonster.strength)

#create class of monsters
class weak_monster:
    name = ""
    strength = random.randint(1,10)


def main():
    intro()

main()

