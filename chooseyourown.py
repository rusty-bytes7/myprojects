#this is a choose your own adventure game about Rusty the cat!

#import stuff
from time import sleep
import random

#function for spacer
def spacer():
    print ("\n\n")
    print("----------")

#pause function to have player press enter to advance code
def pause():
    input("\n(Press Enter to continue.)")

#create player inventory
inventory = []

#start the game
def intro():
    print("Hello player! Please input your name.")
    name = input()
    print(f"Good to meet you, {name}!")
    print("\nLet's get started.")
    pause()
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
            spacer()
            print("Smart choice, although, not a very interesting one. \nGame Over.")
            print("\nTry again?")
            print("\nYes or No")
            playagain = input().lower()
            if playagain == "yes":
                intro()
            elif playagain == "no":
                print("Thanks for playing!")
                break
            return  # End the game if they choose to stay inside
        elif answerdoor == "b":
            spacer()
            print("You slowly creep over to the open door. You smell fresh air. You squeeze through the open door to find yourself outside.")
            choose_path()
            break  # Continue the game if they inspect
        else:
            print("Rusty doesn't understand! Please choose 'A' or 'B'.")

#player chooses a path direction
def choose_path():
    spacer()
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
    spacer()
    print("\nYou decide to go left. As you walk, you find a hidden alley with mysterious glowing graffiti. What could it mean?")
    print("\nYou walk up to the graffiti and inspect it by sniffing. As your nose touches the wall, you hear a noise. The bricks have started to shift!")
    pause()
    spacer()
    print("\nYou jump back in shock, ears down. The bricks have shifted to reveal a secret doorway.")
    print("\nYou smell cool, damp, air coming through the doorway. It's dark and you can't see a thing, no matter how much you strain your eyes.")
    print("\nWhat do you do?")
    print("Do you:\n  A. Advance through the door?\n  B. Keep walking down the alley?")
    
    while True:
        answer_doorway = input().lower()
        #going through the doorway leads player to secret library
        if answer_doorway == "a":
            spacer()
            print("You gingerly step through the open door, feeling a rush of chilly air surround you.")
            print("\nAs you step forward, you hear the bricks shift again, and you are startled to discover that they've closed you inside.")
            print("\nNo turning back now.")
            pause()
            spacer()
            print("You use your whiskers and your sense of smell to navigate down a pitch-black hallway. It's narrow, but you're able to fit.")
            print("\nYou start to wonder if you'll ever make it out of this strange tunnnel, when suddenly you see a faint light in the distance.")
            print("\nYou pick up the pace, and the light grows brighter and warmer before you.")
            pause()
            spacer()
            print("\nYou follow the light until you reach a cavernous room, and realize you're in a gigantic library.")
            library()
            break
        
        #not going through the door leads player other way to tree
        elif answer_doorway == "b":
            spacer()
            print("There's no WAY you're going through that door. You don't know what could be in there!")
            print("\nYou decide to turn around and head the other way.")
            go_right()
            break
        else:
            print("Rusty doesn't understand! Please choose 'A' or 'B'.")

#rusty finds himself in a cavernous library- happens after going through doorway of graffiti wall
def library():
    spacer()
    print("You step into the grand library, the air filled with the scent of old books and dust. Towering shelves stretch as far as you can see, their tops disappearing into shadow. They seem to go on forever- maybe they do.")
    print("\nA soft glow comes from scattered lanterns, casting flickering light onto the ornate floor tiles. The library is silent, but it feels like something is watching you.")
    print("\nBooks shift quietly on their shelves, as though alive, and faint whispers echo through the cavernous room. Somewhere deeper inside, a strange humming sound calls to you.")
    print("\nDo you explore further?")
    print(" \nA. Yes, I'm curious. \nB. No, I'm too scared.")
    while True:
        answer_explore = input().lower()
        if answer_explore == "a":
            spacer()
            print("\nYou cautiously step deeper into the library, your eyes narrowing as you make your way through the darkness.")
            print("\nThe humming sound grows louder, and you can't help but feel a sense of unease. The whispers grow louder as well as you wind your way through the tall shelves, into what seems to be the middle of the library.")
            print("\nYou come across a large, ancient tome that seems to be glowing faintly. You reach out to touch it, and as you do, the book opens on its own.")
            print("\n When you open the ancient book, its pages are blank at first. Suddenly, glowing runes appear, and a voice echoes: 'Traveler, this is the Book of Portals. Place your paw on a page, and it will guide you to the unknown.'")
        elif answer_explore == "b":
            spacer()
            print("\nInstead of exploring, you decide to go to the nearest bookshelf and flip through a book. You find a hidden compartment behind the book, and inside is a small, shiny object.")

#player chooses go right or does not enter door in graffiti wall- weird tree with runes
def go_right():
    # maybe make the printed text easier to read
    spacer()
    print("You go right and find a tree covered in strange markings. A large raven watches you from above.")
    print("\nAs you examine the markings, you spot a tunnel beneath the tree's roots.")
    spacer()
    pause()
    print("\nJust as you're about to enter, sharp claws lift you off the ground. The raven's wings beat furiously as it carries you into the air.")
    print("\n'Stop! Pass the test!' the raven screeches, flying higher.")
    spacer()
    pause()
    print("\nThe raven drops you into a clearing in the woods. It perches on a branch, watching.")
    print("\n'Something hunts you,' the raven chirps, 'but not all dangers are real.'")
    print("\nThe clearing grows dark. A large, shadowy creature moves in the trees, growling—a deep sound that chills you.")
    print("It's bigger than any dog you've seen, circling closer, still hidden in the shadows...")
    spacer()
    pause()

    # Continue the story or add another function
    print("\nWhat do you do?")
    print("\nA. Stand your ground. \nB. Run.")

    while True:
        answermonster = input().lower()
        if answermonster == "a":
            standground()
            spacer()
            # stands ground and gets led back to tree
            print("\nThe raven leads you back to the base of the tree with the strange runes. He allows you to enter the tunnel.")
            print("\n'Good luck, brave one,' the raven squawks.")
            print("\nYou step into the tunnel. It's very dark, and it smells like fresh earth.")
            pause()
            tunnel()
            break
        
        elif answermonster == "b":
            # player has to choose "A" to face the monster, otherwise will loop around
            runfrom_monster()
        else:
            print("Rusty doesn't understand! Please choose 'A' or 'B'.")

#standing ground in face of monster
def standground():
    spacer()
    print("\nYou spot glowing red eyes in the trees.")
    print("\nThe fur on your back rises, but something urges you to stay still.")
    print("\nYou hiss as the dark figure rushes toward you—then vanishes in a puff of smoke.")
    pause()
    print("\nThe raven lands before you.")
    print("\n'Very good, very brave!' it squawks.")
    print("\n'You passed the test!'")
    print("\nYou have passed the raven's test of bravery and it seems as though you will be permitted to enter the tunnel.")
    spacer()
    pause()

#running from monster- will not go anywhere, player has to fight monster
def runfrom_monster():
    spacer()
    print("\nPanic sets in, and you run as fast as you can. But no matter how quickly you move, the predator stays close.")
    print("\nEventually, you find yourself back where you started, exhausted and frightened.")
    print('\n"Running will not save you," the bird warns. "Try again. Face your fears."')
    spacer()
    pause()
    print("\nWhat do you do?")
    print("\nA. Stand your ground. \nB. Run.")


#rusty has passed the test of bravery and is allowed to enter the tunnel
def tunnel():
    spacer()
    print("\nAs you begin your trek through the dark tunnel, you begin to see faint symbols on the walls.")
    print("\nYou realize the walls have the same faintly glowing runes as the tree.")
    print("\nThe light grows dimmer the farther you walk, and it begins to feel as though you've been pulled into another realm entirely.")
    print("\nSuddenly, the ground begins to shake. The floor underneath gives way, and to your surprise, you slide down into a hidden underground chamber.")
    spacer()
    pause()
    print("\nAs you shake off the dust from your fur, you take note and see the underground cavern is filled with glowing mushrooms and crystals that illuminate the room.")
    print("\nThere is a strange shimmering portal on the far wall.")
    print("\nYou try to go over and inspect, but suddenly, the shadows start to swirl and change shape.")
    print("\nYou realize you may have to fight your way to the portal.")
    spacer()
    pause()
    print("\nTwo weapons magically appear before you. Which do you choose?")
    print("\nA. A sword that has a glowing blade. \nB. A whip that appears to move on its own.")
    while True:
        weaponchoice = input().lower()
        if weaponchoice == "a":
            fighthp = sword(rustyhp,hpbar)
            portal(fighthp)
            break
        elif weaponchoice == "b":
            fighthp = whip(rustyhp,hpbar)
            portal(fighthp)
            break
        else:
            print("Rusty doesn't understand! Please choose 'A' or 'B'.")
    
    #create monster to fight
        shadowmonster = weak_monster()
        
    

#create class of monsters
class weak_monster:
    name = ""
    strength = random.randint(1,10)
    attack = random.randint(1,10)
    defense = random.randint(1,10)

#introduces rusty's hp level when fighting monster
rustyhp = 25
hpbar = "*" * rustyhp

#Choose sword
def sword(rustyhp,hpbar):
    spacer()
    print("\nYou pick up the sword and examine it. It's a simple, yet powerful blade. You feel a rush as you realize you need to fight.")
    print("\n")
    #print rusty's hp and monster hp
    print("Rusty's HP: " + str(rustyhp) + " HP")
    print(hpbar)
    
    #prints monsterhp bar from randomly selected strength
    print("\nMonster HP: " + str(weak_monster.strength))
    mhpbar = "+" * weak_monster.strength
    print(mhpbar)
    print ("\n\n")

    
    while weak_monster.strength > 0:
        #ask player if they want to hit or defend
        print("Should Rusty A. Attempt an attack? or B. Defend?")
        attackordefend = input().lower()
        #player chooses to attempt an attack
        if attackordefend == "a":
            print("Rusty swings his sword at the shadow monster.")
            #select a random choice if sword hits or not
            hitlist = ["hit", "miss"]
            hit = random.choice(hitlist)
            #hit
            if hit == "hit":
                print("\nRusty hits the monster with his sword!")
                
                #rusty's sword does damage
                damage = random.randint(1,5)
                print(f"\nRusty deals {damage} damage to the shadow monster!")
                
                #monster's hp is reduced by damage
                weak_monster.strength -= damage
                if weak_monster.strength < 0:
                    weak_monster.strength = 0
                    break
                print("\nMonster HP: " + str(weak_monster.strength))
                print("Rusty's HP: " + str(rustyhp) + " HP")
                pause()
        
            elif hit == "miss":
                print("\nRusty misses the shadow monster with his sword!")
                #rusty takes damage
                rustydamage = random.randint(1,5)
                print(f"\nRusty takes {rustydamage} damage!")
                rustyhp -= rustydamage
                print(f"\nRusty's HP: {rustyhp}")
                print("\nMonster HP: " + str(weak_monster.strength))
                spacer()
                pause()
        #player chooses defend
        elif attackordefend == "b":
            #random choice when defending of the monster hitting or missing
            defense_list = ["m-hit", "m-miss"]
            defense = random.choice(defense_list)
            #monster hits
            if defense == "m-hit":
                print("\nThe monster used its attack!")
                #monster attacks and hit's rusty
                mattack = weak_monster.attack
                print(f"\nThe monster hits Rusty for {mattack} damage!")
                #rusty takes damage
                rustydamage = mattack
                rustyhp -= rustydamage
                #if damage is 0, fight ends
                if rustyhp < 0:
                    rustyhp = 0
                    continue
                print(f"\nRusty's HP: {rustyhp}")
                print("\nMonster HP: " + str(weak_monster.strength), " HP")
                spacer()
                pause()
            #monster misses
            elif defense == "m-miss":
                #rusty takes no damage
                print("\nThe monster lets our a fearsome roar.")
                print("\nRusty defends against the monster's attack!")
                print("\nMonster HP: " + str(weak_monster.strength), " HP")
                print("Rusty's HP: " + str(rustyhp) + " HP")
        else:
            print("Rusty doesn't understand! Please choose 'A' or 'B'.")

    #checks to see if the monster has been slain
    if weak_monster.strength <= 0:
        print("\nThe monster has been slain!")
        print(f"\nRusty has {rustyhp} HP left.")
    rustyfighthp = rustyhp
    return(rustyfighthp)
        
#chose whip
def whip(rustyhp, hpbar):
    spacer()
    print("\nYou pick up the whip and examine it. It appears to move on its own. You feel a rush as you realize you need to fight.")
    print("\n")
    #print rusty's hp and monster hp
    print("Rusty's HP: " + str(rustyhp) + " HP")
    print(hpbar)
    
    #prints monsterhp bar from randomly selected strength
    print("\nMonster HP: " + str(weak_monster.strength))
    mhpbar = "+" * weak_monster.strength
    print(mhpbar)
    print ("\n\n")

    
    while weak_monster.strength > 0:
        #select a random choice if sword hits or not
        hitlist = ["hit", "miss"]
        hit = random.choice(hitlist)
        print("Rusty cracks the whip at the shadow monster.")
        #hit
        if hit == "hit":
            print("\nRusty hits the monster with his whip!")

            #rusty's sword does damage
            damage = random.randint(1,5)
            print(f"\nRusty deals {damage} damage to the shadow monster!")

            #monster's hp is reduced by damage
            weak_monster.strength -= damage
            if weak_monster.strength < 0:
                weak_monster.strength = 0
                break
            print("\nMonster HP: " + str(weak_monster.strength))
            print("Rusty's HP: " + str(rustyhp) + " HP")
            pause()

        elif hit == "miss":
            print("\nRusty misses the shadow monster with his whip!")
            #rusty takes damage
            rustydamage = random.randint(1,5)
            print(f"\nRusty takes {rustydamage} damage!")
            rustyhp -= rustydamage
            print(f"\nRusty's HP: {rustyhp}")
            print("\nMonster HP: " + str(weak_monster.strength))
            spacer()
            pause()

    if weak_monster.strength <= 0:
        print("\nThe monster has been slain!")
        print(f"\nRusty has {rustyhp} HP left.")
    rustyfighthp = rustyhp
    return(rustyfighthp)
    

def portal(rustyfighthp):
    spacer()
    print(f"Rusty's remaining HP: {rustyfighthp} HP")
    pause()
    
    if rustyfighthp > 0:
        print("\nRusty steps through the portal, still recovering from the battle. The air hums with magic as he is transported to another realm.")
        
    else:
        print("\nRusty collapses before the portal, seemingly unable to continue.")
        print("\nJust as Rusty is about to lose consciousness, a figure appears before him.")
        print("\n'You have shown great courage,' the figure says. 'I will help you.'")
        print("\nRusty feels a warm light envelop him, and he feels a little bit of strength come to him.")
        rustyfighthp += 5
        print(f"\nRusty's HP: {rustyfighthp}")
        print("\nRusty stands up, feeling renewed.")
    spacer()
    pause()
    print("\nRusty finds himself in a lush forest, the air filled with the scent of flowers and the sound of birdsong.")
    print("\nHe sees a path ahead, and the sun is shining through the trees.")
    print("\nWhat do you do?")
    print("\nA. Follow the path. \nB. Explore the forest.")
    while True:
        pathchoice = input().lower()
        if pathchoice == "a":
            follow_path()
            break
        elif pathchoice == "b":
            explore_forest()
            break
        else:
            print("Rusty doesn't understand! Please choose 'A' or 'B'.")

def follow_path():

def explore_forest():


def amulet():
    spacer()
    print("You look closer to see that there is a small silver cat figurine on a chain inside the book's compartment. You feel compelled to take it with you.")
    print('As you put the chain around your neck, you feel a warm sensation flow through your body. You feel safer somehow.')
    print('Can you trust this amulet?')
    spacer()
    pause()
    amulet_choice()

def amulet_choice():
       spacer()
       print("Do you:")
       print("A. Trust the amulet and embrace its power?")
       print("B. Discard the amulet, fearing its unknown influence?")

       choice = input().lower()
       if choice == "a":
           # Path where the player trusts the amulet
           # ...
       elif choice == "b":
           # Path where the player discards the amulet
           # ...
       else:
           print("Invalid choice. Please select A or B.")
           amulet_choice()  # Re-prompt for input


#MAIN PROGRAM
def main():
    intro()

main()

