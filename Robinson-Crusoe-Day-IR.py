import time
#defining load function
def threeTwoOne():
  load=3
  for x in range(3):
    print(load)
    time.sleep(1)
    load-=1
    
def waitThree():
  time.sleep(3)
  
print("Hello player! Welcome to the choose your own adventure of Robinson Crusoe day!")
print("Here are the rules:")
print("Words will appear on the screen explaining what is happening in the story")
print("When you finish reading the words, the computer will wait three seconds and then show you more of the story")
waitThree()
print("When you are given an option between different choices during this game,")
print("the game will instruct you what to write in the textbox if you want one option")
print("and what to write in the textbox if you want another choice!")
print("Let's try that out as well!")
print("If you are ready to play, type Yes If you are not ready, type anything")
print("that is not Yes")
print("Are you ready to play?")
y=input()
while y != "Yes":
  print("Type yes when you are ready to play!")
  y=input("Yes")

print("there is one more rule:")
print("if you choose the wrong option, you die, and the code will stop working")
print("so if the code tells you that you're dead, reload the code and try again!")
print("good luck!")

#this is my function
#importing timer
import time
#defining load function
def threeTwoOne():
  load=3
  for x in range(3):
    print(load)
    time.sleep(1)
    load-=1
# this function makes the next printed message wait three seconds before it appears
def waitThree():
  time.sleep(3)

print("Hello! Your name is Robinson Crusoe and you just woke up.")
print("You’re lying on the forest floor.")
time.sleep(3)
print("You are in the Evil Forest, the most dangerous forest in the world.")
print("There are poisonous snakes, tigers, frogs, leopards, deer, wild boar, squid, and more.")
waitThree()
print("You are in grave danger, and you need to get out of the forest as soon as possible.")
print("But there is a problem, you have no idea how to get out. ")
time.sleep(3)
print("You don’t know what part of the forest you are in, all you can see are some markings on the forest floor.")
time.sleep(3)
print("One marking says: This way to truth...")
print("The other reads: The road less travelled")
print("If you follow the advice of marking one, write Choice1")
print("If you follow the advice of marking two, write Choice2")

# This is the variable I will use when the player dies!
death=("You're dead! Better luck next time!")

Choice=input('')
time.sleep(1)
if Choice == "Choice1":
  print("You follow the arrow and reach a clearing. ")
  print("There is a large plank of wood on the ground, and you sit down to catch your breath.")
  print("You rest your eyes, and before you know it, you’re fast asleep")
  time.sleep(3)
  print("You wake up to the sound of slivering")
  print("You immediately open your eyes and in front of you is the biggest snake you could ever imagine")
  waitThree()
  print("You try to stand up to run away, but realize that the snake has already wrapped itself around you")
  print("It's too late")
  print("Within seconds, the snake has crushed you to death")
  print(death)
  quit
elif Choice == "Choice2": 
  print("You follow the arrow and walk for a few hours, until you spot a clearing")
  print("On the ground lays a squirrel that is sleeping")
  print("Your stomach grumbles and you feel a sudden urge to kill the squirrel and eat it")
  time.sleep(3)
  print("You are running out of energy and you need some protein to continue your journey.")
  print("But you don’t know where that squirrel has been, where you are going to cook it, or what other animals might be lurking in this area. ")
  print("Do you choose to kill the squirrel (type “Eat”), or keep walking (type “Walk”)?")

Squirrel=input()
time.sleep(1)
if Squirrel == "Eat":
  print("You grab a rock lying on the floor beside the squirrel, and stab the squirrel in the head with the rock")
  print("you pick up the dead squirrel and look around to see how you will cook it.")
  print("After eating the squirrel, you drink some water from a nearby stream and continue on your way.")
  time.sleep(3)
  print("It begins to rain")
  print("After walking for a few hours, you notice that the sun is beginning to set, so you start to look around for a place to sleep")
  time.sleep(3)
  print("On your left, there is a cave with enough coverage to protect you from the rain")
  print("On your right, there is a patch of flattened grass that is being rained on")
  print("The cave looks promising, but you have a feeling that there might be dangerous animals living inside")
  print("The grass is safe from animals, but you know that you might get cold throughout the night from the rain")
  waitThree()
  print("Do you choose to sleep in the cave (type “Cave”) or on the grass (type “Outside”)?")
elif Squirrel == "Walk":
  print("You continue walking, ignoring the gnawing sense of hunger building up inside you")
  print("After a few hours of walking, the hunger begins to affect your mind, and you start hallucinating, but there is nothing you can do but look for food")
  print("In front of you, there is a man")
  time.sleep(3)
  print("You cannot believe that someone else is in the forest with you, so you start running to catch up with him")
  time.sleep(3)
  print("You run for a few minutes and suddenly you lose your balance and slip off a cliff.")
  print("As you plunge to your death you realize the man was just a figment of your imagination due to hunger")
  print(death)
  quit 

Sleep=input()
time.sleep(1)
if Sleep == "Cave":
  print("You walk into the cave and find yourself a place to sleep that is close to the entrance so you can run away if necessary")
  print("You lie down and fall asleep")
  time.sleep(3)
  print("When you wake up, the sun is about to rise")
  print("You’re freezing cold, but luckily the rain never made its way to where you were sleeping last night.")
  time.sleep(3)
  print("You walk outside the cave and see some markings on the ground.")
  print("One marking is next to five big planks of wood and a pile of sticks. It reads “Use the wood to make fire, and hunt for fish with the sticks”")
  print("The other says “Leave this place immediately, danger is near. When you reach the tallest tree there will be food”")
  waitThree()
  print("Do you stay to make a fire and fish, or do you take the second markings warning to leave immediately?")
  print("If you want to stay and make a fire, type “Stay”. If you want to leave and find the tallest tree, type “Leave”")

elif Sleep == "Cave":
  print("You lie down on the grass and try to ignore the freezing rain falling on you and your “bed”. ")
  time.sleep(3)
  print("Within an hour, the freezing rain has become so unbearable that you are unable to move any part of your body")
  print("You realize that you have frostbite and slowly freeze to death")
  print(death)
  quit

Walk=input()
time.sleep(1)
if Walk == "Stay":
  print("You take the sticks and walk to the nearest stream.")
  print("There are many fish in the water, and you kill three.")
  time.sleep(3)
  print("You come back to the wood and make a fire, cook the fish, and sit down to eat.")
  print("You’re enjoying your meal when you hear a roar behind you")
  time.sleep(3)
  print("A bear comes out of nowhere, rips the fish from your hands, eats it, and then goes on to kill you")
  print(death)
  quit
elif Walk == "Leave":
  print("You quickly leave the area and climb up a rock, in order to find the tallest tree")
  time.sleep(3)
  print("On the rock, you spot a tree half a mile away that is much taller than the others around it")
  print("After walking for a while, you finally reach the tree, and you’re overjoyed by what you find")
  time.sleep(3)
  print("There is a large fire and four plates of all kinds of food sitting on the ground beside the fire")
  print("An envelope rests in front of the plates which reads “Pick one plate to eat, and choose wisely!”")
  waitThree()
  print("You look at the four plates, all heaping with your favorite kinds of food. One plate is blue, another is green, one is red, and the last one is black")
  print("If you choose the blue plate type “Blue”. If you choose the green plate type “Green”. For the red plate type “Red”. For the black plate type “Black”.")

Food=input()
time.sleep(1)
if Food == "Blue":
  print("You take the blue plate and begin to eat, but soon you begin to feel tired. Your eyes start to close and you fall into a deep sleep")
  time.sleep(3)
  print("You sleep for days until a wild boar comes along one day and eats you")
  print(death)
  quit

elif Food == "Green":
  print("You take the green plate and begin to eat")
  time.sleep(3)
  print("You haven’t such amazing food in so long, and you are so happy that you let out a laugh")
  print("Soon you can’t stop laughing and hours pass")
  time.sleep(3)
  print("You cannot contain your laughter. You try to stop laughing, but you can’t, and soon you choke to death.")
  print(death)
  quit

elif Food == "Red":
  print("You take the red plate and start to eat")
  waitThree()
  print("The meal tastes amazing, and when you are finished eating you rest your back on the tree as you sit")
  print("You are contemplating where you are going to go today when you feel something behind you moving")
  time.sleep(3)
  print("You turn around to see what happened, and you realize that the part of the tree you had been leaning on has disappeared")
  print("In its place is what seems to be a dark bottomless pit")
  time.sleep(3)
  print("You try to run away, but you are not quick enough, and you fall into the pit")
  print("You scream as your fall for a few minutes into nothingness.")
  time.sleep(3)
  print("But then you hit the ground")
  print("You stand up and look around.")
  print("You are in a small room without a ceiling and there are lights on the wall")
  print("In front of you are two doors. One is red and the other is blue")
  time.sleep(3)
  print("Which door do you walk through?")
  print("To go through the red door type RedDoor and to go through the blue door type BlueDoor")

elif Food == "Black":
  print("You eat a few bites and realize you have been poisoned")
  print("You came so far only to die a painful death now")
  print(death)
  quit

Door=input()
time.sleep(1)
if Door == "RedDoor":
  print("You walk through the red door and keep walking down a narrow hallway for a few minutes")
  print("Finally, you see light up ahead")
  waitThree()
  print("You run to the light and when you reach it you realize it leads to a busy street in a city.")
  print("You have returned to civilization without a scratch!")
  time.sleep(3)
  print("Great decision making! :)")

elif Door == "BlueDoor":
  print("You walk through the door and immediately step on a knife")
  time.sleep(3)
  print("You have been impaled.")
  print("You bleed to death")
  print(death)
  quit
