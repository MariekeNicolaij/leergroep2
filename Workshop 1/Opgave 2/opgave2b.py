"""
Titel voor je avontuur: De queeste naar taart.

Opmerkingen over hoe je het avontuuur kan "winnen" of "verliezen":
* kies de tafel om te winnen
* kies de deur om te verliezen
"""

import time

# Beste verhaal ooit
def adventure():
    """Runs one session of interactive fiction

    Well, it's "fiction," depending on the pill color chosen...

    arguments: no arguments (prompted text doesn't count as an argument)
    results: no results     (printing doesn't count as a result)
    """
    # zet deze waarde op 0.0 om te testen of snel te spelen,
    # ..of hoger voor meer dramatisch effect!
    delay = 3

    username = input("Hoe noemt men u, edele avonturier? ")

    print()
    print("Welkom,", username, "in het Libracomplex, een labyrint")
    print("van gewichtige wonderen en grote hoeveelheden ... taart!")
    print()
    print("Uw queeste: om een taart te vinden, en te eten!")
    print()

    flavor = input("Welke smaak zoekt u? ")
    if flavor == "aardbeien":
        print("Uw wijsheid in taartkeuze is overweldigend!")
    elif flavor == "kersen":
        print("Een Limburgse klassieker: een goede keuze, avonturier!")
    else:
        print("Ieder zijn smaak...")

    answer = input("Wat een goed antwoord! Maar heeft u ook wel eens gehoord van worteltjestaart? ")
    if answer == "ja":
        print()
        print("Ik wist dat u op de hoogte was van het Giga Konijnenhol!")
    elif answer == "nee":
        print()
        print("Nee! Wat een schande! Loopt u maar snel verder!")
    else:
        print()
        print("Geen direct antwoord op mijn vraag, maar goed ga verder.")

    knop = input("U ziet een knoppie, drukt u hem in?")
    if knop.lower() == "ja" or knop.lower() == 'yes':
        print("Een groot luik opent met extra taart!")
        print()
    elif knop.lower() == "nee" or knop.lower() == "no":
        print("Dan maar niet, loop gerust verder")
        print()
    elif knop.lower() == 'misschien' or knop.lower("maybe"):
        print("Gist gij nu al mis......")
        print()
    else :
        print("oke boomer")   
        print()

    man = input("U ziet een bedelaar op de grond zitten, geeft u deze man wat geld?")
    if man.lower() == 'ja':
        print("De man rukte op en beroofde u van al uw bezittingen!")
        print()
    else :
        print()
        print("De man kijkt u chagerijnig aan en valt weer in slaap")     

    print()
    print("Voorwaarts naar de queeste!\n\n")
    print("Een gang strekt zich voor u uit; in het gedimde licht ziet u")
    print("aan de ene kant een tafel met onduidelijke vormen en")
    print("materialen, en aan de andere kant een deur op een kier,")
    print("waarachter gelach --is dat gelach?-- van studenten klinkt.")

    time.sleep(delay)

    print()
    choice1 = input("Kiest u de tafel of de deur? [tafel/deur] ")
    print()

    if choice1 == "tafel":
        print("Als u de tafel benadert lijkt de onduidelijke massa")
        print("een steeds grotere vorm aan te nemen, tot ...")

        time.sleep(delay)

        print("... ze herkenbaar wordt als een grote stapel verpakte")
        print("taarten, het karton strak geplooid. Uw uitdaging --en")
        print("honger-- is op smakelijke wijze opgelost.")
        print()
        print("Tot ziens,", username, "!")
    else:
        print("U opent de deur en ziet een congregatie van wijze dames")
        print("en heren, die allen genieten van hun taken. Samenwerking")
        print("en vrolijkheid zijn hier in overvloed aanwezig, maar...")

        time.sleep(delay)

        print("...ze hebben ALLE taart opgegeten! Resten van dozen")
        print("liggen overal verspreid. U wordt duizelig en grijpt")
        print("naar een taart. Er is niets. U ademt uit en valt,")
        print("en ligt verslagen tussen de resten van dozen die u")
        print("langzaam bedekken tot verstikking volgt.")
        print()
        print("Vaarwel,", username, ".")

    feest = input("Is het tijd voor feest?")
    if (feest.lower() == 'ja'):
        print()
        print("Heuj, zo mogen we het horen")
    elif (feest.lower() == 'nee'):
        print()
        print("Wut wut wut wut wut")

    finale = input("Wil je nog wat kwijt?")
    if (len(finale) > 0):
        print()
        print(finale)