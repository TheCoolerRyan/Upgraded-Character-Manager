#I had to do this because circular imports are apparently illegal
import levi_code,ryan_pseducode, edwings_psedocode

#create function main
def main():
    #set CHARS to empty dictionary
    chars={}
    #set SKILLS to dictionary, keys c)lasses and values lists of the two avaliable skills for that class
    skills={'archer':{'Snipe':'Ranged weapon range is doubled','Pierce Armor':'Double damage of ranged weapons.'},'knight':{'Parry':'Use a melee attack to negate an enemy\'s next attack','Disarm':'Use a melee attack to remove an enemy\'s weapon.'},'wizard':{'Quick Spell':'Cast two spells as one attack.','Change Spell':'Use melee spell attacks as ranged spell attacks, and ranged spell attacks as melee spell attacks.'}}
    print('Welcome to the RPG Character Manager.')
    #loop
    while True:
        print('\n'*5)
        #ask user if they would like to view, create characters, or exit
        choice=ryan_pseducode.simple(input('\n1. View or Modify Characters\n2. Create Character\n3. Exit\n'))
        while choice not in ['1','2','3']:
            print('\nInvalid input. Try again.')
            choice=ryan_pseducode.simple(input('\n1. View or Modify Characters\n2. Create Character\n3. Exit\n'))
        #if they choose view and the CHARS is not empty
        if choice=='1':
            if chars=={}:
                print('\nThere are no characters.')
                continue
            #call function display_characters on CHARS
            levi_code.display_characters(chars)
            #ask user if they want to view specific character, modify or delete a character, or return to start
            choice=ryan_pseducode.simple(input('\n1. View Specific Character\n2. Modify or Delete Character\n3. Return to Start\n'))
            if choice not in ['1','2','3']:
                print('\nInvalid input. Try again')
                choice=ryan_pseducode.simple(input('\n1. View Specific Character\n2. Modify or Delete Character\n3. Return to Start\n'))
            #if they choose to view specific character
            if choice=='1':
                #call function show_character on called function search on CHARS
                levi_code.show_character(ryan_pseducode.search(chars))
            #else if they choose to modify or delete
            elif choice=='2':
                #set SELECT to called search function on CHARS
                select=ryan_pseducode.search(chars)
                #ask user if they want to modify inventory, level up, remove, or change stats(or exit)
                choice=ryan_pseducode.simple(input('\n1. Modify inventory\n2. Level up\n3. Remove\n4. Change stats\n5. Exit\n'))
                if choice not in ['1','2','3','4','5']:
                    print('\nInvalid input. Try again.')
                    choice=ryan_pseducode.simple(input('\n1. Modify inventory\n2. Level up\n3. Remove\n4. Change stats\n5. Exit\n'))
                #if user chooses to modify inventory
                if choice == '1':
                    #set CHARS to call function inventory on SELECT
                    select=ryan_pseducode.inventor(select)
                #else if user chooses to level up
                elif choice=='2':
                    #set SELECT to call function level_up on CHARS and SKILLS
                    select=levi_code.level_up(select,skills)
                #else if user chooses to remove
                elif choice=='3':
                    #remove SELECT from CHARS
                    del chars[list(select.keys())[0]]
                #else if user chooses to change stats
                elif choice=='4':
                    #ask user if they want to change skills or scores
                    choice=ryan_pseducode.simple(input('\n1.Change skills\n2.Swap scores\n'))
                    while choice not in ['1','2']:
                        print('\nInvalid input. Try again.')
                        choice=ryan_pseducode.simple(input('\n1.Change skills\n2.Swap scores\n'))
                        #if user wants to change skills, set SELECT to function call skills on SELECT
                    if choice=='1':
                        select=ryan_pseducode.skill(select)
                        #else if user wants to change scores, set SELECT to function call stats on SELECT
                    elif choice=='2':
                        select=ryan_pseducode.change(select)
                elif choice=='5':
                    continue
                #update modified character in CHARS with SELECT
                if choice!='3':
                    chars[list(select.keys())[0]]=select[list(select.keys())[0]]
            #else if they choose to return to start
            elif choice=='3':
                #go to next loop iteration
                continue
        #if they choose create, set CHARS to run function create on CHARS
        elif choice=='2':
            chars=edwings_psedocode.create(chars,skills)
        #if they choose exit, break out of loop
        elif choice=='3':
            break

main()