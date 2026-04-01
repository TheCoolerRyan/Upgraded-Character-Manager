# Import the classes from calculations.py
from calculations import *


# Create main function
def main():
    # Pull existing characters
    chars = Characters.pull()

    # Define skills dictionary
    skills = {
        'archer': {'Snipe': 'Ranged weapon range is doubled', 'Pierce Armor': 'Double damage of ranged weapons.'},
        'knight': {'Parry': "Use a melee attack to negate an enemy's next attack", 'Disarm': "Use a melee attack to remove an enemy's weapon."},
        'wizard': {'Quick Spell': 'Cast two spells as one attack.', 'Change Spell': 'Use melee spell attacks as ranged spell attacks, and ranged spell attacks as melee spell attacks.'}
    }

    print('Welcome to the RPG Character Manager.')
    while True:
        print('\n'*5)
        choice = simple(input('\n1. View or Modify Characters\n2. Create Character\n3. Exit\n'))
        while choice not in ['1', '2', '3']:
            print('\nInvalid input. Try again.')
            choice = simple(input('\n1. View or Modify Characters\n2. Create Character\n3. Exit\n'))

        if choice == '1':
            if not chars:
                print('\nThere are no characters.')
                continue
            # Call display_characters from Characters class
            Characters.display_characters(chars)
            choice = simple(input('\n1. View Specific Character\n2. Modify or Delete Character\n3. Return to Start\n'))
            if choice not in ['1', '2', '3']:
                print('\nInvalid input. Try again.')
                choice = simple(input('\n1. View Specific Character\n2. Modify or Delete Character\n3. Return to Start\n'))

            if choice == '1':
                show_char = Characters.search(chars)
                if show_char:
                    Characters.show_character(show_char)
            elif choice == '2':
                selected = Characters.search(chars)
                choice = simple(input('\n1. Modify inventory\n2. Level up\n3. Remove\n4. Change stats\n5. Exit\n'))
                if choice not in ['1', '2', '3', '4', '5']:
                    print('\nInvalid input. Try again.')
                    choice = simple(input())
                if choice == '1':
                    selected = Characters.inventor(selected)
                elif choice == '2':
                    selected = Characters.level_up(selected, skills)
                elif choice == '3':
                    del chars[list(selected.keys())[0]]
                elif choice == '4':
                    sub_choice = simple(input('\n1.Change skills\n2.Swap scores\n'))
                    while sub_choice not in ['1', '2']:
                        print('\nInvalid input. Try again.')
                        sub_choice = simple(input())
                    if sub_choice == '1':
                        selected = Characters.skill(selected)
                    elif sub_choice == '2':
                        selected = Characters.change(selected)
                elif choice == '5':
                    continue
                # Update character in chars
                if choice != '3':
                    chars[list(selected.keys())[0]] = selected[list(selected.keys())[0]]
            elif choice == '3':
                continue

        elif choice == '2':
            chars = Create.create(chars, skills)
        elif choice == '3':
            break

        Characters.save(chars)

        

main()