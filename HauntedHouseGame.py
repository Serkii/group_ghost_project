# Haunted-house-game-in-python

# NOTE: 
# This game was created based on the book: Write Your Own Adventure Programs
# Written by Jenny Tyler, Les Howarth
# Published by Usborne computer books, 1983
# https://books.google.co.nz/books?id=f6BoAAAACAAJ

import random
import sys
import string

#############################################################################################################
# GAME DATA                                                                                                 #
#############################################################################################################

# SOME CONSTANTS
HERO_INVENTORY_POS = 999 ##Global Value##

DirectionsList = ['SE', 'WE',  'WE',  'SWE', 'WE',   'WE',  'SWE',  'WS', #0-7
                   'NS', 'SE',  'WE',  'NW',  'SE',   'W',   'NE',   'NSW', #8-15
                   'NS', 'NS',  'SE',  'WE',  'NW', 'SE',  'WS', 'NS', #16-23
                   'N',  'NS',  'NSE',  'WE',  'WE',   'NSW', 'NS',   'NS', # 24 - 31
                   'S',  'NSE', 'NSW', 'S',   'NS', 'N',   'N',    'NS', #32 - 39
                   'NE', 'NSW',  'NE',  'W',   'NSE',  'WE',  'W',    'NS', #40 - 47
                   'SE', 'NSW', 'E',   'WE',  'NW',   'SE',   'SWE',   'NW', #48 - 55
                   'NE', 'NWE', 'WE',  'WE',  'WE',   'NWE', 'NWE',  'W'] #56 - 63

##Global Value##

# '\' below is a continuation character, it tells Python that the current statement continues to the next line.
LocationsList = \
[ 'DARK CORNER',                  'OVERGROWN GARDEN',       'BY LARGE WOODPILE',         'YARD BY RUBBISH',
  'WEEDPATCH',                    'FOREST',                 'THICK FOREST',              'BLASTED TREE',
  'CORNER OF HOUSE',              'ENTRANCE TO KITCHEN',    'KITCHEN & GRIMY COOKER',    'SCULLERY DOOR',
  'ROOM WITH INCHES OF DUST',     'REAR TURRET ROOM',       'CLEARING BY HOUSE',         'PATH',
  'SIDE OF HOUSE',                'BACK OF HALLWAY',        'DARK ALCOVE',               'SHALL DARK ROOM',
  'BOTTOM OF SPIRAL STAIRCASE',   'WIDE PASSAGE',           'SLIPPERY STEPS',            'CLIFFTOP',
  'NEAR CRUMBLING WALL',          'GLOOMY PASSAGE',         'POOL OF LIGHT',             'IMPRESSIVE VAULTED HALLWAY',
  'HALL BY THICK WOODEN DOOR',    'TROPHY ROOM',            'CELLAR WITH BARRED WINDOW', 'CLIFF PATH',
  'CUPBOARD WITH HANGING COAT',   'FRONT HALL',             'SITTING ROOM',              'SECRET ROOM',
  'STEEP MARBLE STAIRS',          'DINING ROOM',            'DEEP CELLAR WITH COFFIN',   'CLIFF PATH',
  'CLOSET',                       'FRONT LOBBY',            'LIBRARY OF EVIL BOOKS',   'STUDY WITH DESK & HOLE IN WALL',
  'WEIRD COBWEBBY ROOM',          'VERY COLD CHAMBER',      'SPOOKY ROOM',               'CLIFF PATH BY MARSH',
  'RUBBLE-STREWN VERANDAH',       'FRONT PORCH',            'FRONT TOWER',               'SLOPING CORRIDOR',
  'UPPER GALLERY',                'MARSH BY WALL',          'MARSH',                     'SOGGY PATH',
  'BY TWISTED RAILING',           'PATH THROUGH IRON GATE', 'BY RAILINGS',               'BENEATH FRONT TOWER',
  'DEBRIS FROM CRUMBLING FACADE', 'LARGE FALLEN BRICKWORK', 'ROTTING STONE ARCH',        'CRUMBLING CLIFFTOP']

## Add 'QUIT', 'IWANTIT', 'CLEAN','MAGICMAP', 'JETMOVE' in VerbList. JETMOVE is a cheat action, user will find it when he get scroll successfully.##
VerbList = ['HELP', 'CARRYING?', 'GO',    'N',       'S',       'W',     'E',   'U',      'D',
            'GET',  'TAKE',      'OPEN',  'EXAMINE', 'READ',    'SAY',
            'DIG',  'SWING',     'CLIMB', 'LIGHT',   'UNLIGHT', 'SPRAY', 'USE', 'UNLOCK', 'DROP', 'SCORE', 'QUIT', 'IWANTIT', 'CLEAN','MAGICMAP', 'JETMOVE']##Global Value##
# These list may be useful in the future
#NounList = ['NORTH',   'SOUTH',  'WEST',   'EAST',    'UP',   'DOWN',
#            'DOOR',    'BATS',   'GHOSTS', 'X2ANFAR', 'SPELLS', 'WALL']

#PropList = ['DRAWER',  'DESK', 'COAT', 'RUBBISH', 'COFFIN', 'BOOKS']

#PositionOfProps = [43, 43, 32, 3, 38, 35]

ItemList = ['PAINTING', 'RING',      'MAGIC SPELLS', 'GOBLET', 'SCROLL', 'COINS', 'STATUE',  'CANDLESTICK', 'MATCHES',
            'VACUUM',   'BATTERIES', 'SHOVEL',       'AXE',    'ROPE',   'BOAT',  'AEROSOL', 'CANDLE',      'KEY', 'CABINET', 'MAGICWINE']

PositionOfItems = [46, 38, 35, 50, 13, 18, 28, 42, 10, 25, 26, 4, 2, 7, 47, 60, 100, 100, 37, 100]##Global Value##

VisitedLocations =[0]##Global Value##

## Task 8
## MIssion 1: Kill the monster in place 39 and get a secret number.##
SecretNumber = ""
MonsterList = ["Goblin Piker"]
MosterLocation = [39]

quitthegame = False




#############################################################################################################
# HELPER FUNCTIONS                                                                                          #
#############################################################################################################


def isMultiwordStatement(value):
    return value.find(" ") != -1

def isItemAvailableAtLocation(ItemID, currentLocation):
    return PositionOfItems[ItemID] == currentLocation

def isItemInInventory(itemName):
    ItemID = GetItemID(itemName)
    return PositionOfItems[ItemID] == HERO_INVENTORY_POS

def isItemHidden(itemName):
    # 100 is the location for hidden items. 
    ItemID = GetItemID(itemName)
    return PositionOfItems[ItemID] == 100

def GetItemID(item):
    for ItemID in range(0, len(ItemList), 1):
        if item == ItemList[ItemID]:
            return ItemID
    return -1


def contains(validValues, values):
    """
    Function: contains
    validValues: a string containing all the valid characters allowed
    values: a string that need to be checked (to see whether it contains only valid characters)
    """
    validCount = 0
    lengthValues = len(values)
    for letter in validValues:
        for character in values:
           if letter == character:
                validCount=validCount+1
    return validCount == lengthValues


def isAlphabetic(value):
    alphabeticCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return contains(alphabeticCharacters, value)

def isValidName(value):
    alphabeticCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ &-"
    return contains(alphabeticCharacters, value)



#############################################################################################
# GAME LOGIC                                                                                #
#############################################################################################

def GetVerbFromSentence(sentence):
    if not isMultiwordStatement(sentence):
        return sentence
    locationOfSpace=sentence.find(" ")
    return sentence[:locationOfSpace]

def GetNounFromSentence(sentence):
    if not isMultiwordStatement(sentence):
        return ""
    locationOfSpace=sentence.find(" ") + 1
    return sentence[locationOfSpace:]



def isMovementAvailable(directioncharacter, currentLocation):
    """
    isMovementAvailable checks whether it is possible to move in a direction in the current location


    directioncharacter - intended direction to move toward at the currentLocation
    returns True or False - based on whether the directioncharacter can be found in the String from DirectionsList[currentLocation]

    Example: 
    if directioncharacter is 'N' and DirectionsList[currentLocation] is 'NSW', this function returns True
    """
    
    dirString = DirectionsList[currentLocation]
    result = dirString.find(directioncharacter)
    if result >= 0:
        return True
    else:
        return False
    

def isMovementVerb(verb, noun):
    return verb == 'N' or verb == 'S' or verb == 'E' or verb == 'W' or verb == 'U' or verb == 'D' or verb == 'GO'

def GetMovementDirection(statement):
    verb=GetVerbFromSentence(statement)
    noun=GetNounFromSentence(statement)
    if len(verb)==1:
        return verb
    if verb == 'GO':
        return noun[:1]
    return ''

def isEndOfGame(score, currentLocation):
    return score == 5 and currentLocation == 0

def GetScore():
    score = 0
    for name in ItemList:
        if isItemInInventory(name):
            score +=1
    return score

## From week 10 exercise ##
def clearLocationHistory():
    global VisitedLocations
    VisitedLocations = []
    VisitedLocations.append(0)


## Task 6 & 7, create new start meue and add loadgame and savegame functions.##
def SaveLocation():
    f = open("SaveLocation.txt",'w')
    for i in VisitedLocations:
        f.write(str(i)+"\n")
    f.close()

def SaveCurrentLocation(currentLocation):
    fo = open("SaveCurrentLocation", 'w')
    fo.write(str(currentLocation))
    fo.close()


def LoadLocation():
    global VisitedLocations
    VisitedLocations=[]
    f = open('SaveLocation.txt','r')
    for x in f:
        y = x.strip()
        VisitedLocations.append(int(y))
    f.close()

def LoadCurrentLocation():
    fo = open("SaveCurrentLocation", 'r')
    currentLocation = int(fo.read())
    fo.close()
    return currentLocation

def SaveItems():
    global PositionOfItems
    f = open("SaveItems",'w')
    for number in PositionOfItems:
        f.write(str(number)+"\n")
    f.close()

def LoadItems():
    global PositionOfItems
    PositionOfItems = []
    f = open("SaveItems", 'r')
    for number in f:
        PositionOfItems.append(int(number))
    f.close()
############################################################

## Task 2, add QuitGame function to quit the game.##
def QuitGame():
    print("Do you really want to quit Game?")
    exitKey = input("Please input Y or N: ").upper()

    while exitKey != "Y":
        if exitKey == "N":
            print("Game has been resumed")
            return
        else:
            exitKey = input("Sorry, Please input Y or N: ").upper()

    print("""
***************************************
*Thank you for visiting Haunted House!*
*       See you in next adventure!    *
*         Enter any key to quit__     *
***************************************""")
    input()
    global quitthegame
    quitthegame = True





    
#############################################################################################
# END GAME LOGIC                                                                            #
#############################################################################################

#############################################################################################
# BEGIN PRESENTATION LOGIC                                                                  #
#############################################################################################

def DisplayCongratulation():
    print("""
 __     __                    _       
 \ \   / /                   (_)      
  \ \_/ /__  _   _  __      ___ _ __  
   \   / _ \| | | | \ \ /\ / / | '_ \ 
    | | (_) | |_| |  \ V  V /| | | | |
    |_|\___/ \__,_|   \_/\_/ |_|_| |_|
                                      
 """)                                     
def DisplayHelpMessage():
    print("I UNDERSTAND THE FOLLOWING WORDS:") ##Task 1, improve the format of "help" ##
    print(VerbList)
    print("""
[HOW TO WIN?]
Find out 5 inventories (5 marks) and back to the start place (place 0).

HELP                   -  Display all possible action you can carry out in this game.
CARRYIG                -  Display your inventory.
N, S, W, E             -  Tell the game your next movement.
QUIT                   -  Quit the game.
SHOW MAP               -  Display the map.
CLEAN                  -  Clean your location history.
GET or TAKE ITEM       -  Get object from the ground.
DROP ITEM              -  Drop items.
SCORE                  -  Display your current score.
OPEN DOOR              -  Open a hidden door(if there is one).
EXMINE ITEM            -  Examine hidden items.
DIG                    -  Dig on th ground.

MAGICMAP               -  A magic to show you an entire map.

Use READ, SAY, DIG, SWING, CLIMB, LIGHT, UNLIGHT, SPRAY and other hidden actions to explore the game. Have Fun! 
""")
    
    
def DisplayInventory():
    strItems=""
    for i in range(len(PositionOfItems)):
        if PositionOfItems[i] == HERO_INVENTORY_POS:
            strItems = strItems + " "+ ItemList[i]
    
    if len(strItems) == 0:
        strItems = "NOTHING"
    print("YOU ARE CARRYING:" + strItems)
    
def DisplayMagicMessage(currentLocation, newLocationID) :
    print ("YOU UTTER WORDS OF DARK MAGIC... X2ANFAR!")
    print ("YOU DISAPPEAR AND REAPPEAR IN ANOTHER LOCATION...")
    print ("YOU WERE IN " + LocationsList[currentLocation])
    print ("YOU ARE NOW IN " + LocationsList[newLocationID])



def DisplayMap(curentLocation):

    """
     Each row of the map is consisted of 3 lines
     The first line - contains exit to North
     The second line - contains exits to West and East plus room no.
     The third line - contains exit to South
     
    """
    Line1 = ""
    Line2 = ""
    Line3 = ""
    # Use a FOR loop to draw every room

    for Index in range (0, 64, 1):
        if Index in VisitedLocations:
            # assign the exits at location 'Index' to currentValues
            # e.g. "NSW" if there are exits to North, South, and West
            currentValues=DirectionsList[Index]

            # if there is exit to the north draw a gap between the blocks
            if "N" in currentValues:
                Line1 += "█  █"
            # otherwise, draw a wall
            else:
                Line1 += "████"

            ##Task 5, mark the current location as **.##
            ## IndexCurrent = "**" if Index==location else PrintableInts(Index)##
            if Index == curentLocation:
                IndexCurrent = "**"

            else:
                IndexCurrent=PrintableInts(Index)

            if "W" in currentValues:

                Line2 += (" ") + IndexCurrent
            else:
                Line2 += ("█") + IndexCurrent
            
                
            if "E" in currentValues:
                Line2 += " "
            else:
                Line2 += "█"

            if "S" in currentValues:
                Line3 += "█  █"
            else:
                Line3 += "████"
        else:
            Line1 += "    "
            Line2 += "    "
            Line3 += "    "
        # Draw the first row of rooms if 8 rooms have been processed.     
        if (Index + 1) % 8 == 0:
            print (Line1)
            print (Line2)
            print (Line3)
            # Emptying the lines for the next row of 8 rooms.
            Line1 = ""
            Line2 = ""
            Line3 = ""



## Task 4, create a cheat magic to get any item in the game.##
def MagicHand():
    PossibleItem=[]
    for i in range(0, len(PositionOfItems)-1):
        if PositionOfItems[i] != 999:
            AvailableItem=ItemList[i]
            PossibleItem.append(AvailableItem)
    print("Possible items to get:", PossibleItem)
    WantedItem=input("You have a magic on your hand to get any of them now. So what inventory do you want?").upper()
    if WantedItem not in ItemList:
        print("It is greedy to want something beyond this magic!\nMagic invalid.")
    else:
          WantedItemID=ItemList.index(WantedItem)
          if PositionOfItems[WantedItemID] == HERO_INVENTORY_POS:
              print("You have carried the", WantedItem, "already.")
          else:
              print("YOU ARE NOW CARRYING A",WantedItem, file=sys.stderr)
              PositionOfItems[WantedItemID] = HERO_INVENTORY_POS
###############################################################################################################################


##little cheat to go to any place the user wants.##
def JetMove():
    WantedLocation = int(input("You will use the magic to move to any place. Enter the number of the place you will to go."))
    return WantedLocation
###############################################################################################################################


## From week 10 exercise, cheat for creat an entire map. ##
def beenThere():
    global VisitedLocations
    VisitedLocations = []
    for i in range(0,64):
        VisitedLocations.append(i)
#################################################################################################################################

def ExamineCoat(currentLocation):
    if currentLocation == 32 and isItemHidden("Key"):
        PositionOfItems[GetItemID("KEY")] = 32
        print ("YOU EXAMINE THE COAT AND FIND A KEY IN THE POCKET")
    elif currentLocation == 32 and not isItemHidden("Key"):
        print ("IT\'S A DIRTY OLD COAT")
    else:
        print ("WHAT COAT?")


def ExamineDrawer(currentLocation):
    if currentLocation == 43 and isItemInInventory("KEY") :
        print ("YOU UNLOCK THE DRAWER AND FIND IT IS EMPTY")
    elif currentLocation == 43 and not isItemInInventory("KEY") :
        print ("UNFORTUNATELY THE DRAWER IS LOCKED")
    else:
        print ("WHAT DRAWER?")

    

def ExamineRubbish(currentLocation):
    if currentLocation == 3:
        print ("THE RUBBISH IS FILTHY")
    else:
        print ("WHAT RUBBISH?")

def ExamineWall(currentLocation):
    if currentLocation == 43:
        LocationsList[currentLocation] = "STUDY WITH DESK"
        DirectionsList[currentLocation]="NW"
        print ("YOU LOOK AT THE WALL AND DISCOVER IT IS FALSE!\nYOU DISCOVER A NEW EXIT")
    else:
        print ("NO INTERESTING WALLS HERE")

def ExamineDoor(currentLocation):
    if currentLocation == 28 and  isItemInInventory("KEY"):
        DirectionsList[currentLocation]="SEW"
        print ("YOU UNLOCK THE DOOR AND DISCOVER A NEW LOCATION!")
    elif currentLocation == 28 and  not isItemInInventory("KEY"):
        print ("UNFORTUNATELY THE DOOR IS LOCKED")
    else:
        print ("NO INTERESTING DOOR HERE")
    
def ExamineBooks(currentLocation):
    if currentLocation == 42 and isItemHidden("CANDLE"):
        print ("YOU LOOK AT THE BOOKS AND FOUND A CANDLE IN BETWEEN BOOKS!")
        PositionOfItems[GetItemID("CANDLE")] = 42
    elif currentLocation == 42 and not isItemHidden("CANDLE"):
        print ("THE BOOKS LOOK EVIL")
    else:
        print ("NO BOOKS HERE")

##Task 8
## Mission 2, examine cabinet in Dinner Room, and enter the password the one get from Goblin Piker.##
def ExamineCabinet(currentLocation):
    if currentLocation == 37 and isItemHidden("WINE"):
        print("""
There is a treasure in the cabinet, but it seems that the cabinet requires a set of password to open it.
You must beat the monster Goblin Piker in Cliff Path(place 39) to get it.
If you have it then enter it.
You have three chances to try.
""")

        for i in range(0,3):
            EnterPassword = input("Enter the password that you got it from Goblin Piker: ").upper()
            fo = open("SecretNumber", 'r')
            CorrectPassword = fo.readline()
            fo.close()

            if EnterPassword == CorrectPassword:
                print("Your password is match! You are a warrior! And your prize is a bottle of magic wine in it!")
                print("You are carrying a bottle of magic wine!", file=sys.stderr)
                WineIndex = ItemList.index("MAGICWINE")
                PositionOfItems[WineIndex] = HERO_INVENTORY_POS
                break
            else:
                print("It seems that you don't know its password, you will find it in Cliff Path, place 39")


    elif currentLocation == 37 and not isItemHidden("WINE"):
        print("It is just an empty cabinet.")
    else:
        print("No cabinet here.")

####################################################################################################################


def DoExamine(currentLocation, noun) :
    if noun == "COAT":
        ExamineCoat(currentLocation)
    elif noun == "DRAWER":
        ExamineDrawer(currentLocation )
    elif noun == "RUBBISH":
        ExamineRubbish(currentLocation)
    elif noun == "WALL":
        ExamineWall(currentLocation)
    elif noun == "DOOR":
        ExamineDoor(currentLocation)
    elif noun == "BOOKS":
        ExamineBooks(currentLocation)
    elif noun == "CABINET":
        ExamineCabinet(currentLocation)
    else:
        print ("WHAT "+noun+"?")
    
          

def PrintableInts(value):
    if(value<10):
        return " "+str(value) ##if value only one character, than add '' to make it as 2 characters.##
    return str(value)


def Dig(currentLocation):
    if currentLocation == 30 and isItemInInventory("SHOVEL"):
        DirectionsList[currentLocation]="NSE"
        LocationsList[30] = 'HOLE IN WALL'
        print ("YOU DIG AROUND THE ROOM. THE BARS IN THE WINDOW BECOME LOOSE! REVEALLING A NEW EXIT!")
    elif isItemInInventory("SHOVEL"):
        print ("YOU DIG A LITTLE HOLE.")
    else:
        print ("YOU HAVE NOTHING TO DIG WITH")

#############################################################################################
# END PRESENTATION LOGIC                                                                    #
#############################################################################################


def ListItemsAtPosition(currentLocation):
    strItems=""
    for i in range(0, len(PositionOfItems), 1):
        if PositionOfItems[i] == currentLocation:
            strItems = strItems + " "+ ItemList[i]
    return strItems

def ItemsAvailableAtPosition(currentLocation):
    for i in range(0, len(PositionOfItems), 1):
        if PositionOfItems[i] == currentLocation:
            return True
    return False

def GoMagic(currentLocation):
    newLocationID=currentLocation
    while(newLocationID == currentLocation):
           newLocationID = random.randint(0,63)
    return newLocationID

def Go(statement, currentLocation):
    directioncharacter = ''

    verb=GetVerbFromSentence(statement)
    noun=GetNounFromSentence(statement)

    directioncharacter = verb
    if verb == 'GO':
        directioncharacter = noun[:1]
    
    if isMovementAvailable(directioncharacter, currentLocation):
        if directioncharacter == 'N':
            currentLocation -= 8
        elif directioncharacter == 'S':
            currentLocation += 8
        elif directioncharacter == 'W':
            currentLocation -= 1
        elif directioncharacter == 'E':
            currentLocation += 1
    return currentLocation

def GetItem(noun, currentLocation):
    ItemID = GetItemID(noun)
    if isItemAvailableAtLocation(ItemID, currentLocation):
        PositionOfItems[ItemID]=HERO_INVENTORY_POS
        print("YOU ARE NOW CARRYING A",noun, file=sys.stderr)
        if ItemList[ItemID] == "SCROLL":
            print("You have learn a new magic. Enter \"JETMOVE\" to go any room you want! ")
    else:
        print("SORRY YOU CANNOT TAKE A ", noun)
    
        
def DropItem(noun, currentLocation):
    ItemID = GetItemID(noun)
    if isItemAvailableAtLocation(ItemID, HERO_INVENTORY_POS):
        PositionOfItems[ItemID] = currentLocation
        print("YOU HAVE DROPPED THE ", noun)
    else:
        print("YOU CANNOT DROP THAT WHICH YOU DO NOT POSSESS")

def OpenDoor(currentLocation):
    if currentLocation == 28 and isItemInInventory("KEY"):
        DirectionsList[currentLocation]="SEW"
        print("THE DOOR IS NOW OPEN! REVEALLING A NEW EXIT!")
    else:
        print("THE DOOR IS LOCKED")


        
def ProcessStatement(statement, currentLocation):
    '''
      A statement can be either a verb or a verb + a noun
      If a statement is consisted of 1 verb and 1 noun, (separated by a space), it can looks like 'examine desk', 'get axe' ..etc
    '''

    
    verb=GetVerbFromSentence(statement)
    noun=GetNounFromSentence(statement)    

    if verb== "HELP":
        DisplayHelpMessage()

    elif verb == "SCORE":
        print("YOUR CURRENT SCORE IS:", GetScore())

    elif verb == "CARRYING" or verb == "CARRYING?" or verb == "INVENTORY" or verb == "INV":
        DisplayInventory()

    elif verb == "GET" or verb == "TAKE":
        GetItem(noun,currentLocation)

    elif ((verb == "OPEN" or verb == "UNLOCK") and noun == "DOOR") or (verb =="USE" and noun == "KEY"):
        OpenDoor(currentLocation)
        
    elif verb == "DIG" or (verb =="USE" and noun=="SHOVEL"):
        Dig(currentLocation)

    elif verb == "DROP":
        DropItem(noun, currentLocation)

    elif verb == "EXAMINE":
        DoExamine(currentLocation, noun)

    elif verb == "SAY" and noun == "X2ANFAR":
        newLocationID = GoMagic(currentLocation)
        DisplayMagicMessage(currentLocation, newLocationID)
        currentLocation = newLocationID

    elif isMovementVerb(verb, noun):  
        newLocationID = Go(statement, currentLocation)
        if currentLocation != newLocationID:
            print("YOU MOVED FROM " + LocationsList[currentLocation] + " TO " + LocationsList[newLocationID], file=sys.stderr)
        else:
            print("YOU ARE UNABLE TO MOVE IN THAT DIRECTION")
        currentLocation = newLocationID

    ## Task 4, create a cheat magic to get any item in the game.##
    elif verb == 'IWANTIT':
        MagicHand()

    ## Task 2, add QuitGame function to quit the game.##
    elif verb == "QUIT":
        QuitGame()

    ## for week 10 exercise, empty the history.##
    elif verb == "CLEAN":
        clearLocationHistory()
        currentLocation = 0

    ## From week 10 exercise, cheat to show whole map. ##
    elif verb == "MAGICMAP":
        beenThere()

    ## Go any room the user want.##
    elif verb == "JETMOVE":
        currentLocation = JetMove()

    elif verb == "SAVE":
        SaveLocation()
        SaveCurrentLocation(currentLocation)
        SaveItems()
        print("Game has been saved.")

    elif verb == "LOAD":
        LoadLocation()
        currentLocation = LoadCurrentLocation()
        LoadItems()
        print("Your game is loaded.\nYou will start in room", currentLocation,".")


    elif verb == "SHOW" and noun == "MAP" or verb == "SS":
        DisplayMap(currentLocation)




    return currentLocation


## Task 8
## MIssion 1: Kill the monster in place 39 and get a secret number.##
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def DeletMonster(location):
    global MosterLocation
    if location in MosterLocation:
        MonsterIndex = MosterLocation.index(location)
        MosterLocation[MonsterIndex] = -1

        return MosterLocation[MonsterIndex]


def GoblinPiker(location):

    UHP = 100
    MHP = 80

    print("""
ooooooooooooo WARING! oooooooooooo
A goblin piker is in front of you!
    Flight it or you may die!

@@ Kill it and you will get a @@
@@    password and use it     @@
@@    to get a treasure in    @@
@@    Dinning Room, place 37  @@

         Are you ready?
    Enter any key to start
++++++++++++++++++++++++++++++++++
""")
    input()

    print("""
Your HP is 100 now.
Punch its tummy to let it down!
Are you ready? Press any key to give it a punch!
""")
    input()

    while not (UHP <= 0 or MHP <= 0):


            MonsterDamage = random.randint(10,20)
            MHP = MHP - MonsterDamage
            UserDamage = random.randint(0,20)
            UHP = UHP - UserDamage
            print("Monster HP reduced",MonsterDamage,"Your HP reduced",UserDamage)
            print("Your HP is",UHP)
            print("Monster Hp is",MHP)

            if UHP > 0 and MHP > 0:
                input("Dangerous! It is still energic! Press any key to give it another punch!")


            elif MHP <= 0 and UHP > 0:

                print("""
****************************** You Won!! **********************************
         Goblin Piker is bleeding and tell you a password. 
 Now you have a password to get a treasure from Dinning Room, place 37.
                    Press any key to get it!
***************************************************************************
                    """)

                SecretNumber = id_generator()
                print("Do not forget to mark down the password [",SecretNumber,"] or you gonna to forget it!")
                fo = open("SecretNumber", "w")
                fo.write(SecretNumber)
                fo.close()
                DeletMonster(location)


            elif UHP < 0 and MHP > 0:
                print("""
You lost! Try again!
""")
                UHP = 100
                MHP = 80
##############################################################################

##Task8
##MIssion 2: Enter the



def Game(a):
    location = a

    while not isEndOfGame(GetScore(), location) and not quitthegame:
        ## Task 8
        ## MIssion 1: Kill the monster in place 39 and get a secret number.##
        if location in MosterLocation:
            GoblinPiker(location)

        print("========Haunted House=========")
        print("YOU ARE LOCATED IN A ", LocationsList[location], ", place", str(location), ".")

        if ItemsAvailableAtPosition(location):
            print("YOU CAN SEE THE FOLLOWING ITEMS AT THIS LOCATION: ",ListItemsAtPosition(location))
        print("VISIBLE EXITS: ",DirectionsList[location])

        ##Task 3, allow users input lower or upper case.##
        statement = input("WHAT DO YOU WANT TO DO NEXT? ").upper()
        location = ProcessStatement(statement, location)

        if not (location in VisitedLocations):
            VisitedLocations.append(location)

        ##Task 5, mark the current location as **.##
        DisplayMap(location)

    # if userquit == 0:
    global quitthegame
    if not quitthegame:
        DisplayCongratulation()



## Task 6&7, add a new menu to ley user choose "new game", "load game" and "quit", at the start of the game.##

print("""
========Haunted House=========
Welcome to Haunted House!
Please follow the instruction:
Enter "New" to start a New Game, or;
enter "Load" to load the game you have saved, or;
enter "Quit" to quit the game.
""")

def StartMenu(FirstChoice):
    if FirstChoice in ("NEW","LOAD","QUIT"):
        if FirstChoice == "NEW":
            Game(0)

        elif FirstChoice == "LOAD":
            LoadLocation()
            currentLocation = LoadCurrentLocation()
            LoadItems()
            print("Your game is loaded.\nYou will start in room", currentLocation, ".")
            Game(currentLocation)

        elif FirstChoice == "QUIT":
            print("""
    ***************************************
    *Thank you for visiting Haunted House!*
    *       See you in next adventure!    *
    *         Enter any key to quit__     *
    ***************************************""")
            input()

FirstChoice = input("Now, enter the word as the instruction:").upper()

if FirstChoice in ("NEW","LOAD","QUIT"):
    StartMenu(FirstChoice)
while FirstChoice not in ("NEW","LOAD","QUIT"):
    FirstChoice = input("Now, enter the word as the instruction:").upper()
    StartMenu(FirstChoice)

#####################################################################################




