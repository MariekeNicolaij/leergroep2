# Laad dit bestand en voer het uit met run wk1ex2a.py
# Als dat gelukt is, zie je helemaal geen bericht verschijnen
# De code van dit bestand zit in een functie met de naam rps()
# Om de functie uit te voeren (nadat het bestand geladen is) kan je rps() typen bij de prompt en op enter drukken.
# Als het lukt, top! (Als het niet lukt, vraag het ons.) Hier is hoe het eruit ziet net voordat de functie uitgevoerd wordt:
# 
# run wk1ex2.py
# rps()
# 
#
# wk1ex2a.py
#

import time          # importeer de module met de naam time
import random        # importeer de module met de naam random


def rps():
    """ this plays a game of rock-paper-scissors in Dutch ("steen"-"papier"-"schaar")
        (or a variant of that game ...)
        inputs: no inputs    (prompted text doesn't count as input)
        outputs: no outputs  (printing doesn't count as output)
    """
    name = input('Hoi... wat is je naam? ')
    print()
    print("Hmmm...")
    print()

    if name == 'Tjerk':
        print('Even lekker opsparren!')

    elif name == 'Bart':
        print('Maakt dat sense?')
        time.sleep(1)
        print('Ja dat maakt sense')

    else:
        print('Welkom,', name)
        my_choice = random.choice(['steen', 'papier', 'schaar'])
        print('Ik kies overigens ', my_choice)

rps()