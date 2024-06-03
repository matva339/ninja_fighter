# Created by Theo
# Co-written by Maddy Farmer

#   # Of Total Current Endings == 39    38 endings plus ending 0
createdEndingsNumber = 39
anyEndingAchived = False
allEndingsAchived = False # WIP WIP WIP

breaking = False

endStates = [False for i in range (createdEndingsNumber)] # List full of False or True values. Keeps track of which endings a player has gotten by changing the state
                                                          # from False to True when a player unlocks a new ending


#List of items/knowledge you can obtain through specific endings. Once you unlock one, you can take it with you on subsequent playthroughs.
hasTeleportDevice = False
hasKey = False
hasWizardPhoneNumber = False
hasGrappleMastersPhoneNumber = False
hasGrappleMastersGrapplingHook = False
hasRolex = False
hasStructureMap = False
hasRemote = False

hasAnyItem = False

#Floor variables for structure elevator
floor4 = False
floor3 = False
floor2 = False
floor1 = False
Basement1 = False
Cave = False

outtaJail = False
undetected = True

failiures = 0

def returnMenu():
    print("")
    print("Return to menu?")
    print("------------------------------")
    print("1. Yes")
    print("2. No")
    print("------------------------------")
    YNans = input()
    if YNans == "1":
        print("Returning to menu...")
        print("")
    elif YNans == "2":
        print("Goodbye. We hope you'll visit France again soon.")
        yesBreak = True
        return yesBreak
    
def fail():
    print("------------------------------")
    print("Ending 0 of x - You got a Failiure ending...")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
    print("------------------------------")
    endStates[0] = True




while True:
    breaking = False
    floor4 = False
    floor3 = False
    floor2 = False
    floor1 = False
    Basement1 = False
    Cave = False
    firstTimeInBasement = False
    outtaJail = False
    undetected = True
    # Setting variables that may be used later to false to make sure the code works as intended
    for i in endStates:
        if i == True:
            anyEndingAchived = True
    # Checking to see if the player has gotten any endings so that the game knows wether or not to show the option to see the list of achived endings
    print("")
    print("")
    print("")
    print("                                          Welcome to GAMENAMEPLACEHOLDER. VERS. WIP29                            ")
    print("                                      This game follows the story of Matthew.                                    ")
    print("You'll be given number options to make choices. Please make your selection from the list of options given to you.")
        print("                                      When you're ready to begin, hit 'ENTER'.                                   ")
    input()
    print("")
    print("")
    print("")
    print("There once was a man named Matthew. He lived within the Eiffel Tower. One day, something very strange happened.")
    print("------------------------------")
    print("1. Investigate")
    if anyEndingAchived == True:
        print("2. See list of achieved endings")
    if hasAnyItem == True:
        print("3. Bring an item")
    if allEndingsAchived == True:
        print("4. Do nothing about it.")
    print("------------------------------")
    ans = input()
    if ans == "1": # Investigate path
        print("Matthew crawled out of his sleeping place to find that the people below were holding a community chili testing")
        print("picnic in the park nearby. He could make out the shapes of chili pots, some people, and a large pond.")
        print("------------------------------")
        print("1. Go to the chili")
        print("2. Go engage in normal human conversation")
        print("3. Leap off of the tower into the pond")
        print("4. Go and test every chili down there at once")
        print("------------------------------")
        ans1 = input()
        if ans1 == "1": # Go to the chili path (3 endings)
            print("Matthew felt compeled. He felt that he had to go to the chili. He climbd down his tower abode and slowly made")
            print("his way to the park... There it was. There Matthew saw the most beautiful thing his beady little eyes had ever")
            print("looked upon. There, was Le Or Chile.")
            print("------------------------------")
            print("1. Jump in the pot")
            print("2. Use one of the serving spoons like a normal person")
            print("3. Inspect the chili closer")
            print("------------------------------")
            ans1_1 = input()
            if ans1_1 == "1":
                print("Matthew was unable to resist, this may be his only oppurtunity. He looked upon the large pot before him, big")
                print("enough to fit a wheelbarrow. He steped a few paces backwards, as a few people turned to look at what he was doing.")
                print("He got a running start, and he leaped! He yelled out into the sky, 'WHAHOOIE!!!!' The people slowly watched him in")
                print("immense surprise, and terror, as he landed into the chili. The chili was flung everywhere by the splash, those near where he jumped")
                print("were blinded, some with irreversable damage, most of the families who had come to take part in the chili tasting were")
                print("traumatized, and several people were on the phone with the authorities. But none of that mattered to Matthew. Because, for a")
                print("brief, fleeting moment in time, Matthew got to live his dream.")
                print("------------------------------")
                print("Ending 1 of x - You got the Very Hot Tub ending!") #ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                print("------------------------------")
                endStates[1] = True
                breaking = returnMenu()
                if breaking == True:
                    break
            elif ans1_1 == "2":
                print("Matthew held himself back. As much as he wanted to jump in that pot, he decided he would use the serving spoons that were supplied")
                print("as to not pull too much attention to himself. Matthew was a vigilante after all.")
                print("He grabbed a plastic spoon with his right hand, and clasped it in his fist. He shakily lowered the spoon into the chili, and brought")
                print("it back up to take a bite. Matthew spoke. 'Huh. This chili is pretty bland-' *BWOOOOM!* Matthew then exploded into glitter.")
                print("------------------------------")
                print("Ending 5 of x - You got the Oh, That Chili Was Trapped ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                print("------------------------------")
                endStates[5] = True
                breaking = returnMenu()
                if breaking == True:
                    break
            elif ans1_1 == "3":
                print("Matthew decided to more closely inspect the chili. As he grazed his eyes overtop the shimmering surface, he saw a fly swoop down and land")
                print("on the chili. Matthew was disgusted. He grabbed the pot of chili, looked at the fly, and he said, 'You are an abomination.' Matthew then")
                print("screamed with rage as he threw the pot of chili with all of his strength, straight into the sun.")
                print("------------------------------")
                print("Ending 10 of x - You got the Fly Fly Away ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                print("------------------------------")
                endStates[10] = True
                breaking = returnMenu()
                if breaking == True:
                    break
        elif ans1 == "2": # Engage in human conversation path
            print("Matthew thought that he would take this oppurtunity to engage in social activity. He hardly ever got out anymore, so he saw this as")
            print("a perfect chance. Matthew climbed out of his fun little home, and entered the park. He looked around and saw three potential persons")
            print("to talk to. There was a small boy with a interesting looking box, a large muscular man, and a normal looking guy.")
            print("------------------------------")
            print("1. Talk to the boy")
            print("2. Talk to the muscular man")
            print("3. Talk to the guy")
            print("------------------------------")
            ans1_2 = input()
            if ans1_2 == "1": # Talk to the Boy path
                print("Matthew walked up to the small boy. 'Hi there little boy, what do you have there?' He asked. The boy responded, in the deepest voice Matthew")
                print("had ever heard, 'Right here I have a self-sustaining ecosystem of foreign metal-eating beetles. If you don't surrender and come with us, I will")
                print("release them from this box and they will destroy your home, the Eiffel Tower. Afterwards they will wreck complete havoc on the entirety of")
                print("France. If you do agree to come along with us, we'll spare the Eiffel Tower, and France will go on peacefully.' Matthew couldn't belive what he")
                print("was hearing. This was terrible. Be he had a feeling he knew who was behind this... 'So, what are you going to choose Matthew? I'll give")
                print("you ten seconds to pick.' Matthew couldn't believe he had fallen for one of their feindish tricks again. He looked around")
                print("the chili tasting event, and watched every person there reveal a tattoo of a fish. He knew these people, they meant buisiness. But he also")
                print("knew their management was never far away. If he could figure a way out of this, maybe he could take down the organization for good.")
                print("His thoughts were interrupted. 'Tick tock Matthew! What'll it be?'")
                print("------------------------------")
                print("1. Surrender")
                print("2. Bide for time")
                print("------------------------------")
                ans1_2_1 = input()
                if ans1_2_1 == "1": # Surrender path
                    print("Matthew bent down on his knees and held his wrists out towards the boy. He stared at him with strong emotions behind his eyes. 'Ah, good choice.' The boy grabbed a")
                    print("strange pair of handcuffs and placed them on Matthews wrists. 'You are hereby under arrest for crimes against our organization. You will spend time in our prison")
                    print("until management feel that you've learned your place.' The boy pulled out what looked like a normal TV remote. He bent down and whispered, 'See you around Matthew.' He")
                    print("pushed a button on the remote, and Matthew began to feel tingly and odd. Before he could figure out what was going on, everything around him was fuzzy, and he was")
                    print("vanishing from the park, appearing in some strange new room. He was sligthly nauseous from whatever just happened to him, and he took a moment to get his bearings. Once")
                    print("he felt better, he looked around, and saw that he was in a solid walled-in room with nothing but an empty bucket, a dirty sink, and a speaker built in to the wall.")
                    print("On the floor in front of him there was a scrap of paper. He picked it up and looked at it. It was covered it strange scrawled writing. Matthew began to read")
                    print("the note off to himself. 'ThE WaLLs ArE ThIn. BrEAk ThEm. 2093088372619-28' Weird.")
                    print("------------------------------")
                    print("1. 'Well, I'll break the walls I guess'")
                    print("2. Drink some water")
                    print("3. Just enjoy your time here")
                    print("------------------------------")
                    ans1_2_1_1 = input()
                    if ans1_2_1_1 == "1": # Break the walls path
                        while True: # outtaJail while loop
                            print("Matthew decided that he would do what the note said, and he would break the walls. Despite his handcuffs, he picked up the bucket from the ground, and he")
                            print("swung it at one of the walls. To his surprise, the wall didn't just break, it fell over flat like a cardboard cut-out. On the other side of the flat wall what seemed")
                            print("to be a large, empty, abandoned library. The room was eerily dark, and it was totally empty besides a couple of chairs that were randomly placed, one of which was knocked over.")
                            print("'Where the heck am I?' Matthew wondered to himself aloud. His words reverberated off the walls. He began to walk around. He saw a large double door on the")
                            print("opposite end of the room, and there was an exit sign above it. Suddenly, Matthew heard a sound behind him, and turned to see an elevator door with a lit-up arrow")
                            print("above it pointing down, signifying that an elevator was on it's way. It was slowly getting audibly closer.")
                            print("------------------------------")
                            print("1. Wait at the elevator")
                            print("2. Hide")
                            print("3. Run")
                            print("------------------------------")
                            ans1_2_1_1_1 = input()
                            if ans1_2_1_1_1 == "1": # Wait at elevator for Jim path
                                undetected = False # Regesters wether or not the "Recceed into my imagination" option pops up in outtaJail section
                                print("'Ah,' Matthew thought, 'how perfect. I'll just wait for the elevator and ride it out of this place.' Matthew walked up to the closed elevator doors, and a few secods")
                                print("later, they opened, revealing a shadowed figure. As he moved into the light, Matthew could make out what looked like an employee from a retail store. He had a pair of")
                                print("jeans held up by a simple leather belt, and he wore a simple under-shirt with a small name badge pinned to it. The badge read 'Jim J. Jimmothy'.")
                                print("------------------------------")
                                print("1. 'Hey, do you know where we are? This place is freaking creepy.'")
                                print("2. 'Excuse me, may I use the elevator?'")
                                print("3. 'Get outta my way! I'm elevating here!'")
                                print("4. Quick! Lie to him! Lie to the stranger!")
                                print("------------------------------")
                                ans1_2_1_1_1_1 = input()
                                if ans1_2_1_1_1_1 == "1": # Jim fail #1
                                    print("'We are in the F.R.O.G. headquarters.' Matthew was startled by this revalation. He didn't expect to be sent to the head base of the Forces Retaining Order Greatly. He'd had many run ins")
                                    print("with F.R.O.G. before, but he'd never been to their headquarters. Who knew what he would find here. Jim J. Jimothy spoke again. 'Speaking of which, aren't you supposed to be trapped?' The")
                                    print("man then pulled out some sort of high-tech taser and rendered Matthew unconcious.")
                                    fail()
                                    breaking = returnMenu()
                                    if breaking == True:
                                        break
                                    elif breaking == False:
                                        break
                                elif ans1_2_1_1_1_1 == "2": # Jim fail #2 (UNFINISHED)
                                    print("")
                                elif ans1_2_1_1_1_1 == "3": # Jim fail #3 (UNFINISHED)
                                    print("'Get outta my way! I'm elevating here!' Matthew yelled at Jim because he wanted him to move out of the way. Jim reacted with a very serious expression. 'I am the one who is")
                                    print("elevating here.' Then Jim pulled out a slingshot and shot Matthew in the face at point-blank range.")
                                elif ans1_2_1_1_1_1 == "4": # Lie to Jim path
                                    print("Before speaking, Matthew turned his back quickly and used his high-quality disguise kit! No one could see through his facade! Matthew fasened his moustache as he turned around.")
                                    print("'Hello! My name is Rod Annette Ficher! You know those tabs on the top of all soda cans? Yeah, well my job is to install those soda tabs on soda cans before they're sold.")
                                    print("Every soda you've ever seen, I put the tab on it. My hobbies include knitting, collecting rubber ducks, and taxidermy-ing possums. If you'd like to know more, just look")
                                    print("at my buisiness card!' Matthew held out a buisiness card with the name 'Rod Annette Ficher' written on it in crayon. On the back it said 'phone number not included' The man took the card")
                                    print("out of Matthew's hand, and stared at him intensely. The man cracked his knuckles, inhaled strongly, then spoke. 'Mr. Rod Ficher! How did you end up down here? There was supposed")
                                    print("to be a dangerous violator of the space-time continuum locked in a cell in this room, but the perimiter alarm went off! Has he escaped?' 'O-Oh, oh yes he has!' Matthew")
                                    print("said with a hint of fear in his voice. 'That scary horrible man knocked me over and made me show him which way to run!' 'That's so horrible! What a jerk! I'll make him pay,")
                                    print("I won't let him get away with this!' Jimmothy sprinted towards and through the double doors on his way to find Matthew. Meanwhile, Matthew thought. 'Well, that sure was an")
                                    print("odd man. I wonder if those double doors lead to an exit. That would explain why he went that way.'")
                                    outtaJail = True
                                    break

                            elif ans1_2_1_1_1 == "2": # Hide after braking walls path
                                print("Matthew looked around frantically for a place to hide. In the room there was a very expensive looking sofa, a scrappy barstool, and an ottoman. He didn't see any other options.")
                                print("------------------------------")
                                print("1. Hide behind the fancy sofa")
                                print("2. Hide on the barstool")
                                print("3. Hide inside the ottoman")
                                print("------------------------------")
                                ans1_2_1_1_1_2 = input()
                                if ans1_2_1_1_1_2 == "1": # Hide behind sofa path
                                    print("Matthew quickly leaped behind the sofa in a stunning athletic feat. Matthew laid himself against the sofa, and then he heard the sound of the elevator doors")
                                    print("sliding open. He also heard the sound of footsteps echoing throughout the room. '*Tap, Tap, Tap*.' Matthew stayed as quiet as he could. He eventually heard the")
                                    print("footsteps fade away. It was quiet again.")
                                    print("------------------------------")
                                    print("1. Get out")
                                    print("2. Stay hidden")
                                    print("------------------------------")
                                    ans1_2_1_1_1_2_1 = input()
                                    if ans1_2_1_1_1_2_1 == "1": # Get out too soon (1st time) path
                                        print("Matthew stood up from behind the soda, and as he looked around, he realized that the man who must've been stepping around was still right in the middle of the room.")
                                        print("'Ha!' the man yelled. 'The old fading footstep trick! I learned that little tip from a good buddy in high school.' Before Matthew could respond, the man pulled out")
                                        print("a slingshot from his pocket, and hit Matthew square in the face, rendering him unconcious.")
                                        print("------------------------------")
                                        print("Ending 32 of x - You got the Fading Footsteps Trick ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                                        print("------------------------------")
                                        breaking = returnMenu()
                                        if breaking == True:
                                            break
                                        elif breaking == False:
                                            break
                                    elif ans1_2_1_1_1_2_1 == "2": # Stay hidden (1st time) path
                                        print("Matthew decided to stay where he was. He didn't want anyone trying the old fake fading footstep trick on him. After about a minute had passed, he heard a sigh")
                                        print("come from somewhere near him in the room. He heard a voice mumble, '2, 0... 4... then a... 8.' Matthew heard a beeping noise. Then the voice said, much louder,")
                                        print("'The prisoner has escaped his room, I'm going to search the nearby halls. Keep me posted.' This time the footsteps sounded genuine.")
                                        print("------------------------------")
                                        print("1. Get out")
                                        print("2. Stay hidden")
                                        print("------------------------------")
                                        ans1_2_1_1_1_2_1_2 = input()
                                        if ans1_2_1_1_1_2_1_2 == "1": # Get out too soon (2nd time) path
                                            print("Matthew stood up from behind the soda, and as he looked around, he realized that the man who must've been stepping around was STILL right in the middle of the room.")
                                            print("'Ha!' the man yelled. 'The old fading footstep trick! I learned that little tip from a good buddy in high school.' Before Matthew could respond, the man pulled out")
                                            print("a slingshot from his pocket, and hit Matthew square in the face, rendering him unconcious.")
                                            print("------------------------------")
                                            print("Ending 33 of x - You got the Ha, Fading Footsteps Trick Again! ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                                            print("------------------------------")
                                            breaking = returnMenu()
                                            if breaking == True:
                                                break
                                            elif breaking == False:
                                                break
                                        elif ans1_2_1_1_1_2_1_2 == "2": # Stay hidden (2nd time) path
                                            print("Even though the footsteps sounded genuine, Matthew had a sneaking suspicion that they were fake. He waited for another minute before he heard the footsteps walk")
                                            print("out of the room again. He waited, but didn't hear anything more.")
                                            print("------------------------------")
                                            print("1. Get out")
                                            print("2. Stay hidden")
                                            print("------------------------------")
                                            ans1_2_1_1_1_2_1_2_2 = input()
                                            if ans1_2_1_1_1_2_1_2_2 == "1": # Get out the correct time path
                                                print("Matthew got out from his hiding place. He was sure that no one would be in the room anymore. As he stood up, he saw that the room was empty, and he was safe, for at")
                                                print("least a moment. He sat on the sofa for a moment and thought. He could go through the double doors and get to what he assumed was the escape, or he could try to ride on")
                                                print("the elevator and make his way to their boss. He wasn't sure where either path would lead him, but he was sure that no matter what, it would be interesting.")
                                                undetected = True # Regesters wether or not the "recceed into my imagination" should appear
                                                outtaJail = True
                                                break
                                                
                                            elif ans1_2_1_1_1_2_1_2_2 == "2": # Hide forever path
                                                print("Matthew woould not be decieved! He would not be tricked! He would never leave this spot until he was one-hundred percent certain that there wasn't somebody out there")
                                                print("trying to fake him out. Matthew laid there for minutes. Hours. Had days gone by? Matthew wasn't sure anymore, but that didn't matter to him. He had to stay hidden, he")
                                                print("could not under any circumstance get out from behind this couch. He was sure he would be ready to leave soon. Matthew waited. And he waited. He continued to wait. The end")
                                                print("was getting closer now. Now even closer. Here it comes.")
                                                print("------------------------------")
                                                print("Ending 15 of x - You got the Wait ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                                                print("------------------------------") 
                                                endStates[15] = True
                                                breaking = returnMenu()
                                                if breaking == True:
                                                    break
                                                elif breaking == False:
                                                    break
                                            
                                            
                                elif ans1_2_1_1_1_2 == "2": # Barstool ending path
                                    print("Matthew sat down on the barstool. As the elevator doors opened, Matthew saw a very plainly dressed man. 'Howdy there son,' said Matthew in a sudden, southern")
                                    print("drawl, 'what's yer name?' As he said this, he noticed a small 'Hello my name is...' sticker on the mans shirt. It said 'Jim.' The man responded, 'My name")
                                    print("is Jim.' Matthew nodded. 'I'm sorry about this.' Then, before Matthew could react, he pulled out a slingshot and shot Matthew right in the face.")
                                    print("------------------------------")
                                    print("Ending 14 of x - You got the Quick, Quick, Draw! ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                                    print("------------------------------") 
                                    endStates[14] = True
                                    breaking = returnMenu()
                                    if breaking == True:
                                        break
                                    elif breaking == False:
                                        break
                                elif ans1_2_1_1_1_2 == "3": # Ottoman path
                                    print("Matthew hastily folded himself inside the ottoman. He barely fit, but it was good enough for now. Matthew heard the sound of elevator arriviing, and the doors opening.")
                                    print("He heard an odd voice say 'Nothing here... what are my... I'm on my way...' It was hard to hear inside of the ottoman, so Matthew could only catch parts of what the")
                                    print("voice said. After the voice finished speaking, he heard the sound of footsteps moving towards the elevator, and the sound of the elevator leaving again.")
                                    print("------------------------------")
                                    print("1. Get out")
                                    print("2. ")
                                    print("3. ")
                                    print("------------------------------")

                                    # MORE HERE
                                    
                            elif ans1_2_1_1_1 == "3": # Escape ending path
                                print("Matthew didn't want to see what they'd do to him for breaking the thin wall, so he decided to try and get out quickly. He sprinted away from the elevator, towards")
                                print("the exit door. He pushed through the door, and just as he got to the other side, he heard the elevator stop. He kept running down a long empty hallway until he got")
                                print("to a staircase, which he took down. He assumed it would be the general direction to escape from. As he reached the bottom, he was dumbfounded to find that he was almost")
                                print("out. Right in front of him was a door to outside. Matthew ran through the door, and escaped onto a very foggy, and rocky seashore. He looked behind him and saw the threatening")
                                print("structure of the building looming over him. He didn't know where he was, or how he was going to get home back to the Eiffel Tower. Matthew decided that he would")
                                print("figure it out when he got to it. Right now, he just needed to get away from here. He'd get them someday though. Oh, he'd show them who's in charge. Matthew walked away")
                                print("into the fog.")
                                print("------------------------------")
                                print("Ending 11 of x - You got the Escaped ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                                print("------------------------------")  
                                endStates[11] = True
                                breaking = returnMenu()
                                break
                        
                        if breaking == True:
                            print("BREAKING TRUE")
                            break
                        elif breaking == False:
                            print("BREAKING FALSE")
                            pass

                        if outtaJail == True: # Either hid successfully or tricked Jim path
                            print("------------------------------")
                            print("1. Take the elevator")
                            print("2. Go through the double doors")
                            if undetected == True:
                                print("3. Recede into my imagination")
                            print("------------------------------")
                            ans1_2_1_1_1_2_1_2_2_1 = input()
                            if ans1_2_1_1_1_2_1_2_2_1 == "1": # Elevator path
                                print("Matthew would take the elevator. He was sick of these people getting involved in his life, and he was going to see to it that they wouldn't do so any longer. Matthew pushed the button")
                                print("on the wall to call the elevator. Once it arrived Matthew stepped inside and looked around. The elevator was very normal looking for the most part, with handlebars on the sides and a")
                                print("panel with buttons by the door. The buttons read from top to bottom:")
                                print("FL 4")
                                print("FL 3")
                                print("FL 2")
                                print("FL 1")
                                print("B 1")
                                print("C")
                                print("There was also a note taped on the panel. It read 'Elevator malfunctioning, only FL 4, FL 1, B 1, and C buttons work. Sorry for inconvinience.'")
                                print("Matthew couldn't tell which floor he was currently on. If only he had some sort of map which outlined the floors and what was on them...")
                                if hasStructureMap == True: # Show the descriptions of the floors in the structure if you have the map
                                    print("Oh yeah, he did! The map of the structure labeled what was on each floor. It read as follows:")
                                    print("FL 6 - description placeholder")
                                    print("FL 5 - description placeholder")
                                    print("FL 4 - description placeholder")
                                    print("FL 3 - description placeholder")
                                    print("FL 2 - description placeholder")
                                    print("FL 1 - description placeholder")
                                    print("B 1 - description placeholder")
                                    print("C - description placeholder")
                                else:
                                    print("Well, he didn't, so for now he would have to make due with guessing floors at random.")
                                while True:
                                    print("------------------------------")
                                    print("1. Press the button labeled 'FL 4'")
                                    print("2. Press the button labeled 'FL 3'")
                                    print("3. Press the button labeled 'FL 2'")
                                    print("4. Press the button labeled 'FL 1'")
                                    print("5. Press the button labeled 'B 1'")
                                    print("6. Press the button labeled 'C'")
                                    print("------------------------------")
                                    ans1_2_1_1_1_2_1_2_2_1_1 = input()
                                    if ans1_2_1_1_1_2_1_2_2_1_1 == "1":
                                        floor4 = True
                                        break
                                    if ans1_2_1_1_1_2_1_2_2_1_1 == "2":
                                        print("Matthew pushed the button labeled FL 3. Nothing happened.")
                                        print("")
                                        continue
                                    if ans1_2_1_1_1_2_1_2_2_1_1 == "3":
                                        print("Matthew pushed the button labeled FL 2. Nothing happened.")
                                        print("")
                                        continue
                                    if ans1_2_1_1_1_2_1_2_2_1_1 == "4": # Push FL 1 the 1st time path
                                        print("Matthew pushed the button labeled FL 1. The elevator doors closed, and smooth elevator jazz began to play, but almost immediately the doors opened, and")
                                        print("Matthew could see that he was on the same floor as before. 'Well, that must mean that this is floor 1.' Matthew thoguht to himself. 'I guess it was lucky")
                                        print("of me to choose this floor first in case I need to get back here.'")
                                        print("------------------------------")
                                        print("1. Press the button labeled 'FL 4'")
                                        print("2. Press the button labeled 'FL 3'")
                                        print("3. Press the button labeled 'FL 2'")
                                        print("4. Press the button labeled 'FL 1'")
                                        print("5. Press the button labeled 'B 1'")
                                        print("6. Press the button labeled 'C'")
                                        print("------------------------------")
                                        ans1_2_1_1_1_2_1_2_2_1_1_4 = input()
                                        if ans1_2_1_1_1_2_1_2_2_1_1_4 == "1":
                                            floor4 = True
                                            break
                                        if ans1_2_1_1_1_2_1_2_2_1_1_4 == "2":
                                            print("Matthew pushed the button labeled FL 3. Nothing happened.")
                                            print("")
                                            continue
                                        if ans1_2_1_1_1_2_1_2_2_1_1_4 == "3":
                                            print("Matthew pushed the button labeled FL 2. Nothing happened.")
                                            print("")
                                            continue
                                        if ans1_2_1_1_1_2_1_2_2_1_1_4 == "4": # Push FL 1 the 2nd time path
                                            print("Matthew pushed the FL 1 button again. He was excited the first time, and wanted to see if anything changed the second time. The elevator revved, the music began, and")
                                            print("it just as quickly shut off, as the doors opened to reveal the expected, that everything was the same. Matthew simply stood there.")
                                            print("------------------------------")
                                            print("1. Press the button labeled 'FL 4'")
                                            print("2. Press the button labeled 'FL 3'")
                                            print("3. Press the button labeled 'FL 2'")
                                            print("4. Press the button labeled 'FL 1'")
                                            print("5. Press the button labeled 'B 1'")
                                            print("6. Press the button labeled 'C'")
                                            print("------------------------------")
                                            ans1_2_1_1_1_2_1_2_2_1_1_4_4 = input()
                                            if ans1_2_1_1_1_2_1_2_2_1_1_4_4 == "1":
                                                floor4 = True
                                                break
                                            if ans1_2_1_1_1_2_1_2_2_1_1_4_4 == "2":
                                                print("Matthew pushed the button labeled FL 3. Nothing happened.")
                                                print("")
                                                continue
                                            if ans1_2_1_1_1_2_1_2_2_1_1_4_4 == "3":
                                                print("Matthew pushed the button labeled FL 2. Nothing happened.")
                                                print("")
                                                continue
                                            if ans1_2_1_1_1_2_1_2_2_1_1_4_4 == "4": # Push FL 1 the 3rd time path
                                                print("Matthew was unsatisfied. He must push the FL 1 button again. He had to. There was no two ways about it. ect ect")
                                                    #Finish this ending sometime
                                            if ans1_2_1_1_1_2_1_2_2_1_1_4_4 == "5":
                                                Basement1 = True
                                                break
                                            if ans1_2_1_1_1_2_1_2_2_1_1_4_4 == "6":
                                                Cave = True
                                                break

                                        if ans1_2_1_1_1_2_1_2_2_1_1_4 == "5":
                                            Basement1 = True
                                            break
                                        if ans1_2_1_1_1_2_1_2_2_1_1_4 == "6":
                                            Cave = True
                                            break
                                    if ans1_2_1_1_1_2_1_2_2_1_1 == "5":
                                        Basement1 = True
                                        break
                                    if ans1_2_1_1_1_2_1_2_2_1_1 == "6":
                                        Cave = True
                                        break
                                    else:
                                        break

                                    

                                

                                
                                
                                if floor4 == True: # FL 4 path
                                    
                                    print("Matthew pushed the button labeled FL 4. The elevator doors closed and smooth elevator jazz began to play. Matthew stood in the elevator for what felt like a while,")
                                    print("until eventually the elevator stopped and the doors opened. Matthew looked out throught the open doors and saw a small waiting room, or some kind of lounge. In the room")
                                    print("there were a few chairs lined up on one wall, as well as some potted plants. On the wall opposite to the chairs there was a powered off TV. Underneath the TV was a small")
                                    print("shelf with a TV remote on it, some board games, and some magazines. Lastly, on the wall across from the elevator was a pair of doors. One door was unlabeled, and the other")
                                    print("had a small sign next to it which said 'Elevator 2 this way.'")
                                    while True:
                                        print("------------------------------")
                                        print("1. Enter the labeled door")
                                        print("2. Enter the unlabeled door")
                                        print("3. Investigate the shelf")
                                        print("4. Sit on a chair and wait")
                                        print("------------------------------")
                                        fl4ans1 = input()
                                        if fl4ans1 == "1":
                                            print("Matthew decided to enter the door which apparently led to another elevator. Opening the door, he found a short carpeted hallway with a door to the left, another")
                                            print("door ahead and to the right, and a door at the end. There was also a decoritive plant and some art on the walls.")
                                            print("------------------------------")
                                            print("1. Try the left door")
                                            print("2. Try the right door")
                                            print("3. Try the door at the end of the hall")
                                            print("------------------------------")
                                            fl4ans1_1 = input()
                                            if fl4ans1_1 == "1":
                                                print("Matthew turned to the door on his left and turned the handle. The door opened, and Matthew stepped inside, quickly shutting the door in case anyone walked by.")
                                                print("Inside, Matthew found what was seemingly a dimly lit computer lab. There were long desks with lines of alcoves for different setups, and a moniter at each one. The")
                                                print("dim lighting that was filling the room was coming from the moniters, which were each a different color. There were tens of moniters in here, and none of them looked")
                                                print("particularly different from the others. There was also a closet door in one corner, and more houseplants strewn throughout the room. As Matthew finished looking around,")
                                                print("he noticed a lockbox sitting on one of the desks.")
                                                print("------------------------------")
                                                print("1. Look closer at the moniters")
                                                print("2. Check the closet")
                                                print("3. Investigate the lockbox")
                                                print("------------------------------")
                                                fl4ans1_1_1 = input()
                                                if fl4ans1_1_1 == "1":
                                                    print()
                                                if fl4ans1_1_1 == "2":
                                                    print()
                                                if fl4ans1_1_1 == "3":
                                                    print()

                                            if fl4ans1_1 == "2":
                                                print()
                                            if fl4ans1_1 == "3":
                                                print()
                                        if fl4ans1 == "2":
                                            print()
                                        if fl4ans1 == "3":
                                            if hasRemote == False:
                                                print("Matthew looked at the things on the small shelf closer. Among the magazines there was a copy of Exotic Frogs magazine, the newest issue of Paris Times, and a limited edition")
                                                print("issue of Imposter magazine. Matthew turned his attention to the TV remote. Upon further inspection, the remote didn't look like it controlled a TV at all. The buttons had odd, foreign")
                                                print("symbols which Matthew had never seen before. Matthew tried pushing one of the buttons, but he realized there were no batteries inside. The biggest surprise was the shape of the battery")
                                                print("compartment. It looked like it required a trangular battery of some kind. Matthew decided to keep the remote for now.")
                                                print("------------------------------")
                                                print("You obtained Remote!")
                                                print("------------------------------")
                                                hasRemote = True
                                                continue
                                            elif hasRemote == True:
                                                print("Matthew looked at the things on the small shelf closer. Among the magazines there was a copy of Exotic Frogs magazine, the newest issue of Paris Times, and a limited edition")
                                                print("issue of Imposter magazine. There was nothing else of intrest on the shelf.")
                                                continue
                                        if fl4ans1 == "4":
                                            print()
                                        else:
                                            break
                                

                                if Basement1 == True: # Basement (Maze) path
                                    firstTimeInBasement = True
                                    while True:
                                        if firstTimeInBasement == True:
                                            print("Matthew pushed the button labeled B 1. The elevator doors closed and smooth elevator jazz began to play. Matthew stood around for a moment while the elevator")
                                            print("moved, but it didn't take too long for the doors to open again. As the doors opened, Matthew looked out of the elevator and immediately noticed that he was in")
                                            print("an odd place. The room outside the elevator was dimly lit with ominus blue light. Directly in front of Matthew there was a single opening leading down a long")
                                            print("hallway with a few offshoots. Matthew stepped out of the elevator and saw a small sign on the wall next to the hallway. It read as follows:")
                                            print("'Cursed labrynth, please ignore. We're working on hiring a guy to fix it. Don't go in.'")
                                            print("Matthew liked the sound of that, so he decided to not take the sign's advice and he stepped forward into the entrance of the labrynth. In front of Matthew")
                                            print("there was a long hallway leading to a dead end, a path to the right, and a path forward and to the left.")
                                        elif firstTimeInBasement == False:
                                            print("Matthew appeared in the elevator room at the beginning of the labrynth. The original path laid before him.")
                                        print("------------------------------")
                                        print("1. Go right")
                                        print("2. Go left")
                                        print("3. Go forward")
                                        if firstTimeInBasement == False:
                                            print("4. Give up and cry")
                                        print("------------------------------")
                                        lab1 = input()
                                        firstTimeInBasement = False
                                        if lab1 == "1": # Correct labrynth path
                                            print("")
                                        if lab1 == "2": # Go left (all dead ends) path ALL PATHS DONE
                                            print("Matthew walked forward and took a left. As he turned the corner and looked down the next hall, he saw a left turn close to him, a right turn a short distance")
                                            print("away, and a left turn at the very end of the hall.")
                                            print("------------------------------")
                                            print("1. First Left")
                                            print("2. Go Right")
                                            print("3. Second Left")
                                            print("------------------------------")
                                            lab1_2 = input()
                                            if lab1_2 == "1": # Reset labrynth
                                                print("Matthew stepped forward and turned left. Down the next hallway there was a left turn very close to him, and a right turn at the end of the hall very far away.")
                                                print("------------------------------")
                                                print("1. First Left")
                                                print("2. End Right")
                                                print("------------------------------")
                                                lab1_2_1 = input()
                                                if lab1_2_1 == "1": # Reset labrynth
                                                    print("Matthew took the path immediately to his left. As he turned the corner, he was met with a wall directly in front of his face.")
                                                if lab1_2_1 == "2": # Reset labrynth
                                                    print("Matthew walked down the long hallway and turned to the right. Down the next hall, there was a left turn a few paces ahead of him, and a left and right turn")
                                                    print("at the end of the hall.")
                                                    print("------------------------------")
                                                    print("1. First Left")
                                                    print("2. End Left")
                                                    print("3. End Right")
                                                    print("------------------------------")
                                                    lab1_2_1_2 = input()
                                                    if lab1_2_1_2 == "1": # Reset labrynth
                                                        print("Matthew walked a short distance forward an turned to the left. There was a very short hall with another left turn at the end in front of him.")
                                                        print("------------------------------")
                                                        print("1. Go Left")
                                                        print("------------------------------")
                                                        lab1_2_1_2_1 = input()
                                                        if lab1_2_1_2_1 == "1": # Reset labrynth
                                                            print("Matthew took the left turn, and in front of him he saw an extremely long hallway. There was a left turn just before the end, and one at the end.")
                                                            print("------------------------------")
                                                            print("1. First Left")
                                                            print("2. End Left")
                                                            print("------------------------------")
                                                            lab1_2_1_2_1_1 = input()
                                                            if lab1_2_1_2_1_1 == "1": # Reset labrynth
                                                                print("Matthew walked down the long hallway towards the first left turn. His footsteps echoed off of the smooth stone walls. He wondered what lay at the end")
                                                                print("of this odd labrynth. As he thought, he reached his destination. He turned around the corner to the left, and in front of his was another rather long hallway,")
                                                                print("this time with a single left turn at the very end.")
                                                                print("------------------------------")
                                                                print("1. Go Left")
                                                                print("------------------------------")
                                                                lab1_2_1_2_1_1_1 = input()
                                                                if lab1_2_1_2_1_1_1 == "1": # Reset labrynth
                                                                    print("Matthew walked down the hall. Maybe this labrynth didn't have any end at all. It was supposedly cursed after all. Matthew hoped that there was a hot tub at the end. That would")
                                                                    print("be a nice surprise. As Matthew fantasized about the hot tub of his dreams, he reached the end of the hall. He turned the corner, anticipating greatness, his dreams were crushed, as")
                                                                    print("he saw a dead end in front of him. That's too bad.")
                                                            if lab1_2_1_2_1_1 == "2": # Reset labrynth
                                                                print("Matthew walked down the long hallway. His footsteps echoed off of the smooth stone walls. He wondered what lay at the end of this strange labrynth.")
                                                                print("Maybe it didn't have and end. It was supposedly cursed, after all. Matthew finally reached the end of the hall, and turned to his left. In front")
                                                                print("of him, there was a short hall, follwed by a left turn at the end.")
                                                                print("------------------------------")
                                                                print("1. Go Left")
                                                                print("------------------------------")
                                                                lab1_2_1_2_1_1_2 = input()
                                                                if lab1_2_1_2_1_1_2 == "1": # Reset labrynth
                                                                    print("Matthew again stepped forward and turned to his left. In front of him was another short path with a left turn at the end.")
                                                                    print("------------------------------")
                                                                    print("1. Go Left")
                                                                    print("------------------------------")
                                                                    lab1_2_1_2_1_1_2_1 = input()
                                                                    if lab1_2_1_2_1_1_2_1 == "1": # Reset labrynth
                                                                        print("Matthew stepped forward and took the left turn in front of him. He was yet again met with a short hallway with a left turn at the end.")
                                                                        print("------------------------------")
                                                                        print("1. Go Left")
                                                                        print("------------------------------")
                                                                        lab1_2_1_2_1_1_2_1_1 = input()
                                                                        if lab1_2_1_2_1_1_2_1_1 == "1": # Reset labrynth
                                                                            print("Matthew walked down the hallway and turned left again. This time, instead of a hallway with only one turn, he found a hallway with no turns.")
                                                    if lab1_2_1_2 == "2": # Reset labrynth
                                                        print("Matthew walked to the end of the hall and turned to the left. In front of him there was a short hallway with only a turn to the left at the end.")
                                                        print("------------------------------")
                                                        print("1. Go Left")
                                                        print("------------------------------")
                                                        lab1_2_1_2_2 = input()
                                                        if lab1_2_1_2_2 == "1": # Reset labrynth
                                                            print("Matthew walked forward and turned left. As he rounded the corner, he found a dead end.")
                                                    if lab1_2_1_2 == "3": # Reset labrynth
                                                        print("Matthew walked down the hall and took the right at the end. In front of him, there was a short hall with another right turn at the end.")
                                                        print("------------------------------")
                                                        print("1. Go Right")
                                                        print("------------------------------")
                                                        lab1_2_1_2_3 = input()
                                                        if lab1_2_1_2_3 == "1": # Reset labrynth
                                                            print("Matthew stepped forward and turned right. In front of him, there was another short hall, this time with a left turn at the end.")
                                                            print("------------------------------")
                                                            print("1. Go Left")
                                                            print("------------------------------")
                                                            lab1_2_1_2_3_1 = input()
                                                            if lab1_2_1_2_3_1 == "1": # Reset labrynth
                                                                print("Matthew stepped forward again, and turned to the left. He was met with a relatively longer hallway with another single right turn at the end.")
                                                                print("------------------------------")
                                                                print("1. Go Right")
                                                                print("------------------------------")
                                                                lab1_2_1_2_3_1_1 = input()
                                                                if lab1_2_1_2_3_1_1 == "1": # Reset labrynth
                                                                    print("Matthew walked down the hallway. He wondered why there were so few options this way. Maybe he was almost to the end! Matthew excitedly ran forward and turned the corner,")
                                                                    print("finding yet another short hallway with one right turn at the end.")
                                                                    print("------------------------------")
                                                                    print("1. Go Right")
                                                                    print("------------------------------")
                                                                    lab1_2_1_2_3_1_1_1 = input()
                                                                    if lab1_2_1_2_3_1_1 == "1": # Reset labrynth
                                                                        print("Matthew turned the corner. This must be it! He must have reached the end! Matthew was so excited! He looked forward, and in front of him was... a dead end.")
                                            if lab1_2 == "2": # Reset labrynth
                                                print("Matthew walked forward and turned to his right. He was slightly overwhelmed, as he saw before him a hallway with five different paths leading in different directions.")
                                                print("There was a path to the left just in front of him, a path to the right just ahead of that, another path to the left just ahead of that, and at the end of the hall, there")
                                                print("were paths leading both left and right.")
                                                print("------------------------------")
                                                print("1. First Left")
                                                print("2. First Right")
                                                print("3. Second Left")
                                                print("4. End Left")
                                                print("5. End Right")
                                                print("------------------------------")
                                                lab1_2_2 = input()
                                                if lab1_2_2 == "1": # Reset labrynth
                                                    print("Matthew decided to play it safe and take the first path to his left. He stepped around the corner, and saw in front of him a hallway leading to a right turn at the end.")
                                                    print("------------------------------")
                                                    print("1. Go Right")
                                                    print("------------------------------")
                                                    lab1_2_2_1 = input()
                                                    if lab1_2_2_1 == "1": # Reset labrynth
                                                        print("Matthew steped down the hall in front of him, and turned to the right. In front of him, he found a dead end.")
                                                if lab1_2_2 == "2": # Reset labrynth
                                                    print("Matthew decided to try the first path to the right. As he rounded the corner, he found in front of him yet another corner, this one to the left.")
                                                    print("------------------------------")
                                                    print("1. Go Left")
                                                    print("------------------------------")
                                                    lab1_2_2_2 = input()
                                                    if lab1_2_2_2 == "1": # Reset labrynth
                                                        print("Matthew walked forward and around the corner. He walked confidently, straight into a wall.")
                                                if lab1_2_2 == "3": # Reset labrynth
                                                    print("Matthew was feeling particularly daring, and decided to pick the second path to the left. He passed the first paths to the left and right. Ha! They")
                                                    print("probably lead to dead ends anyways. As Matthew neared his path of choice, he turned to see a short hall with a path to the left.")
                                                    print("------------------------------")
                                                    print("1. Go Left")
                                                    print("------------------------------")
                                                    lab1_2_2_3 = input()
                                                    if lab1_2_2_3 == "1": # Reset labrynth
                                                        print("Matthew perilously turned the corner. He could feel the creak in his bones as his legs slowly moved. His surroundings seemed to slow down as he became more and")
                                                        print("more frieghtened of his current situation. What was past this corner? Anything may be past this corner. Matthew's death may be waiting behind this corner! In the")
                                                        print("course of 7 seconds which felt like 29 hours, Matthew slowly stepped forward and turned. He was met with a horrifying sight! A dead end!")
                                                if lab1_2_2 == "4": # Reset labrynth
                                                    print("Matthew would walk to the end of this hall and turn to the left! That was surely the best course of action. Matthew gracefully walked to the end of the hall,")
                                                    print("thinking about what could possibly be at the end of this wreched labrynth. He neared the corner, and turned. He found another short hall, with one more corner at the")
                                                    print("end, also turning to the left.")
                                                    print("------------------------------")
                                                    print("1. Go Left")
                                                    print("------------------------------")
                                                    lab1_2_2_4 = input()
                                                    if lab1_2_2_4 == "1": # Reset labrynth
                                                        print("Matthew walked forward, his dreams at the forefront of his mind. He would find a magical tresure in this labrynth! Why would a cursed labrynth even be in a")
                                                        print("basement if not to hide treasure? 'Working on a guy to fix it? Right.' Matthew stepped around the corner, and found a dead end.")
                                                if lab1_2_2 == "5": # Reset labrynth
                                                    print("Matthew stepped forward down the hall, passing the first three halls, and then turned right as he reached the diverging halls at the end. As Matthew turned the corner,")
                                                    print("he saw another right corner a short ways away from him.")
                                                    print("------------------------------")
                                                    print("1. Go Right")
                                                    print("------------------------------")
                                                    lab1_2_2_5 = input()
                                                    if lab1_2_2_5 == "1": # Reset labrynth
                                                        print("Matthew treaded down the path and turned to the right. In front of him, he found another short hallway with a turn to the left, and a wall straight at the end.")
                                                        print("------------------------------")
                                                        print("1. Go Left")
                                                        print("2. Go Forward")
                                                        print("------------------------------")
                                                        lab1_2_2_5_1 = input()
                                                        if lab1_2_2_5_1 == "1": # Reset labrynth
                                                            print("Matthew wouldn't be a fool! Of course he wouldn't walk straight forward into a dead end! How dense did this labrynth think he was? Matthew walked forward and")
                                                            print("turned to his left with a strong temper. He would show this labrynth. He then walked forward, into another dead end.")
                                                        if lab1_2_2_5_1 == "2": # Reset labrynth
                                                            print("Matthew walked forward. It must be a trick! There must be some knid of secret hidden door at the end of this hall! The dead end must be a fake-out to detour people")
                                                            print("who try to solve the labrynth. Matthew reached the dead end, and noticed a piece of paper on the floor. He picked it up. There was writing on it, which read 'Yeah, you")
                                                            print("are pretty dense.'")
                                            if lab1_2 == "3": # Reset labrynth
                                                print("Matthew walked ahead and took the left turn at the end of the hallway. He rounded the corner, and found in front of him a dead end.")
                                        if lab1 == "3": # Reset labrynth
                                            print("Matthew walked straight ahead to the dead end. There was a note on the floor. Matthew picked it up and read it. 'You sure aren't very good at mazes, huh?' The")
                                            print("note guessed correct. Matthew was not good at mazes.")
                                        if firstTimeInBasement == False:
                                            if lab1 == "4": # Give up on labrynth ending path
                                                print("Matthew gave up, yada yada")
                                                break

                                            # Unsure what to do for maze. Maybe dead ends just teleport you back to the start and it's long enough of a maze to make that a deturrent
                                            # (Do this by putting the maze section in its own while loop)
                                            # But even if I did do that, how do you end it without solving the maze? Would there just be an option to give up each time you're sent back to the start?
                                            # Maybe

                                if Cave == True: # Elevator to cave path (Very Unfinished)
                                    print("Matthew chose Cave at any time ever")

                                # We have our work cut out here (For all of the various elevator floors and paths and things)

                            elif ans1_2_1_1_1_2_1_2_2_1 == "2": # Double doors after outtaJail path (Unfinished)
                                print()
                            elif ans1_2_1_1_1_2_1_2_2_1 == "3": # Imagination path
                                if undetected == True:
                                    print("But Matthew didn't like interesting things. He was exausted, and this couch was actually pretty comfortable. He decided that he would just stay there and imagine an adventure to")
                                    print("go on. Lets see, our protganist would be...")
                                    print("------------------------------")
                                    print("1. An apothecary")
                                    print("2. A fool")
                                    print("3. A cheapskate")
                                    print("4. A medieval farmer")
                                    print("------------------------------")
                                    ansprotaganist = input()
                                    if ansprotaganist == "1":
                                        print("An apothecary! And they would fight...")
                                        print("------------------------------")
                                        print("1. The drug industry")
                                        print("2. The government")
                                        print("3. A sentient toaster")
                                        print("4. Hans from the hit Disbley movie Cold")
                                        print("------------------------------")
                                        ansantagonist1 = input()
                                        if ansantagonist1 == "1":
                                            print("The entire drug industry! Matthew imagined an incredible legal battle between an apothecary who was sueing the whole drug industry for medical malpractice and disregard for patient safety.")
                                            print("The apothecary would point out that their skin care drugs gave people cancer, and the apothecary would win out. With the winnings, the apothecary would found a childrens hospital and go on")
                                            print("to be a internationally hailed hero and win the nobel peace prize. Matthew never exited his imagination.")
                                            print("------------------------------")
                                            print("Ending 16 of x - You got the Apothecary Hero ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                                            print("------------------------------")
                                            endStates[16] = True
                                            breaking = returnMenu()
                                            if breaking == True:
                                                break
                                        elif ansantagonist1 == "2":
                                            print("The United States Government. The apothecary would use his powerful drugs to make sleeping gas that would knock out all of the agents at a secure government facility. They would make")
                                            print("it into the most secure room and press the big self-destruct button that blows up every government building in the world. Matthew never exited his imagination.")
                                            print("------------------------------")
                                            print("Ending 17 of x - You got the Toppled Government ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                                            print("------------------------------")
                                            endStates[17] = True
                                            breaking = returnMenu()
                                            if breaking == True:
                                                break
                                        elif ansantagonist1 == "3":
                                            print("A living, breathing, sentient toaster! The apothecary would go to make some toast one morning, when the toaster decided that it was sick of making toast and decided to fight back. The toaster")
                                            print("would restrain the apothecary using its power cords. In response, the apothecary would punch the toaster sort of hard and it would break. Matthew never exited his imagination.")
                                            print("------------------------------")
                                            print("Ending 18 of x - You got the Toaster Fight ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                                            print("------------------------------")
                                            endStates[18] = True
                                            breaking = returnMenu()
                                            if breaking == True:
                                                break
                                        elif ansantagonist1 == "4":
                                            print("Hans, from the hit Disbley movie Cold! The apothecary would hit him really hard in the face and with the fight. Matthew never exited his imagination.")
                                            print("------------------------------")
                                            print("Ending 19 of x - You got the Hans ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                                            print("------------------------------")
                                            endStates[19] = True
                                            breaking = returnMenu()
                                            if breaking == True:
                                                break
                                    elif ansprotaganist == "2":
                                        print("A fool! And they would fight...")
                                        print("------------------------------")
                                        print("1. An idiot")
                                        print("2. A wall")
                                        print("3. A bowl of sherbert")
                                        print("4. A staircase")
                                        print("------------------------------")
                                        ansantagonist2 = input()
                                        if ansantagonist2 == "1":
                                            print("An idiot! It would be the contest of a lifetime! The fool would trip and fall on his face, the idiot would fail to notice a tree that was in front of his face, the two would never even")
                                            print("get close to landing a blow on one another. Matthew never exited his imagination.")
                                            print("------------------------------")
                                            print("Ending 20 of x - You got the Stupid ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                                            print("------------------------------")
                                            endStates[20] = True
                                            breaking = returnMenu()
                                            if breaking == True:
                                                break
                                        elif ansantagonist2 == "2":
                                            print("A wall! The fool would punch and kick and scratch at the wall trying to get through, not realizing that there was a door right next to them. They would fall unconsious before they could")
                                            print("make it through, and the wall would win the fight. Riveting.")
                                            print("------------------------------")
                                            print("Ending 21 of x - You got the Wall Wins ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                                            print("------------------------------")
                                            endStates[21] = True
                                            breaking = returnMenu()
                                            if breaking == True:
                                                break
                                        elif ansantagonist2 == "3":
                                            print("A delicous and scrumptious bowl of shrebert. The fool would grab the bowl, and throw it at an innocent bystander! The bystander would run in fear! The fool reigns supreme!")
                                            print("------------------------------")
                                            print("Ending 22 of x - You got the Sherbert Throw ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                                            print("------------------------------")
                                            endStates[22] = True
                                            breaking = returnMenu()
                                            if breaking == True:
                                                break
                                        elif ansantagonist2 == "4":
                                            print("A staircase! So much could go wrong in a fight with a staircase. The fool could trip up the stairs, and when they tried to retaliate they'd fall dowbn the stairs! This would")
                                            print("probably go on forever until the fool was rendered unconcious, and the staircase won.")
                                            print("------------------------------")
                                            print("Ending 23 of x - You got the Stairs Win ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                                            print("------------------------------")
                                            endStates[23] = True
                                            breaking = returnMenu()
                                            if breaking == True:
                                                break
                                    elif ansprotaganist == "3":
                                        print("A cheapskate! And they would fight...")
                                        print("------------------------------")
                                        print("1. The IRS")
                                        print("2. Organic produce")
                                        print("3. An entitled rich child")
                                        print("4. The means of production")
                                        print("------------------------------")
                                        ansantagonist3 = input()
                                        if ansantagonist3 == "1":
                                            print("The IRS! The cheapskate in question would be running from the law due to their frequent tax evasion. The IRS would track them down, and they'd have a chilling legal battle, where")
                                            print("the cheapskate would mock the judge and the jury and everyone else present, but still somehow escape with no repercussions because they were so convincing in their defense.")
                                            print("------------------------------")
                                            print("Ending 24 of x - You got the Cheapskate Wins the Trial ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                                            print("------------------------------")
                                            endStates[24] = True
                                            breaking = returnMenu()
                                            if breaking == True:
                                                break
                                        elif ansantagonist3 == "2":
                                            print("Organic produce! The cheapskate would be completely incapable of purchasing the produce due to its expensive nature! So, in retaliation, the cheapskate would leave the grocery store")
                                            print("with a stolen bag of cookies. Thus is the creul nature of capitalism.")
                                            print("------------------------------")
                                            print("Ending 25 of x - You got the Cheapskate Capitalism Cookies ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                                            print("------------------------------")
                                            endStates[25] = True
                                            breaking = returnMenu()
                                            if breaking == True:
                                                break
                                        elif ansantagonist3 == "3":
                                            print("An entitled rich child! It'd be like one of those wierd old movies where two people from completely opposite backgrounds meet each other for some crazy reason and become friends. Except")
                                            print("instead of becoming friends, or fighting some government agents or something, the cheapskate would just try to steal everything in the child's house and get arrested due to the blaring")
                                            print("alarm from their expensive security system.")
                                            print("------------------------------")
                                            print("Ending 26 of x - You got the Cheapskate Loses and goes to Jail ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                                            print("------------------------------")
                                            endStates[26] = True
                                            breaking = returnMenu()
                                            if breaking == True:
                                                break
                                        elif ansantagonist3 == "4":
                                            print("The means of production! The cheapskate hated the means of production. In the cheapskate's humble opinion, the end did not justify the means. To reach the cheapskate's desired end,")
                                            print("they would infiltrate a factory that made other factories, and blow it up with dynamite!")
                                            print("------------------------------")
                                            print("Ending 27 of x - You got the Cheapskate Destroys a Factory ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                                            print("------------------------------")
                                            endStates[27] = True
                                            breaking = returnMenu()
                                            if breaking == True:
                                                break
                                    elif ansprotaganist == "4":
                                        print("A medieval farmer! And they would fight...")
                                        print("------------------------------")
                                        print("1. A bird")
                                        print("2. A drought")
                                        print("3. A king")
                                        print("4. George Washington")
                                        print("------------------------------")
                                        ansantagonist4 = input()
                                        if ansantagonist4 == "1":
                                            print("A bird! Everyone knows that birds have occasionally been enemies of farmers. Why else would there be scarecrows? This particular bird would evade the farmer's every trap, slowly")
                                            print("destroying the farmers entire crop. The farmer would try to chase the bird in a last-ditch effort, but would not be able to keep up, and accidentally trip on a rock and fall down.")
                                            print("------------------------------")
                                            print("Ending 28 of x - You got the Farmer Falls Down ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                                            print("------------------------------")
                                            endStates[28] = True
                                            breaking = returnMenu()
                                            if breaking == True:
                                                break
                                        elif ansantagonist4 == "2":
                                            print("A drought! No farmer can grow their crops if there's a drought, so the drought would have the natural advantage over the farmer. The drought had not taken into consideration, however,")
                                            print("just how much rain water the farmer had been saving up in his secret basement. The farmer would single-handedly end the drought by pouring metric tons of water all over the ground. He")
                                            print("may or may not have been the reason that there was a drought in the first place...")
                                            print("------------------------------")
                                            print("Ending 29 of x - You got the Farmer Rehydrates the World ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                                            print("------------------------------")
                                            endStates[29] = True
                                            breaking = returnMenu()
                                            if breaking == True:
                                                break
                                        elif ansantagonist4 == "3":
                                            print("A king! Farmers have historically not been treated very well by those in higher positions of power, especially kings. The king in question would pass a law saying that 95 percent of the")
                                            print("farmer's crops were to be directly sent to the king's palace. The farmer would try to plead his case, but the king would react by creating a new law, saying that all farmers are banned")
                                            print("from entering the royal palace or having any say in laws. Never trust a king.")
                                            print("------------------------------")
                                            print("Ending 30 of x - You got the Farmer Banned from the Palace ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                                            print("------------------------------")
                                            endStates[30] = True
                                            breaking = returnMenu()
                                            if breaking == True:
                                                break
                                        elif ansantagonist4 == "4":
                                            print("George Washington! A bit of an odd choice, since old George-Washy lived many decades after the medieval times were over, but the farmer didn't mind. The farmer would take his pitchfork in")
                                            print("one hand, his hammer in the other, and charge into the battle! George Washington would counter an attempted strike from the pitckfork with a blow from his axe! In a quick response, the farmer")
                                            print("would duck back and slide to George Washington's feet, smacking one with his hammer! George WAshington would yell out in pain, and attempt to smack the farmer with his American flag, but")
                                            print("it wouldn't be very effective since it was a flimsy flag which didn't have much leverage. After George Washington's failed strike, the farmer would end the match by jabbing George Washington")
                                            print("with his pitckfork. George Washington would fall to his knees, and drop his axe and flag. The farmer would stand tall and victorious.")
                                            print("------------------------------")
                                            print("Ending 31 of x - You got the Farmer Defeats the American Spirit ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                                            print("------------------------------")
                                            endStates[31] = True
                                            breaking = returnMenu()
                                            if breaking == True:
                                                break
                                else:
                                    pass                    
                    elif ans1_2_1_1 == "2": # Drink water path (Frog bucket ending)
                        print("Matthew wasn't in a rush or anything, so he decided he should hydrate himself. Matthew's lips had been really dry today, and he felt like he hadn't been drinking enough")
                        print("water. Matthew awkwardly turned on the sink with his cuffed hands, and leaned over to take a sip of the water. As he did this he began to feel a tingling sensation all throughout")
                        print("his body. Before he could figure out what was happening, he found himself unable to reach the sink anymore. He also noticed that the handcuffs were gone. Then, he realized that somehow,")
                        print("he had been shrunken down to the size of a common frog. He looked at his little tiny hands. 'How did I fall for that again?' he thought. There seemed only one choice now.")
                        print("------------------------------")
                        print("1. Climb into the empty bucket and live there for the rest of your natural life")
                        print("------------------------------")
                        ans1_2_1_1_1 = input()
                        if ans1_2_1_1_1 == "1":
                            print("Matthew took the only clear course of action, and climbed into the bucket. Inside, he found a tiny, frog-sized bed, a set of matching frog-sized pajamas, and a comfroting brew of Matthew's")
                            print("favorite tea. Matthew changed into the pajamas, took a sip of tea, and flipped off the tiny lightswitch on the wall of the bucket. Matthew went to sleep.")
                            print("------------------------------")
                            print("Ending 12 of x - You got the Cozy ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                            print("------------------------------")
                            endStates[12] = True
                            breaking = returnMenu()
                            if breaking == True:
                                break  
                    elif ans1_2_1_1 == "3": # Stay in jail path (VERY UNFINISHED)
                        print("Matthew thought that this room was not so bad. That note freaked him out a little anyways, so he thought that he shouldn't worry, and that he'd probably be fine. He sat around and waited for")
                        print("something to happen.")

                        #MORE HERE                                                
                elif ans1_2_1 == "2": # Bide for time path
                    print("'Hey, I'm sorry- could we do this another time? I have an appointment with a hedge trimmer at 4:30, and-' 'Matthew, you know the answer to that question. We are going to deal with you")
                    print("now, whether that means locking you up, or something worse. You don't have any other options besides those two. Make your decision, now.' Matthew didn't think he'd be able")
                    print("to buy himself any more time. ")
                    print("------------------------------")
                    print("1. Surrender")
                    print("2. Sprint away")
                    print("------------------------------")
                    ans1_2_1_2 = input()
                    if ans1_2_1_2 == "1": # Surrender (but get saved by truck) path
                        print("Matthew bent down on his knees and held his wrists out towards the boy. He stared at him with strong emotions behind his eyes. 'Ah, good choice.' The boy grabbed a")
                        print("strange pair of handcuffs, but before he could put them on to Matthews wrists, suddenly, an enormus semi-truck containing the worlds most endangered frog species flew into")
                        print("the park out of nowhere. 'RUN!' 'WE'VE GOT TO GET OUT OF HERE!' Distressed screams echoed through the park as the truck barreled into the boy, missing Matthew by a hair,")
                        print("then it collided with a nearby stone wall and exploded. As the smoke cleared, Matthew realized that he could take this strangely perfect oppertunity to escape.")
                        print("------------------------------")
                        print("1. Sprint away in a random direction")
                        print("2. Stay and fight these fools!")
                        print("3. Go home to the Eiffel Tower")
                        print("------------------------------")
                        ans1_2_1_2_1 = input()
                        if ans1_2_1_2_1 == "1": # Run away to cruise ship path
                            print("Matthew's immediate reaction was to escape quickly, so he ran as fast as he possibly could in a random direction away from the park. He ran through narrow streets, which he would have")
                            print("thought were beautiful on any other day, were it not for his dire circumstances. He eventually found a long and open road that led him out of town. As the buildings around him thinned, he")
                            print("found himself running past elegant green fields and small lush forests. Occasionally a car would pass, or he would run by a fancy large home in the middle of nowhere, but besides that")
                            print("there was no one around. After running for a long time, Matthew noticed that he was getting close to a large river, and in the direction he was running there was a large boat which looked")
                            print("like some sort of cruiseline. He began to slow down as he got nearer to the boat, and saw a sign directing people to a stand where they could buy tickets. He followed its lead to a stand,")
                            print("and found another sign which outlined the prices of the tickets. A first-class ticket cost 300 Euros, and a regular ticket cost 30. Matthew only had 5 Euros to his name. He would have to")
                            print("find a way to get more if he wanted to get a ticket, which he felt oddly obliged to do for some reason. Before doing anything though, he also saw a sign saying that they were looking for")
                            print("workers on the ship. He bet he could get a job in the lower decks if he tried.")
                            print("------------------------------")
                            print("1. Try to steal a ticket")
                            print("2. Ask people for money to help pay for a ticket")
                            print("3. Get a job below deck")
                            print("------------------------------")
                            ans1_2_1_2_1_1 = input()
                            while True: # ENTER CRUISE SHIP EITHER WAY
                                if ans1_2_1_2_1_1 == "1": # Steal someone's ticket path
                                    print("Matthew felt that his best chance to get on the ship was to steal someone's ticket. He might even get first class if he stole well enough. He scanned the nearby area in search of someone who")
                                    print("he could steal from. He quickly spotted a very pompus looking man with a ticket sticking out of his pocket very obviously. Matthew snuck around behind him while he was talking to some people.")
                                    print("They didn't seem very interested in whatever he was talking about. 'So, you see, I have the biggest collection of clocks in the world! It doesn't matter what time anybody else says it is,")
                                    print("because I am the Master of keeping the time. So I was at this clocks enthusiast rally this weekend in Spain, and there were some real spectacular clocks there, let me tell you! I was talking")
                                    print("with this man, he said his name was Fifebinado, and he had a clock the size of me! I don't just mean it was large, no, it was actually the exact size and shape of me! doen to the clothes and")
                                    print("hair, a PERFECT, copy. I couldn't make a deal with him then to buy it due to my lack of proper funds, but we arranged for me to meet him tommorow when the cruise ship docks in Spain. OH, did I")
                                    print("ever tell you about the time...' Matthew began to tune the man out. No wonder the people he was talking to weren't paying attention. He never stopped talking. Well, at least that made him an easy")
                                    print("target. Matthew slipped the ticket out of the man's pocket as he told the people the story of when he bought a clock shaped like a vase. Matthew walked away from the man and readied himself to")
                                    print("get onto the cruise ship. Matthew looked over his ticket. It seemed that the man he'd stolen the ticket from was named Mr. Timely. Ridiculous. Matthew was near the end of the line, and as he")
                                    print("walked past the man who checked his ticket, he heard commotion coming from behind him. 'No, I have my ticket, I swear! I made extra sure to bring it on time! Look at my watch! No! Please! I must")
                                    print("go to Spain! Nooooooooo!' Mr. Timely yelled for mercy as the ticket checkers forced him off the ship. Matthew took a sigh of relief. He'd made it. Matthew picked up a brochure from a small stand")
                                    print("and looked it over. It had some basic tourist advertisements on the first few pages, but there was a map of the ship on page 4. Matthew saw that there were a few places he could go.")
                                    print("------------------------------")
                                    print("1. Go to the Ballroom/Dinning Hall")
                                    print("2. Go to Mr. Timely's former room")
                                    print("------------------------------")
                                    crus1 = input()
                                    if crus1 == "1": # Go to ballroom as guest path
                                        print("Matthew decided to go to the ballroom. He was sure that he'd have plenty of time to relax in Timely's fancy room later. He walked through the hallway and up a set of stairs which led to the")
                                        print("ballroom. Upon entry it was a magnificent sight. The ballroom was huge, easily the largest and tallest room Matthew had ever been in. The majority of the ballroom floor was filled with a large")
                                        print("number of fancy tables, all set and most empty. On the far end from where Matthew entered there was a huge double curved staircase leading up to a door. Across from the leigion of tables was an")
                                        print("open area, presumably for balling, whatever that was. Matthew had never figured that out. Besides everything else, the most eye-catching part of the room was a pillar in the very center of the")
                                        print("room, cordoned off with velvet ropes. The pillar was at least seven times taller than Matthew, and on the top there was a small glass case with a beautiful looking gemstone inside. Matthew was")
                                        print("fascinated by everything he saw. He had so many questions. He decided to scope out the scene and see what sort of people were on this ship with him. Through the sea of tables, Matthew counted (one")
                                        print("kindly young lad with an old looking cap), one fancy looking woman in a violet yellow and orange dress, (one distinguished looking gentleman with a very golden outfit), and one scrabby looking older")
                                        print("man sitting alongside a stern looking old woman. Matthew remembered seeing a guest registry in the pamphlet. Inside he found an astoundingly small guest list. He only found the names Mr. Timely,")
                                        print("Vivian Middleton (yelloworangepurpledress), Edward LASTNAME, Herbert Derber, BOYSNAME, OLDMANSNAME, STERNWOMANSNAME, and GOLDOUTFITSNAME. It was very strange to Matthew that such a huge and expensive")
                                        print("seeming ship would have so few customers.")
                                    elif crus1 == "2": # Go to Timely's room path
                                        print("Matthew was completely worn out from the chaos and the running and the running and the running, and he wanted to get some rest. He was sure that that Timely guy must have had a pretty")
                                        print(" fancy room based off of his appearance. Matthew walked through a hallway and up a staircase that led to the guest quarters. He eventually found the room that matched the number on")
                                        print(" Timely's ticket and opened the door. Inside, he found proof that his suspicions had been correct. The room had all of the luxuries of a modern house, including a living room area,")
                                        print(" kitchen area, seperate bedroom, a huge bathroom with a hot tub, and even a washer and dryer. Matthew went straight for the bed, and laid down. What a day. Matthew stayed there for a")
                                        print("minute in silence before doing anything else. He was tired. After a few minutes in silence, Matthew pulled the brocure from his pocket and looked it over again. Inside he found a ")
                                        print("guest list with the names of all the guests staying on the ship. Surprisingly, there were only eight(?) guests listed. The names in the pamphlet were Mr. Timely, Vivian Middleton,")
                                        print(" Edward LASTNAME, Count Herbert Derber, BOYSNAME, OLDMANSNAME, STERNWOMANSNAME, and GOLDOUTFITSNAME. Matthew found it very peculiar that a ship as huge and fancy as this one would")
                                        print("only have eight customers, but who knows? When Matthew walked past the other guest quarters, there certainly weren't very many rooms. Maybe this ship was just too elite to hold")
                                        print("any more customers.")
                                        print("As Matthew pondered over these things, his thoughts were inturrupted by an announcement on the loudspeakers. 'ALL NON-ESSENTIAL SHIP PERSONEL AND GUESTS, MAKE YOUR WAY TO THE BALLROOM IMMEDIATELY.")
                                        print("SOMETHING OF EXTREME SIGNIFIGANCE HAS OCCURRED.' Matthew wondered what was going on. Had something bad happened? He walked down the hallway towards the ballroom, and as he did, he saw a few other")
                                        print("guests heading there too. A strange looking man in a golden outfit remarked, 'I was in the middle of personal affairs! There'd better be a good explination for this.' Finally, Matthew reached the")
                                        print("ballroom doors. As he entered, he noted the extravagance of the room. There was a sea of fancy tables set up for dinner, and on the opposite end of the room there was an intricate double staircase")
                                        print("leading up to a balcony. In the center of the room was a tall pillar with what looked to be a gemstone on top inside of a glass case. Matthew was pulled back into the moment as he noticed a small")
                                        print("crowd formed below the staircase. As he walked up to the small crowd to ask what was happening, someone emerged from the door at the top of the stairs. He walked up to the railing and adressed the")
                                        print("crowd. 'Ladies and gentlemen,' the man began, 'a tragedy has occurred on our humble cruiseliner tonight.' The crowd began mumbling faintly, and one particularly old looking man shouted 'what's going")
                                        print("on?!' The man replied to the crowd. 'Tonight, there has been a murder!' The crowd broke into a frenzy. 'Everyone, we must remain calm. Let me explain what has happened.' Someone shouted, 'How did")
                                        print("this happen?!?' The man continued. 'At sometime within the last hour, someone broke into the room of Count Herbert Derber, and stabbed him to death.' 'Herbert Derber was murdered?! Dear God!'")
                                        print("'No! Not Herbert!' 'Who would do this?!' 'We are currently investigating the matter, but we have yet to find any leads. Everyone is urged to remain calm and return to their rooms until we have")
                                        print("a better grasp on the situation,' the man continued. 'I assure you, that I, Captain NAMENAME will not leave any of you in danger! Herbert will be avenged! Now return to your rooms. There is much to")
                                        print("do.' After the Captain finished his speech, the crowd began breaking up as everyone talked and walked away, presumably to their rooms.")
                                        print("Matthew was quite surprised by the events that had just taken place. He wasn't sure what to think. He wasn't sure what to do either, for that matter.")
                                        print("------------------------------")
                                        print("1. Go talk to the Captain")
                                        print("2. Go to your assigned quarters")
                                        print("3. Snoop for leads!")
                                        print("------------------------------")

                                if ans1_2_1_2_1_1 == "2": # Ask for money path (2 endings)
                                    print("Matthew decided that he would ask the lovely people of France for just a small bit of money so that he could afford a ticket. He was sure that the people who would pay to go on a luxury cruise would")
                                    print("be reasonable and charitable. He was wrong, though. Matthew repeatedly asked anyone who passed if they had any money to spare, but most of them just replied with, 'Oh, I apologize. I only pay with card,'")
                                    print("and then they walked away. There was one kind young lad who stopped for poor Matthew and gave him a whole 10 Euros, then told him it was 'No trouble at all!' Then winked and gave Matthew a kind smile,")
                                    print("but that was all he got. Matthew was beginning to burn daylight, and the ship was going to disembark soon. He was 10 Euros short of a ticket.")
                                    print("------------------------------")
                                    print("1. Attempt to sneak onto the ship")
                                    print("2. Give up on the ship")
                                    print("------------------------------")
                                    ans1_2_1_2_1_1_2 = input()
                                    if ans1_2_1_2_1_1_2 == "1": # Try to sneak on ship (fail) path
                                        print("")
                                    if ans1_2_1_2_1_1_2 == "2": # Give up on ship path
                                        print("")
                                if ans1_2_1_2_1_1 == "3": # Get a job on the ship path
                                    print("Matthew would get a job working on the ship. He was sure it wouldn't be that hard. He walked up to the man at the job applicant stand. 'Hello sir, could I find a job on this")
                                    print("cruiseliner?' The man had a very uninterested expression on his face. 'What do you want to get paid?' 'Oh, uh... less than minimum wage..?' 'You're hired.' The man gave Matthew")
                                    print("a sailor's uniform and a key to his room in the crew quarters. 'The ship departs in five minutes, so you'd better not miss it.' Matthew thanked the man and boarded the ship.")
                                    print("As he walked up the walkway onto the ship, another crew member stopped him and pulled him aside. 'Hey, I need to take a bathroom break, could you take people's tickets for me?'")
                                    print("'I don't know how.' 'It's easy, just punch a hole in it and let them through.' 'Oh, okay.' Matthew manned the ticket taking station for the next few minutes. While he was there,")
                                    print("he noticed a viriatey of colorful characters. There was a young and very kind lad, a very pompus man with watches all over his arms, a (ADD MORE PEOPLE DESCRIPTIONS HERE LATER).")
                                    print("As the last passenger walked by, Matthew left the ticket station. The man who'd given him the job had given him a brochure. There wasn't much of interst, save for a map of this ship,")
                                    print("detailing the various rooms. There were only a few places that Matthew figured he should go.")
                                    print("------------------------------")
                                    print("1. Go to the Ballroom/Dinning Hall")
                                    print("2. Go to your assigned quarters")
                                    print("3. Go to the boiler room")
                                    print("------------------------------")
                                    crus2 = input()
                                    if crus2 == "1": # Go to the ballroom as Crew path
                                        print("Matthew decided to go to the ballroom. He assumed that he might be able to find a clearer direction from there. He walked through the hallway and up a set of stairs which led to the")
                                        print("ballroom. Upon entry it was a magnificent sight. The ballroom was huge, easily the largest and tallest room Matthew had ever been in. The majority of the ballroom floor was filled with a large")
                                        print("number of fancy tables, all set and most empty. On the far end from where Matthew entered there was a huge double curved staircase leading up to a door. Across from the leigion of tables was an")
                                        print("open area, presumably for balling, whatever that was. Matthew had never figured that out. Besides everything else, the most eye-catching part of the room was a pillar in the very center of the")
                                        print("room, cordoned off with velvet ropes. The pillar was at least seven times taller than Matthew, and on the top there was a small glass case with a beautiful looking gemstone inside. Matthew was")
                                        print("fascinated by everything he saw. He had so many questions. He decided to scope out the scene and see what sort of people were on this ship with him. Through the sea of tables, Matthew counted (one")
                                        print("kindly young lad with an old looking cap), one fancy looking woman in a violet yellow and orange dress, (one distinguished looking gentleman with a very golden outfit), and one scrabby looking")
                                        print("older man sitting alongside a stern looking old woman. Matthew remembered seeing a guest registry in the pamphlet. Inside he found an astoundingly small guest list. He only found the names")
                                        print("Mr. Timely, Vivian Middleton (yelloworangepurpledress), Edward LASTNAME, Count Herbert Derber, BOYSNAME, OLDMANSNAME, STERNWOMANSNAME, and GOLDOUTFITSNAME. It was very strange to Matthew that")
                                        print("such a huge and expensive seeming ship would have so few customers.")
                                    elif crus2 == "2": # Go to Crew Quarters path
                                        print("Matthew was exhausted from all of the running he had done, so he decided to go to his assigned crew quarters. He checked the key that the man had given him. On on side it had a picture")
                                        print("of a gem, and the other side had the number 042 engraved into it. Matthew followed the map on the pamphlet through the halls until he found the hallway with his room in it. The crew")
                                        print("section of the ship where the crew quarters were located was more run down than the rest of the ship. There were old looking pipes making concerning noises and water dripping from some")
                                        print("places on the ceiling. He eventually came up to the door labeled '042'. He turned the key in the lock of the door, he heard a click, and the door opened. Inside he found a rather")
                                        print("small space with a rusty looking sink and a twin sized matress. He would have to make due. Matthew climbed onto the matress and curled up as small as he could. His feet still hung")
                                        print("over the edge, but it was better than nothing. 'How did it come to this?' Matthew thought, 'From living in the Eiffel Tower to living in absolute squalor.' Matthew slept to the")
                                        print("best of his ability for about 15 minutes.")
                                    elif crus2 == "3": # Go to boiler room path
                                        print("Matthew guessed that he should probably go to the boiler room and... work? He had no other clear leads as to where he needed to go to do his job, so he decided to go there. It took")
                                        print("Matthew a long time to find his way to the boiler room. After searching for at least 15 minutes, he finally found a small sign on the wall pointing towards the place he needed to go.")
                                        print("He walked down a narrow hall and down some stairs. The boiler room was at the very bottom of the ship, and the entrances to the boiler room and brig were straight across from each")
                                        print("other. Matthew chose not to question why a cruise ship needed a brig, and walked into the boiler room. Inside, he found an enormous, expansive room, wall-to-wall with huge tubes which")
                                        print("Matthew guessed were the boilers. There were a few other emplyees turning valves, and checking notes on clipboards. Matthew walked up to one of them. 'Hello,' said Matthew, 'I'm new here,")
                                        print("do you have any idea where I should go?' 'You're new? We aren't hiring any new employees to manage the boilers. Are you sure you didn't get hired as a waiter?' Matthew realized that he")
                                        print("hadn't actully considered what position he had been hired for. 'Oh, that would make sense,' Matthew responded after a moment. The man and Matthew stood awkwardly for a moment. 'Well...")
                                        print("I guess I'll be going then.' 'Okay, don't get lost.' The man walked away back to one of the boilers as Matthew stepped out of the room. 'Man,' Matthew thought, as he climbed up the stairs")
                                        print("and into the hall, 'I feel pretty ridiculous. What was I thinking? There's no way that I'm qualified to go anywhere near a gigantic water boiler anyways.' As Matthew emerged back into the")
                                        print("upstairs hallways, an announcement suddenly came over the loudspeakers. 'ALL NON-ESSENTIAL SHIP PERSONEL AND GUESTS, MAKE YOUR WAY TO THE BALLROOM IMMEDIATELY. SOMETHING OF EXTREME")
                                        print("SIGNIFIGANCE HAS OCCURRED.' Matthew definately wasn't essential personel, so he made his way to the Ballroom as the announcement directed. As he entered, he noted the extravagance of")
                                        print("the room. There was a sea of fancy tables set up for dinner, and on the opposite end of the room there was an intricate double staircase leading up to a balcony. In the center of the room")
                                        print("was a tall pillar with what looked to be a gemstone on top inside of a glass case. Matthew was pulled back into the moment as he noticed a small crowd formed below the staircase. As he")
                                        print("walked up to the small crowd to ask what was happening, someone emerged from the door at the top of the stairs. He walked up to the railing and adressed the crowd. 'Ladies and gentlemen,'")
                                        print("the man began, 'a tragedy has occurred on our humble cruiseliner tonight.' The crowd began mumbling faintly, and one particularly old looking man shouted 'what's going on?!' The man replied")
                                        print("to the crowd. 'Tonight, there has been a murder!' The crowd broke into a frenzy. 'Everyone, we must remain calm. Let me explain what has happened.' Someone shouted, 'How did this happen?!?'")
                                        print("The man continued. 'At sometime within the last hour, someone broke into the room of Count Herbert Derber, and stabbed him to death.' 'Herbert Derber was murdered?! Dear God!' 'No! Not Herbert!'")
                                        print("'Who would do this?!' 'We are currently investigating the matter, but we have yet to find any leads. Everyone is urged to remain calm and return to their rooms until we have a better")
                                        print("grasp on the situation,' the man continued. 'I assure you, that I, Captain NAMENAME will not leave any of you in danger! Herbert will be avenged! Now return to your rooms. There is much to do.'")
                                        print("After the Captain finished his speech, the crowd began breaking up as everyone talked and walked away, presumably to their rooms.")
                                        print("Matthew was quite surprised by the events that had just taken place. He wasn't sure what to think. He wasn't sure what to do either, for that matter.")
                                        print("------------------------------")
                                        print("1. Go talk to the Captain")
                                        print("2. Go to your assigned quarters")
                                        print("3. Snoop for leads!")
                                        print("------------------------------")
                        if ans1_2_1_2_1 == "2": # Die in an explosion ending path
                            print("Matthew was done with these F.R.O.G. people interfering with his life. He decided he was going to kick them while they were down! Matthew ran around kicking all of the members")
                            print("of the organization that he could find. He was pleased by their pain. Matthew laughed. 'ahahahaHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHa!!' Matthew was blind with anger. He kept kicking")
                            print("people, but eventually realized that there were almost no people left. In the commotion, he barely heard from a distance, someone yell something. What was it? ... Matthew heard it")
                            print("again, more clearly this time. 'Run, it's gonna blow!' Matthew tried to sprint away from the scene, but he was too slow. The park errupted into a huge explosion as the fire from")
                            print("the initial explosion sparked a flame in the propane tanks that people had been using to cook their chili before the chaos had started. Matthew whispered something under his breath as")
                            print("his body was incinerated by the flames of the massive explosion.")
                            print("------------------------------")
                            print("Ending 34 of x - You got the Emotional Explosion ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                            print("------------------------------")
                            breaking = returnMenu()
                            if breaking == True:
                                break
                        if ans1_2_1_2_1 == "3": # Go home ending path
                            print("Matthew was tried, and he just wanted to go home to be perfectly honest. He didn't expect so much to happen because of his attmept to socialize. Screams of panic and people runing away")
                            print("from the scene filled the park, as Matthew yawned and slowly walked towards the Eiffel Tower in which he lived. He climbed up into his home and went to sleep. The ambient noises of fire trucks,")
                            print("ambulances, and general commotion lasted through the night. At some point it had begun raining. The sky was dull, shrouded in dappled greys.")
                            print("------------------------------")
                            print("Ending 2 of x - You got the Just Tired ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                            print("------------------------------")
                            endStates[2] = True
                            breaking = returnMenu()
                            if breaking == True:
                                break

                        # More here?
                    elif ans1_2_1_2 == "2": # Get grappling hooked path
                        print("Matthew began running. 'Great conversation! Hope to not see you again sometime!' After about twenty paces Matthew felt something clamp onto his shirt. He fell over and was pulled")
                        print("back towards the boy. 'Matthew, you can't escape the power of a high quality GrappleMasters grappling hook. These things can grapple anything from dozens of yards away!  Just watch as")
                        print("I grapple this piece of blue cheese!' The boy unlatched the grapple hook and proceeded to grapple a piece of cheese from a cheese shop a long distance away. The grappling hook was gone")
                        print("for a moment.")
                        print("------------------------------")
                        print("1. Run again now")
                        print("2. Watch the demonstation")
                        print("------------------------------")
                        ans1_2_1_2_2 = input()
                        if ans1_2_1_2_2 == "1":
                            print("")
                        if ans1_2_1_2_2 == "2":
                            print("Matthew was impressed. That grappling hook was very sturdy to pull him back to the boy the way in did. Matthew was interested. The grappling hook quickly zipped back to the boy with the")
                            print("piece of blue cheese in tow. 'Wow,' Matthew said, 'that was amazing!' 'Isn't it? Any you can get one of these bad boys for yourself for only $19.99! Just call 572-3284-800!' 'But I don't")
                            print("have a phone,' Matthew responded. 'Aw, that's too bad.' The boy then grappled Matthew in the face and knocked him out.")
                            print("------------------------------")
                            print("Ending 38 of x - You got the GrappleMasters Grappling Hooks ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                            print("------------------------------")
                            endStates[38] = True
                            breaking = returnMenu()
                            if breaking == True:
                                break

            
            elif ans1_2 == "2": # Talk to the Muscular Man path
                print("Matthew mustered up his courage, and walked up to the man. Although his large stature seemed intimidating at first, as Matthew got closer, he")
                print("realized that the muscular man had a bouque of flowers in his hand, and was repeating something to himself under his breath. As Matthew walked up,")
                print("the man said, 'It'l be okay. C'mon, you can do this, you can do this, it'l be okay. C'mon, c'mon, you can do this, c'mon. You can-' 'Hey.' Matthew")
                print("inturrupted the man as he began to feel awkward about watching this silently. The man turned and looked at Matthew strangely. '...hey. What are you")
                print("doing here?' The man asked. Matthew was confused. 'What do you mean? Do I know you?'")
                print("------------------------------")
                print("1. I do know him!")
                print("2. I do not know him.")
                print("------------------------------")
                ans1_2_2 = input()      
                if ans1_2_2 == "1":
                    print("'Oh yeah!' Matthew exclaimed as his brain clicked. 'You must be that gardener I hired to trim the yard around my house. I'll show you over there.'")
                    print("'Wait, I'm not-' 'Sure you are! C'mon, lets go.' Matthew grabbed the man's arm and pulled him to the base of the Eiffel Tower. 'So here it is. I know")
                    print("that it's sort of a mess, but I'm sure you can handle it.' 'Wait sir, I think you've got me mistaken for anot-' The man was inturrupted by Matthew shoving")
                    print("a pair of hedge trimmers into his arms. 'Alright, good luck!' The man watched as Matthew scrambled up the tower and weaved his way into the structure.")
                    print("'Okay...' The man decided to simply listen to the stranger who just kidnapped him because he was sort of freaked out. He started trimming the hedges, and")
                    print("eventually he really started to get a rhythm going. 'Hey, this is kind of fun!' Hours passed and the man was still trimming away at the hedges as it got")
                    print("dark. Matthew came down to the ground and greeted him. The man expressed his gratitude to Matthew, as he enjoyed the trimming so much that he decided that")
                    print("he wanted to become a professional hedge trimmer. The man also asked Matthew if he could come back in a few weeks and trim his hedges again, and Matthew")
                    print("thought that that would be wonderful. Every few weeks, the man would show up, they would talk for a while, and the man would trim his hedges for him.")
                    print("And thus is the tale of the professional hedge trimmer.")  
                    print("------------------------------")
                    print("Ending 3 of x - You got the Personal Hedge Trimmer ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                    print("------------------------------")
                    endStates[3] = True
                    breaking = returnMenu()
                    if breaking == True:
                        break 
                elif ans1_2_2 == "2":
                    print("'Nope, I don't know you.' The man looked saddened by this answer, and sulked away. Matthew watched him, and thought hard as he stared at the man. After")
                    print("he watched him walk away, he decided he was sad too. Like that man. Now sad, Matthew sulked in that same direction. Eventually, after a while had passed,")
                    print("Matthew found the man, sad, sitting on a bench. Matthew sat down and sighed. 'I'm sorry I don't know who you are.' 'I don't even know who I am myself anymore.'")
                    print("The man began to sob, and Matthew sobbed with him. They cried together on that bench, shunned, outcast by the world, alone.")
                    print("------------------------------")
                    print("Ending 4 of x - You got the Sad ending! :D")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                    print("------------------------------")
                    endStates[4] = True
                    breaking = returnMenu()
                    if breaking == True:
                        break
            elif ans1_2 == "3": # Talk to the Regular Guy path
                print("Matthew walked up to the man. 'Hello,' said Matthew. 'Hi' said the man. 'Great conversation!' Yelled Matthew as he sprinted away. Matthew was")
                print("simply too scared to continue, so he took the reasonable course of action and ran as far away as possible, until he got all the way to the ocean.")
                print("He looked around, and saw a few things. First, he saw a large rectangular structure that ominusly streched high into the sky. He also saw a lighthouse on")
                print("the precipus of a nearby cliff, hanging over the water. In front of him, far out in the middle of the ocean, he saw a fancy looking ship, possibly an")
                print("expensive cruiseline.")
                print("------------------------------")
                print("1. Go to the structure")
                print("2. Go to the lighthouse")
                print("3. Investigate the ship")
                print("------------------------------")
                ans1_2_3 = input()
                if ans1_2_3 == "1":
                    print()
                elif ans1_2_3 == "2":
                    print("Matthew decided to go to the lighthouse. He wanted to investigate it, because he realized that the light wasn't on and that might mean that the ship out in the water")
                    print("was in trouble. Matthew ran up the hill to the top of the cliff while the cool marine air blew past him and the sound of the crashing ocean waves echoed across the")
                    print("landscape. As Matthew neared the lighthouse")

                    #MORE HERE MORE HERE
                    
                elif ans1_2_3 == "3":
                    print("Matthew decided he was more interested in the ship that was very far away in the water than the two buildings which he could easily walk to. On his quest to feel")
                    print("powerful and important, he attempted to swim out to the cruise ship. On the way, he felt something pulling at him. Not exactly physically, but he felt like he was")
                    print("being pulled down. Suddenly, Matthew found himself swept under the water. He began to struggle, and try to swim up, but he couldn't make any progress. 'Is this it?'")
                    print("Matthew wondered to himself. 'Is this how it ends?' It was, as it turns out, not how it ends, as Matthew fell out of the water, down into a large, expansive cavern,")
                    print("and landed hard on one leg. 'AHHHGG!' Matthew yelled. Matthew was in pain, but he made sure to take note of his surroundings. He was in a barren looking cavern filled with")
                    print("stalagmites and stalagtites jutting from the floor and the ceiling. There were crystals sprinkled around the cave, emitting a faint glow which served as the only real source")
                    print("of light. Looking up to the place where he fell from, Matthew saw a sight which was generally unexplainable. He had fallen from the water, because the water suddenly stopped in midair,")
                    print("leaving a flat surface which covered a small hole in the ceiling. Matthew's mind snapped back to his current circumstances as he heard a loud noise coming from")
                    print("somewhere in the cave. Matthew tried to stand, but he felt like his leg was broken, and fell back down on his side.")
                    print("------------------------------")
                    print("1. Stand anyways!")
                    print("2. Check your pockets")
                    print("3. Stay silent and wait")
                    if hasRolex == True:
                        print("4. Check your very expensive Rolex to ascertain the time of your own demise")
                    print("------------------------------")
                    ans1_2_3_3 = input()
                    if ans1_2_3_3 == "1":
                        print("Matthew was determined. He would not give in! He used every ounce of strength in his body to stand up without screaming. He looked all around him. There was only one direction that he")
                        print("could see an opening in, and that was where the noises had come from. Matthew was scared. He didn't want this to happen. He felt someting horrible in his soul. Something was completely wrong")
                        print("here. He felt a darkness approaching. Before he could see anything emerge from the opening, everything went black.")
                        print("------------------------------")
                        print("Ending 35 of x - You got the Unprepared ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                        print("------------------------------")
                        endStates[35] = True
                        breaking = returnMenu()
                        if breaking == True:
                            break
                    if ans1_2_3_3 == "2":
                        print("Pockets! Matthew had to have something in his pockets that could help him! He searched through his belongings. He had:")
                        # Add every item description here IF you have obtained said item
                        # No matter how powerful or useful the objects would be in this situation, its going to say that nothing he had could help him here lol
                        print("He also had a paperclip and some glitter. Nothing useful here. Matthew tensed up. He didn't know what was coming, and he wouldn't find out. He suddenly felt a horrible chill crawl")
                        print("down his spine. Something was wrong. He felt very wrong. Something was here. It was loud. It was silent. Before he could see what was happening, everything went black.")
                        print("------------------------------")
                        print("Ending 36 of x - You got the Nothing Useful ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                        print("------------------------------")
                        endStates[36] = True
                        breaking = returnMenu()
                        if breaking == True:
                            break
                    if ans1_2_3_3 == "3":
                        print("Matthew stayed silent and waited. He didn't want to jump to any conclusions about what was happening. Plus, he hardly felt like he could move in the first place. Matthew stared at the")
                        print("ceiling where he'd fallen in for a moment...")
                        print("He felt that there was a presence in the room. He was scared. He didn't move. He felt something getting closer to him. Something dark. He knew that this was wrong. He felt it. He waited")
                        print("silently until everything went black.")
                        print("------------------------------")
                        print("Ending 37 of x - You got the Presence ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                        print("------------------------------")
                        endStates[37] = True
                        breaking = returnMenu()
                        if breaking == True:
                            break
                    if ans1_2_3_3 == "4":
                        if hasRolex == True:
                            print("")
                        else:
                            pass

        elif ans1 == "3": # Jump off the tower into the pond path
            print("'Ah, so I finally have an audience.' Matthew had been waiting for an oppertunity like this. He'd been practicing for months now, and he had eagerly awaited")
            print("for an oppurtunity to show off to everyone. Matthew yelled 'HEY EVERYONE! WATCH ME!' People tuned their heads to see what the commontion was about, and they")
            print("watched as Matthew gracefully perfomed a triple front-flip, followed by a triple-backflip, followed by a mid-air moon-walk, as he flew in the direction of the")
            print("pond. Those watching were mezmerized by Matthews incredible ability, and applauded his amazing techniques and movements. Matthew was so, so happy that he was")
            print("finally being recognized for his skills. He was so happy, in fact, that he didn't even notice the flat surface of the water zooming towards his face at over")
            print("100 MPH.")
            print("------------------------------")
            print("Ending 6 of x - You got the Oww... ... ...That Must've Hurt... ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
            print("------------------------------")
            endStates[6] = True
            breaking = returnMenu()
            if breaking == True:
                break   
        elif ans1 == "4": # Try all the chili's down there at once (Wizard) path
            print("Matthew was bored, so he decided he would remedy that. He climbed down his tower, and walked into the chili picnic. He looked around, and saw tens of pots")
            print("of delicious chili all around him. As he looked upon the great pots of chili, he notcied that there were some very odd things around each of them. The ground")
            print("around one pot was covered in pink glitter, near another pot there were a bunch of piles of clothes, and around another, the was what looked to be a huge pile")
            print("of unopened white-out contatiners.")
            print("------------------------------")
            print("1. Try the glitter chili")
            print("2. Try the clothes chili")
            print("3. Try the white-out chili")
            print("4. Wait...")
            print("------------------------------")
            ans1_4 = input()
            if ans1_4 == "1":
                print("Matthew grabbed a serving spoon and proceeded to take a bit of the chili with the glitter around it. He stood there for a moment, and then he exploded.")
                print("Into glitter.")
                print("------------------------------")
                print("Ending 9 of x - You got the Oh, That Chili's Still Trapped ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                print("------------------------------")
                endStates[9] = True
                breaking = returnMenu()
                if breaking == True:
                    break
            elif ans1_4 == "2":
                print("Matthew grabbed a serving spoon and proceeded to take a bit of the chili with the clothes around it. It tasted like fabric and it was full of threads")
                print("and fuzz. Then Matthew stopped existing. His clothes fell into the pile with the rest")
                print("------------------------------")
                print("Ending 8 of x - You got the Lint Chili ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                print("------------------------------")
                endStates[8] = True
                breaking = returnMenu()
                if breaking == True:
                    break
            elif ans1_4 == "3":
                print("Matthew grabbed a serving spoon and proceeded to take a bit of the chili with the white-out around it. As he looked closer at the chili, he relized it")
                print("was just a pot full of white-out, and the containers weren't full, they were empty. Above the pot there was a sign that said 'lol gottem' on it in crude")
                print("handwriting. Matthew felt like a fool. Then, as he stood there, he watched all of his surroundings turn white...")
                print("------------------------------")
                print("Ending 7 of x - You got the White-Out ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                print("------------------------------")
                endStates[7] = True
                breaking = returnMenu()
                if breaking == True:
                    break   
            elif ans1_4 == "4":
                print("Looking at all of these sights made Matthew feel slightly uneasy... where was everyone? Why would everyone at the picnic suddenly just vanish and leave")
                print("behind such an odd scene? What with the clothes? The glitter? The white-out? As Matthew pondered over these questions he began to notice something else odd.")
                print("The sky was startsing to fill with clouds, and the environment around him was slowly getting darker, and darker. Matthew was starting to get really freaked")
                print("out. He didn't like the feeling he was getting from this. The wind was starting to pick up. It felt like something was about to happen.")
                print("------------------------------")
                print("1. Get out of this place")
                print("2. Stay right here")
                print("3. Look for a hiding spot")
                print("------------------------------")
                ans1_4_4 = input()
                if ans1_4_4 == "1":
                    print("Matthew  absolutely did NOT feel good about his current situation, so he thought it'd be better to be basically anywhere else. He ran away from the park in a")
                    print("miscellaneous direction, and as he was nearly out of the park he heard a loud boom. He looked behind him. 'Am I dreaming?'")
                    print("Behind Matthew, right in the clearing he'd been standing in, there was a huge flash of blue light, and as Matthew's eyes adjusted, he saw a figure standing there,")
                    print("who seemed to be some kind of wizard. Matthew hid behind a tree and continued to watch. The wizard was walking around the different pots of chili, tasting them")
                    print("and inspecting the odd things that were laying on the ground around them.")

                    # MORE HERE

                elif ans1_4_4 == "2":
                    print("Matthew wasn't scared. No way. Definately... not. He decided that he was going to stand his ground, and whatever was about to happen, was probably nothing at")
                    print("all and he definately didn't need to worry. As he stood there, he spotted some strange blue sparks forming in midair. They started to grow much more abundant, and")
                    print("suddenly, Matthew was blinded by a huge flash of blue light. He tripped over backwards and fell onto the ground. As his eyes adjusted, and the light went out, he")
                    print("saw in front of him the silhouette of a humanoid figure. Matthew came back to his wits, and realized that the man standing before him was wearing a wizard costume.")
                    print("He had a blue robe with purple undertones, a pointy blue wizard hat with stars on it, and a long white beard. The complete package. 'Ah,' he said, in a wizardly")
                    print("voice,'so you've passed my trial of chili, huh?'")
                    print("------------------------------")
                    print("1. Insult him")
                    print("2. Say nothing")
                    print("------------------------------")
                    ans1_4_4_2 = input()
                    if ans1_4_4_2 == "1":
                        print("'Thou venomed crook-pated haggard!' Matthew hurled a Shakespearean insult at the feind. 'Wow, how rude!' yelled the wizard, with an increasing anger in his tone.")
                        print("'I don't like you!' The wizard used his wizardly powers. 'Aga baga wooga woo, I now turn your face into a shoe!' Matthew could no longer see or hear, and he couldn't")
                        print("feel his face at all. Matthew soon realized he was completely unable to breath, and started to lose conciousness. 'That's what you get, jerk!' the wizard yelled at him")
                        print("in his last moments. Matthew fell to the gorund.")
                        print("------------------------------")
                        print("Ending 13 of x - You got the Shoe ending!")#ENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDINGENDING
                        print("------------------------------")
                        endStates[13] = True
                        breaking = returnMenu()
                        if breaking == True:
                            break
                    if ans1_4_4_2 == "2":
                        print("The wizard continued speaking. 'I expected that there would be someone out there with a will powerful enough to resist the temptation of my cursed chili. Tell me boy, what")
                        print("is your name?' 'Cursed chili..?' As Matthew looked around at the chili, he noticed that each of the pots around them seemed to be glowing just the faintest bit. The wizard")
                        print("continued. 'Your name, boy?' 'Oh, my name is Matthew. So this is all your chili?' 'Why yes!' The wizard used his wizardly powers of translocation and levitated one of the")
                        print("pots of chili in the direction of the two of them. He held it up to Matthew's face, and pointed at a little engraving of himself that was on the side of the pot. 'I made")
                        print("all of this chili with my own two hands. I also made all of these pots with my own two hands. As a test. And you passed!' The wizard conjured a party popper and confettied")
                        print("Matthew in the face. Matthew had a momentary coughing fit, then responded.")
                        print("------------------------------")
                        print("1. 'What is your name?'")
                        print("2. wip")
                        print("3. wip")
                        print("------------------------------")
                        ans1_4_4_2_3 = input()
                        if ans1_4_4_2_3 == "1":
                            print("'What is your name?' Matthew asked the wizard. 'My name is Alphonzo Khusnitzof!' The wizard replied, 'I have created this test as means of finding someone capable of learning my")
                            print("powerful ways. I want that someone to be you Matthew.' 'You want me to learn magic because I didn't eat some chili?' Matthew was confused. This wizard was quite the peculiar one.")
                            print("'It wasn't just any old chili you succeeded in not eating, it was my special irresistable concoction which pulls people's minds towards it with its incredible smell and its delicious")
                            print("flavor! I'm impressed that you could resist the urge to eat it,' explained the wizard. Matthew didn't say anything, but in reality he didn't feel like he smelt anything at all when")
                            print("he walked into this area a few moments ago.")

                            #MORE HERE
                            
                        elif ans1_4_4_2_3 == "2":
                            print("")
                        elif ans1_4_4_2_3 == "3":
                            print("")

                elif ans1_4_4 == "3":
                    print("")
    if ans == "2": # Check achieved endings
        if anyEndingAchived == True:
            print("List of all endings currently discovered:")
            if endStates[0] == True:
                print("Ending 0 - a Failiure ending...")
            if endStates[1] == True:
                print("Ending 1 - the Very Hot Tub ending!")
            if endStates[2] == True:
                print("Ending 2 - the Just Tired ending!")
            if endStates[3] == True:
                print("Ending 3 - the Personal Hedge Trimmer ending!")
            if endStates[4] == True:
                print("Ending 4 - the Sad ending! :D")
            if endStates[5] == True:
                print("Ending 5 - the Oh, That Chili Was Trapped ending!")
            if endStates[6] == True:
                print("Ending 6 - the Oww... ... ...That Must've Hurt... ending!")
            if endStates[7] == True:
                print("Ending 7 - the White-Out ending!")
            if endStates[8] == True:
                print("Ending 8 - the Lint Chili ending!")
            if endStates[9] == True:
                print("Ending 9 - the Oh, That Chili's Still Trapped ending!")
            if endStates[10] == True:
                print("Ending 10 - the Fly Fly Away ending!")
            if endStates[11] == True:
                print("Ending 11 - the Escaped ending!")
            if endStates[12] == True:
                print("Ending 12 - the Cozy ending!")
            if endStates[13] == True:
                print("Ending 13 - the Shoe ending!")
            if endStates[14] == True:
                print("Ending 14 - the Quick, Quick, Draw! ending!")
            if endStates[15] == True:
                print("Ending 15 - the Wait ending!")
            if endStates[16] == True:
                print("Ending 16 - the Apothecary Hero ending!")
            if endStates[17] == True:
                print("Ending 17 - the Toppled Government ending!")
            if endStates[18] == True:
                print("Ending 18 - the Toaster Fight ending!")
            if endStates[19] == True:
                print("Ending 19 - the Hans ending!")
            if endStates[20] == True:
                print("Ending 20 - the Stupid ending!")
            if endStates[21] == True:
                print("Ending 21 - the Wall Wins ending!")
            if endStates[22] == True:
                print("Ending 22 - the Sherbert Throw ending!")
            if endStates[23] == True:
                print("Ending 23 - the Stairs Win ending!")
            if endStates[24] == True:
                print("Ending 24 - the Cheapskate Wins the Trial ending!")
            if endStates[25] == True:
                print("Ending 25 - the Cheapskate Capitalism Cookies ending!")
            if endStates[26] == True:
                print("Ending 26 - the Cheapskate Loses and Goes to Jail ending!")
            if endStates[27] == True:
                print("Ending 27 - the Cheapskate Destroys a Factory ending!")
            if endStates[28] == True:
                print("Ending 28 - the Farmer Falls Down ending!")
            if endStates[29] == True:
                print("Ending 29 - the Farmer Rehydrates the World ending!")
            if endStates[30] == True:
                print("Ending 30 - the Farmer Banned from the Palace ending!")
            if endStates[31] == True:
                print("Ending 31 - the Farmer Defeats the American Spirit ending!")
            if endStates[32] == True:
                print("Ending 32 - the Fading Footsteps Trick ending!")
            if endStates[33] == True:
                print("Ending 33 - the Ha, Fading Footsteps Trick Again! ending!")
            if endStates[34] == True:
                print("Ending 34 - the Emotional Explosion ending!")
            if endStates[35] == True:
                print("Ending 35 - the Unprepared ending!")
            if endStates[36] == True:
                print("Ending 36 - the Nothing Useful ending!")
            if endStates[37] == True:
                print("Ending 37 - the Presence ending!")
            if endStates[38] == True:
                print("Ending 38 - the GrappleMasters Grappling Hooks ending!")
    if ans == "3":
        if hasAnyItem == True:
            pass
    if ans == "4":
        if allEndingsAchived == True:
            pass
            # Sort of a "True" kind of ending
    