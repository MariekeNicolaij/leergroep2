#
# opgave2a.py
#

import random          # importeer de module met de naam random
import time
import sys

def rps():
    """ this plays a game of rock-paper-scissors in Dutch ("steen"-"papier"-"schaar")
        (or a variant of that game)
        arguments: no arguments    (prompted text doesn't count as an argument)
        results: no results        (printing doesn't count as a result)
    """
    # Gebruiker uitnodigen
    print('Kom dat zien kom dat zien! Battle of the leergroep 2 en iemand anders!!!!')
    print()
    # answer = input('Wilt u een potje spelen?')
    time.sleep(2)

    letsplay = True
    while letsplay:
        yesno = input ("Wil je mee doen?: [Ja/Nee]? : ")
        # check if yesno is equal to one of the strings, specified in the list
        if yesno in ['Ja', 'Nee']:
            # if it was equal - break from the while loop
            break
            # process the input
        if yesno.lower() == "nee" and "no": 
            print ("Oke doei") 
            # quit() werkt niet ?
            letsplay = False
        elif yesno.lower() == "ja" and 'yes': 
            print ("Have fun!")
            break
    print()

# small fix because quit() doesn't work 
    if (not letsplay):
        return

    weaponIsChosen = False
    weapon1 = 'Tiny Tim'
    weapon2 = 'Trotse Tom'
    weapon3 = 'Makkelijke Marieke'
    weapon4 = 'Grote boze heks'
    weapon = ''

    print()
    while not weaponIsChosen:
        weapon = input ("Choose your weapon: [" + weapon1 + "/" + weapon2 + "/" + weapon3 + "/" + weapon4 + "/" + "]? : ")
        # check if yesno is equal to one of the strings, specified in the list
        if weapon in [weapon1, weapon2, weapon3, weapon4]:
            # if it was equal - break from the while loop
            # process the input
            if weapon == weapon1: 
                print("Ik vind provotype een beter woord")
                weaponIsChosen = True
            elif weapon == weapon2: 
                print("9 tegen rascisme")
                weaponIsChosen = True
            elif weapon == weapon3: 
                print("Roekoe HOOO")
                weaponIsChosen = True
            elif weapon == weapon4: 
                print("IPOOOOOOOOO")
                weaponIsChosen = True

    comp = random.choice([weapon1, weapon2, weapon3, weapon4])
    print()

    print('De gebruiker (jij) koos', weapon)
    print('De computer (ik)   koos', comp)
    print()

    if weapon == weapon1:
        if comp == weapon1:
            print("Gelijkspel! Probeer nog een keer")
        if comp == weapon2:
            print("Speler heeft gewonnen!")
        if comp == weapon3:
            print("Computer heeft gewonnen!")
        if comp == weapon4:
            print("Speler heeft gewonnen!")

    if weapon == weapon2:
        if comp == weapon1:
            print("Speler heeft gewonnen!")
        if comp == weapon2:
            print("Speler heeft gewonnen!")
        if comp == weapon3:
            print("Speler heeft gewonnen!")
        if comp == weapon4:
            print("Speler heeft gewonnen!")

    if weapon == weapon3:
        if comp == weapon1:
            print("Speler heeft gewonnen!")
        if comp == weapon2:
            print("Computer heeft gewonnen!")
        if comp == weapon3:
            print("Gelijkspel! Probeer nog een keer")
        if comp == weapon4:
            print("Speler heeft gewonnen!")

    if weapon == weapon4:
        if comp == weapon1:
            print("Computer heeft gewonnen!")
        if comp == weapon2:
            print("Computer heeft gewonnen!")
        if comp == weapon3:
            print("Computer heeft gewonnen!")
        if comp == weapon4:
            print("Computer heeft gewonnen!")
