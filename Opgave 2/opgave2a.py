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
    print('Kom tot ziens kom tot ziens! Steen papier schaar!!!!')
    time.sleep(1)
    # answer = input('Wilt u een potje spelen?')
    time.sleep(2)

    letsplay = True
    while letsplay:
        yesno = input ("Wil je mee doen?: [Ja/Nee]? : ")
        # check if d1a is equal to one of the strings, specified in the list
        if yesno in ['Ja', 'Nee']:
            # if it was equal - break from the while loop
            break
            # process the input
        if yesno.lower() == "nee" and "no": 
            print ("Oke doei") 
            # quit() werkt niet ?
            letsplay = False
        elif yesno.lower() == "ja": 
            print ("Have fun!")
            break

# small fix because quit() doesn't work 
    if (not letsplay):
        return
    user = input("Kies je wapen [steen, papier, schaar]: ")
    comp = random.choice(['steen', 'papier', 'schaar'])
    print()

    print('De gebruiker (jij) koos', user)
    print('De computer (ik)   koos', comp)
    print()

    if user == 'steen':
        print('Haha! Eigenlijk koos ik papier! IK HEB GEWONNEN!')

    print("Hopelijk heb je de volgende keer meer geluk...")