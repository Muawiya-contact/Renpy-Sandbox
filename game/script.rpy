# Define characters
define narrator = Character("Narrator")
define john = Character("John", color="#c8c8ff")
define player = Character("You", color="#ffff00")

# Start of the game
label start:
    narrator "Welcome to MyGame!"
    narrator "This is a simple visual novel adventure."
    
    john "Hello! I'm John. Nice to meet you!"
    
    player "Hi there!"
    
    menu:
        "What's your name?":
            $ player_name = "Friend"
            john "Nice to meet you too, Friend!"
            jump storyline_1
        
        "I don't talk to strangers":
            john "Oh... that's okay."
            john "But we could be friends!"
            jump storyline_2

label storyline_1:
    narrator "John smiles warmly."
    john "I'm glad we're friends now!"
    john "I wanted to tell you about an adventure I found..."
    
    menu:
        "Tell me more!":
            john "There's an ancient treasure hidden in the forest!"
            john "Will you help me find it?"
            jump adventure_start
        
        "That sounds dangerous...":
            john "You might be right. We should be careful."
            jump adventure_start

label storyline_2:
    narrator "After a moment of awkward silence..."
    john "I understand. But I really could use some help."
    john "There's something I need to find, and I can't do it alone."
    
    john "Will you reconsider?"
    
    menu:
        "Okay, I'll help":
            john "Thank you! You won't regret this!"
            jump adventure_start
        
        "No, sorry":
            john "I understand... goodbye then."
            narrator "John walks away sadly."
            jump ending_sad

label adventure_start:
    narrator "You and John head toward the forest."
    narrator "The trees are tall and the path is mysterious..."
    
    john "According to the map, the treasure is somewhere near the old temple."
    
    menu:
        "Head left toward the mountains":
            narrator "You choose the mountain path..."
            narrator "After hours of hiking, you find ancient ruins!"
            jump treasure_found
        
        "Head right along the river":
            narrator "You follow the river downstream..."
            narrator "It leads to a hidden waterfall!"
            narrator "Behind it... ancient markings on the rocks!"
            jump treasure_found
        
        "Continue straight ahead":
            narrator "You push through dense vegetation..."
            narrator "Suddenly, you spot the old temple!"
            jump temple_encounter

label temple_encounter:
    narrator "The temple is covered in vines and moss."
    narrator "It looks ancient and mysterious."
    
    john "This must be it! The treasure should be inside!"
    
    menu:
        "Enter the temple carefully":
            narrator "You step inside slowly..."
            narrator "Your eyes adjust to the darkness..."
            narrator "There, in the center of the main chamber..."
            narrator "You see a golden chest!"
            jump treasure_found
        
        "Look around the outside first":
            narrator "You search the temple exterior..."
            narrator "You find a secret entrance!"
            narrator "It leads directly to an underground chamber!"
            jump treasure_found

label treasure_found:
    narrator "You found the treasure!"
    narrator "It's even more beautiful than you imagined."
    
    john "We did it! Together!"
    john "I couldn't have done this without you!"
    
    narrator "John puts his hand on your shoulder."
    john "Thank you, my friend. You're braver than anyone I know."
    
    narrator "The treasure will bring great fortune to your village."
    narrator "And you and John become legendary heroes!"
    
    jump ending_good

label ending_good:
    narrator "---"
    narrator "THE END"
    narrator "---"
    narrator "Thanks for playing MyGame!"
    narrator ""
    narrator "You helped John find the treasure and became heroes!"
    return

label ending_sad:
    narrator "---"
    narrator "THE END"
    narrator "---"
    narrator "John never found the treasure..."
    narrator "But perhaps that's not what matters most."
    narrator ""
    narrator "Thanks for playing MyGame!"
    return