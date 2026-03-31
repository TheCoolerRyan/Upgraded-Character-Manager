#RC 1st, My part of the pseducode


import random
import time
import csv
import ast

#Psuedocode (and now code) for character display functions, point distribution fuction, level up function, main function

#create function display_characters, get dictionary of characters as CHARS
def display_characters(chars):
    #loop through CHARS as CHAR
    print('\nCharacters:')
    for char in chars.keys():
        #display name, class, and level of character represented by CHAR list
        print(f'{char.title()}: level {chars[char][-1]} {chars[char][0]}')

#create function show_character, get character list as CHAR
def show_character(char):
    name=list(char.keys())[0]
    #display name, class, and level of CHAR
    print(f'\n{name.title()}\nLevel {char[name][6]} {char[name][0]}\n')
    #display attribute scores
    print(f'Strength: {char[name][1]}\nSpeed: {char[name][2]}\nIntelligence: {char[name][3]}\n')
    #display skills in CHAR
    print(f'Active skill:\n{list(char[name][4].keys())[0]}: {char[name][4][list(char[name][4].keys())[0]]}\n')
    #display inventory of CHAR
    print('Inventory:')
    for i in char[name][5].keys():
        print(f'{i}:\n{char[name][5][i]}')
    if list(char[name][5].keys())==[]:
        print('Inventory empty.')


def point_holder(total):
    def use_points(amount):
        nonlocal total
        total -= amount
        return total
    return use_points


#create function distribute, get POINTS
def distribute(points):
    #set SCORES to list of three 0s
    get_points=point_holder(points)
    scores=[0,0,0]
    #display you have POINTS points
    print(f'\nYou have {get_points(0)} points.')
    #get (valid) user input for how many points to put into strength
    while True:
        try:
            scor=int(simple(input('\nHow many points do you want to put into strength? ')))
            if points-scor >=0 and scor>=0:
            #subtract that number from POINTS
                get_points(scor)
            else:
                print('\nInvalid input. Try again.')
                continue
            break
        except:
            print('\nInvalid input, try again.')
    #add that number of points to first in SCORES
    scores[0]+=scor
    #display you have POINTS points
    print(f'\nYou have {get_points(0)} points remaining.')
    #get (valid) user input for how many points to put into speed
    while True:
        try:
            scor=int(simple(input('\nHow many points do you want to put into speed? (The remaining points will go into intelligence) ')))
            if points-scor >=0 and scor>=0:
            #subtract that number from POINTS
                get_points(scor)
            else:
                print('\nInvalid input. Try again.')
                continue
            break
        except:
            print('\nInvalid input, try again.')
    #add that number of points to second in SCORES
    scores[1]+=scor
    #display you have POINTS points put into intelligence
    print(f'\nThe remaining {get_points(0)} points go into intelligence.')
    #add POINTS to third in SCORES
    scores[2]+=get_points(0)
    #return SCORES
    return scores[0],scores[1],scores[2]



#create function level_up, get character list as CHAR, get skills as SKILLS
def level_up(char,skills):
    def modify(indx,new):
        char[name][indx]=new
    name=list(char.keys())[0]
    #if CHAR is second level
    if char[name][6]==2:
        #display character is max level
        print(f'\n{name} is max level.')
        #return CHAR
        return char
    #set CHAR level to 2
    modify(6,2)
    #add function distribute called on random number between 5 and 10 to CHAR scores
    distr=distribute(random.randint(5,10))
    for i in range(3):
        modify(i+1,distr[i])
    #display all skills in SKILLS that are for CHAR class
    print('\nSkills Avaliable:')
    for i,x in skills[char[name][0]].items():
        print(f'{i}: {x}')
    #set skill in CHAR to (valid) user input for which skill they want
    skil=simple(input('\nWould you like to use the first or the second skill?(1/2) '))
    while skil not in ['1','2']:
        print('\nInvalid input. Try again.')
        skil=simple(input('\nWould you like to use the first or the second skill?(1/2) '))
    if skil=='1':
        modify(4,{list(skills[char[name][0]].keys())[0]:skills[char[name][0]][list(skills[char[name][0]].keys())[0]]})
    elif skil=='2':
        modify(4,{list(skills[char[name][0]].keys())[1]:skills[char[name][0]][list(skills[char[name][0]].keys())[1]]})
    #return CHAR
    return char


#make a funtion create
def create(characters,skills):
    #make the user choose a name, and add it t the character dictionary as a key 
    name = simple(input("What would you wish your character name to be?: "))
    characters[name] = ['',0,0,0,{'name':'description'},{},1]
    #create a while loop
    while True:
    #make class equals input what their character class is going to be, with numbers to be easier, and stupid profe
        clas = input("\nPlease select the class you want to choose\n1:Archer\n2:Knight\n3:Wizard\n")
        if clas == "1" or clas == "2" or clas == "3":
            break
        else:
            print("Select again")
            continue
    if clas == "1":
        clas='archer'
        #add class to character information
        characters[name][0] = clas
    elif clas == "2":
        clas='knight'
        #add class to character information
        characters[name][0] = clas
    elif clas == "3":
        clas='wizard'
        #add class to character information
        characters[name][0] = clas
    #print stats
    print("\nYour stats are:\nStrength\nSpeed\nIntelligence")
    #add stats to character information
    characters[name][1], characters[name][2],characters[name][3] = distribute(random.randint(5,10))
    #print skill and say that to unlock another one they need to level up
    print("\nYou have one skill right now, but if you level up, you will unlock more")
    #add skill to character information
    characters[name][4]={list(skills[clas].keys())[0]:skills[clas][list(skills[clas].keys())[0]]}
    #return chaacter dictionary
    return characters


#Start off the search function (Take in the dictionary containing all of the characters):
def search(characters):
    char = {}
    #Put into a loop to make sure that the input is one of the options
    while True:
        #Take their input on wether they want to search by name level or skill
        option = simple(input("Would you like to search by name, level, or class?:"))
        #Check to see if its one of them, if it is break
        if option == "name" or option == "level" or option == "class":
            break
        else:
            print("That is not an option...")

    #Check to see which one of the three options it is

    #If it is a name, have them input the name they want and print out all characters that have that name
    check = False
    while True:
        if option == "name":
            #Allow them to select one of the characters and set that to a variable
            name = simple(input("Please tell me the characters name:"))
            if name in characters:
                char[name] = characters[name]
                break
            else:
                print("That character dosen't exist...")
        else:
            break
        

    #If it is a class, have them input the class they want and print out all characters that have that class
    while True:
        if option == "class":
            available = []
            #Allow them to select one of the characters and set that to a variable
            clas = simple(input("Please tell me the class:"))
            if clas == "archer" or clas == "knight" or clas == "wizard":
                for value in characters.values():
                    if list(value)[0] == clas:
                        check = True
                    else:
                        pass
                if check == True:
                    for key,value in characters.items():
                        if value[0] == clas:
                            available.append([key,value])
                        else:
                            pass
                    x = 1                   
                    for info in available:
                        print(f'{x}. {info[0].title()}: level {info[1][-1]} {info[1][0]}')
                        x += 1
                    while True:
                        pick = input("Which character would you like to select? (Please type the number):").strip()
                        if pick.isdigit() == True and int(pick) >0 and int(pick) < x:
                            pick = int(pick)
                            pick -= 1
                            break
                        else:
                            print("That is not a valid option (Its not one of the numbers listed)")
                    char[available[pick][0]] = characters[available[pick][0]]
                    break
                else:
                    print("You don't have a character with that class...")
            else:
                print("That is not a class...")
        else:
            break

    #If it is a level, have them input the level they want and print out all characters that have that level
    while True:
        if option == "level":
            available = []
            #Allow them to select one of the characters and set that to a variable
            level = input("Please tell me the level:").strip()
            if level == "1" or level == "2":
                level = int(level)
                for value in characters.values():
                    if list(value)[6] == level:
                        check = True
                    else:
                        pass
                if check == True:
                    for key,value in characters.items():
                        if value[6] == level:
                            available.append([key,value])      
                        else: 
                            pass
                    x = 1                        
                    for info in available:
                        print(f'{x}. {info[0].title()}: level {info[1][-1]} {info[1][0]}')
                        x += 1
                    while True:
                        pick = input("Which character would you like to select? (Please type the number):").strip()
                        if pick.isdigit() == True and int(pick) >0 and int(pick) < x:
                            pick = int(pick)
                            pick -= 1
                            break
                        else:
                            print("That is not a valid option (Its not one of the numbers listed)")
                    char[available[pick][0]] = characters[available[pick][0]]
                    break
                else:
                    print("You don't have a character with that level")
            else:
                print("That is not a level...")
        else:
            break
    #Return variable
    return char


#Create a function to allow them to change stats
def change(character):
    cname=list(character.keys())[0]
    #Display all of the main stats (Strength, speed, and intelligence) and there scores.
    strength = character[cname][1]
    speed = character[cname][2]
    intelegence = character[cname][3]
    print(f"Strength: {strength}\nSpeed: {speed}\nIntelegence: {intelegence}")
    #Ask them what is the first one they want to swap
    while True:
        #Get valid inputs
        #assign both of them to base things, 1 or 2
        first = simple(input("What is the first stat that you want to swap?:"))
        if first == "strength" or first == "speed" or first == "intelegence":
            break
        else: 
            print("That is not an option...")
    #Ask them what is the second one they want to swap
    while True:
        #Get valid inputs
        #assign both of them to base things, 1 or 2
        second = simple(input("What is the second stat that you want to swap?:"))
        if second == "strength" or second == "speed" or second == "intelegence":
            if second != first:
                break
            else:
                print("I guess you can switch it with itself???")
                break
        else: 
            print("That is not an option...")
    #Then set first choose = to variable 2
    if first == "strength":
        x = 1
    elif first == "speed":
        x = 2
    else:
        x = 3

    if second == "strength":
        y = 1
    elif second == "speed":
        y = 2
    else:
        y = 3

    #Set first choice = variable 1
    value_one = character[cname][x] 
    #Set second choice = variable 1
    value_two = character[cname][y]
    character[cname][x] = value_two
    character[cname][y] = value_one

    #Display new stats
    strength = character[cname][1]
    speed = character[cname][2]
    intelegence = character[cname][3]
    print(f"Strength: {strength}\nSpeed: {speed}\nIntelegence: {intelegence}")
    #Return main dictionary
    return character


#Create a function to allow them to change there skill
def skill(character):
    cname=list(character.keys())[0]
    #Create a dictionary of skills for there class and what they do
    skills={'archer':{'Snipe':'Ranged weapon range is doubled','Pierce Armor':'Double damage    of ranged weapons.'},
            'knight':{'Parry':'Use a melee attack to negate an enemy\'s next attack','Disarm':'Use a melee attack to remove an enemy\'s weapon.'},
            'wizard':{'Quick Spell':'Cast two spells as one attack.','Change Spell':'Use melee spell attacks as ranged spell attacks, and ranged spell attacks as melee spell attacks.'}}
    #Take there characters class and print of the skills that are allowed for that class and there level required
    available = skills[list(character.values())[0][0]]
    x = 1
    for key,value in available.items():
        print(f"Level {x}. {key}: {value}")
        x += 1
    #Put it into a while loop to make sure they choose something available
    while True:
        #Ask them what of the two skills they want to use
        while True:
            choice = input("Which skill do you want to select? (Please put 1 or 2)").strip()
            if choice == "1" or choice == "2":
                break
            else:
                print("That is incorrect formating.")
        #Check to see if the skills exitst and if they have met the level requirements
        if choice == "1":
            skl = {list(available.keys())[0]:available[list(available.keys())[0]]}
            break
        #If all of the requirements are met, change there skill and return the dictionary containing everything
            #Then break
        elif choice == "2" and character[cname][6] >1:
            skl = {list(available.keys())[1]:available[list(available.keys())[1]]}
            break
        #Otherwise have them chose again until they select something that works
        else:
            print('You do not meet the requirements for this skill.')
            #Then break
    character[cname][4] = skl
    return character

#Create a function for inventory
def inventor(character):
    cname=list(character.keys())[0]
    #Create a while loop for there choice
    while True:
        #ask them if they want to create a weapon or remove a weapon
        answer = simple(input("Would you like to create a weapon or destroy a weapon? (Please put c or d)"))
        #If there input equals create or remove, then break
        if answer == "c":
            break
        elif answer == "d" and character[cname][5] != {}:
            break
        #Else have continue
        else:
            print("That is not a correct option, please put c or d. If its d, make sure you have weapons to destroy. (C for create, d for destroy)...")

    #Check to see which of the choices they choose

    #If they chose to add an item, let them create its name and its description, adding it to the dictionary
    if answer == "c":
        name = simple(input("What is the name of this item?:"))
        description = simple(input("What is the description of this weapon?:"))
        character[cname][5][name] = description
    #If they chose to remove an item, create a for loop that will print of the name and the description
    else:
        x = 1
        names = []
        for key,value in character[cname][5].items():
            print(f"{x}. {key}: {value}")
            x += 1
            names.append(key)
    #Get valid user input
        while True:
            choice = simple(input("Which of the weapons do you want to remove? (Please put only the weapon name):"))
            if choice in names:
                break
            else:
                print(f"{choice} is not an option...")
    #Remove the choosen weapon
        del character[cname][5][choice]
    #Return the main dictionary
    return character


#Save and pull functions
def save(characters):
    try:
        filename = 'C:/Users/ryan.crop/Documents/Upgraded-Character-Manager/.docs/character_data.csv'
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Write a header row for clarity
            writer.writerow(['Name', 'Data'])
            for name, data_list in characters.items():
                # Convert the list to a string before writing
                writer.writerow([name, str(data_list)])
    except:
        print("There are no characters...")


def pull():
    characters = {}
    with open("C:/Users/ryan.crop/Documents/Upgraded-Character-Manager/.docs/character_data.csv", mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        # Skip header if necessary
        # next(reader)
        
        for row in reader:
            # Assuming format: name, data_list
            char_name = row[0]
            # Convert string representation of list/dict into actual objects
            try:
                char_data = ast.literal_eval(row[1]) 
                characters[char_name] = char_data
            except (ValueError, SyntaxError) as e:
                print(f"Error parsing row for {char_name}: {e}")
                
    return characters


#Simmplyfiying
def simple(input):
    input = (input).strip().lower()
    return input