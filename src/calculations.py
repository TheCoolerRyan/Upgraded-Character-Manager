import random
import csv
import ast

class Characters:
    @staticmethod
    def display_characters(chars):
        print('\nCharacters:')
        for char in chars.keys():
            print(f'{char.title()}: level {chars[char][-1]} {chars[char][0]}')

    @staticmethod
    def show_character(char):
        name = list(char.keys())[0]
        print(f'\n{name.title()}\nLevel {char[name][6]} {char[name][0]}\n')
        print(f'Strength: {char[name][1]}\nSpeed: {char[name][2]}\nIntelligence: {char[name][3]}\n')
        print(f'Active skill:\n{list(char[name][4].keys())[0]}: {char[name][4][list(char[name][4].keys())[0]]}\n')
        print('Inventory:')
        for i in char[name][5].keys():
            print(f'{i}:\n{char[name][5][i]}')
        if list(char[name][5].keys()) == []:
            print('Inventory empty.')

    @staticmethod
    def level_up(char, skills):
        def modify(indx, new):
            char[name][indx] = new
        name = list(char.keys())[0]
        if char[name][6] == 2:
            print(f'\n{name} is max level.')
            return char
        modify(6, 2)
        distr = Create.distribute(random.randint(5, 10))
        for i in range(3):
            modify(i + 1, distr[i])
        print('\nSkills Available:')
        for i, x in skills[char[name][0]].items():
            print(f'{i}: {x}')
        skil = input('\nWould you like to use the first or the second skill?(1/2) ')
        while skil not in ['1', '2']:
            print('\nInvalid input. Try again.')
            skil = input('\nWould you like to use the first or the second skill?(1/2) ')
        if skil == '1':
            modify(4, {list(skills[char[name][0]].keys())[0]: skills[char[name][0]][list(skills[char[name][0]].keys())[0]]})
        elif skil == '2':
            modify(4, {list(skills[char[name][0]].keys())[1]: skills[char[name][0]][list(skills[char[name][0]].keys())[1]]})
        return char

    @staticmethod
    def search(characters):
        char = {}
        while True:
            option = input("Would you like to search by name, level, or class?:")
            if option in ['name', 'level', 'class']:
                break
            else:
                print("That is not an option...")

        check = False
        while True:
            if option == "name":
                name = input("Please tell me the character's name:")
                if name in characters:
                    char[name] = characters[name]
                    break
                else:
                    print("That character doesn't exist...")
            else:
                break

        while True:
            if option == "class":
                available = []
                clas = input("Please tell me the class:")
                if clas in ['archer', 'knight', 'wizard']:
                    for value in characters.values():
                        if value[0] == clas:
                            check = True
                    if check:
                        for key, value in characters.items():
                            if value[0] == clas:
                                available.append([key, value])
                        x = 1
                        for info in available:
                            print(f'{x}. {info[0].title()}: level {info[1][-1]} {info[1][0]}')
                            x += 1
                        while True:
                            pick = input("Which character would you like to select? (Please type the number):").strip()
                            if pick.isdigit() and 0 < int(pick) < x:
                                pick = int(pick) - 1
                                break
                            else:
                                print("That is not a valid option.")
                        char[available[pick][0]] = characters[available[pick][0]]
                        break
                    else:
                        print("You don't have a character with that class...")
                else:
                    print("That is not a class...")
            else:
                break

        while True:
            if option == "level":
                available = []
                level = input("Please tell me the level:").strip()
                if level in ["1", "2"]:
                    level = int(level)
                    for value in characters.values():
                        if value[6] == level:
                            check = True
                    if check:
                        for key, value in characters.items():
                            if value[6] == level:
                                available.append([key, value])
                        x = 1
                        for info in available:
                            print(f'{x}. {info[0].title()}: level {info[1][-1]} {info[1][0]}')
                            x += 1
                        while True:
                            pick = input("Which character would you like to select? (Please type the number):").strip()
                            if pick.isdigit() and 0 < int(pick) < x:
                                pick = int(pick) - 1
                                break
                            else:
                                print("That is not a valid option.")
                        char[available[pick][0]] = characters[available[pick][0]]
                        break
                    else:
                        print("You don't have a character with that level")
                else:
                    print("That is not a level...")
            else:
                break
        return char

    @staticmethod
    def change(character):
        cname = list(character.keys())[0]
        print(f"Strength: {character[cname][1]}\nSpeed: {character[cname][2]}\nIntelligence: {character[cname][3]}")
        while True:
            first = input("What is the first stat that you want to swap?:")
            if first in ['strength', 'speed', 'intelegence']:
                break
            else:
                print("That is not an option...")
        while True:
            second = input("What is the second stat that you want to swap?:")
            if second in ['strength', 'speed', 'intelegence']:
                if second != first:
                    break
                else:
                    print("I guess you can switch it with itself???")
                    break
            else:
                print("That is not an option...")
        x = 1 if first == 'strength' else 2 if first == 'speed' else 3
        y = 1 if second == 'strength' else 2 if second == 'speed' else 3
        value_one = character[cname][x]
        value_two = character[cname][y]
        character[cname][x] = value_two
        character[cname][y] = value_one
        print(f"Strength: {character[cname][1]}\nSpeed: {character[cname][2]}\nIntelligence: {character[cname][3]}")
        return character

    @staticmethod
    def skill(character):
        cname = list(character.keys())[0]
        skills = {
            'archer': {'Snipe': 'Ranged weapon range is doubled', 'Pierce Armor': 'Double damage of ranged weapons.'},
            'knight': {'Parry': "Use a melee attack to negate an enemy's next attack", 'Disarm': "Use a melee attack to remove an enemy's weapon."},
            'wizard': {'Quick Spell': 'Cast two spells as one attack.', 'Change Spell': 'Use melee spell attacks as ranged spell attacks, and ranged spell attacks as melee spell attacks.'}
        }
        available = skills[character[cname][0]]
        x = 1
        for key, value in available.items():
            print(f"Level {x}. {key}: {value}")
            x += 1
        while True:
            choice = input("Which skill do you want to select? (Please put 1 or 2)").strip()
            if choice in ['1', '2']:
                break
            else:
                print("That is incorrect formatting.")
        if choice == '1':
            skl = {list(available.keys())[0]: available[list(available.keys())[0]]}
        elif choice == '2' and character[cname][6] > 1:
            skl = {list(available.keys())[1]: available[list(available.keys())[1]]}
        else:
            print('You do not meet the requirements for this skill.')
            return character
        character[cname][4] = skl
        return character

    @staticmethod
    def inventor(character):
        cname = list(character.keys())[0]
        while True:
            answer = input("Would you like to create a weapon or destroy a weapon? (Please put c or d)")
            if answer in ['c', 'd']:
                break
            else:
                print("That is not a correct option.")
        if answer == 'c':
            name = input("What is the name of this item?:")
            description = input("What is the description of this weapon?:")
            character[cname][5][name] = description
        else:
            x = 1
            names = []
            for key, value in character[cname][5].items():
                print(f"{x}. {key}: {value}")
                x += 1
                names.append(key)
            while True:
                choice = input("Which of the weapons do you want to remove? (Please put only the weapon name):")
                if choice in names:
                    break
                else:
                    print(f"{choice} is not an option...")
            del character[cname][5][choice]
        return character

    @staticmethod
    def save(characters):
        try:
            filename = 'C:/Users/ryan.crop/Documents/Upgraded-Character-Manager/.docs/character_data.csv'
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'Data'])
                for name, data_list in characters.items():
                    writer.writerow([name, str(data_list)])
        except:
            print("There are no characters...")

    @staticmethod
    def pull():
        try:
            characters = {}
            with open("C:/Users/ryan.crop/Documents/Upgraded-Character-Manager/.docs/character_data.csv", mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    char_name = row[0]
                    try:
                        char_data = ast.literal_eval(row[1])
                        characters[char_name] = char_data
                    except (ValueError, SyntaxError) as e:
                        print(f"Error parsing row for {char_name}: {e}")
        except:
            print("Probably just the fact that I pull from my file and not the home computers...")                        
        return characters


class Create:
    @staticmethod
    def distribute(points):
        def use_points(amount):
            nonlocal total
            total -= amount
            return total
        total = points
        scores = [0, 0, 0]
        print(f'\nYou have {total} points.')
        while True:
            try:
                scor = int(input('\nHow many points do you want to put into strength? '))
                if total - scor >= 0 and scor >= 0:
                    use_points(scor)
                else:
                    print('\nInvalid input. Try again.')
                    continue
                break
            except:
                print('\nInvalid input, try again.')
        scores[0] += scor
        print(f'\nYou have {use_points(0)} points remaining.')
        while True:
            try:
                scor = int(input('\nHow many points do you want to put into speed? (Remaining points will go into intelligence) '))
                if total - scor >= 0 and scor >= 0:
                    use_points(scor)
                else:
                    print('\nInvalid input. Try again.')
                    continue
                break
            except:
                print('\nInvalid input, try again.')
        scores[1] += scor
        scores[2] += use_points(0)
        return scores[0], scores[1], scores[2]

    @staticmethod
    def create(characters, skills):
        name = input("What would you wish your character name to be?: ")
        characters[name] = ['', 0, 0, 0, {'name':'description'}, {}, 1]
        while True:
            clas = input("\nPlease select the class you want to choose\n1:Archer\n2:Knight\n3:Wizard\n")
            if clas in ["1", "2", "3"]:
                break
            else:
                print("Select again")
        if clas == "1":
            clas='archer'
        elif clas == "2":
            clas='knight'
        elif clas == "3":
            clas='wizard'
        characters[name][0] = clas
        print("\nYour stats are:\nStrength\nSpeed\nIntelligence")
        characters[name][1], characters[name][2], characters[name][3] = Create.distribute(random.randint(5, 10))
        print("\nYou have one skill right now, but if you level up, you will unlock more")
        characters[name][4] = {list(skills[clas].keys())[0]: skills[clas][list(skills[clas].keys())[0]]}
        return characters

def simple(input):
    input = (input).strip().lower()
    return input