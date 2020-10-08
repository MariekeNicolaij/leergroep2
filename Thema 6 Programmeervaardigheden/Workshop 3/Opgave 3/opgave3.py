
# encipher

# De functie encipher moet een nieuwe string teruggeven waarin de letters
# in s met n letters voorwaarts zijn "geroteerd" in het alfabet, 
# en terug naar het begin van het alfabet als dat nodig is.
def encipher(string = "ondo", number = 1):
    # if number < 0:
    #     number = 0
    if number > 25:
        number = 25

    if number > (len(string) - 1):
        number = (len(string) - 1)

    string = string.lower().strip()

    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    i = 0
    temp = ''
    for s in string:
        index = abc.index(s) + number

        # voor als hij weer bij a moet beginnen
        if index >= (len(abc)):
           index = index - (len(abc))

        temp += abc[index]
        i = i + 1
    return temp

def decipher(s = "qpfq"):
    return encipher(s, -1)

def blsort(L = [0,0,1,1,0,1,0,1,1,1,1,1]):
    return [0 for x in L if x == 0] + [1 for x in L if x == 1]

import random

def gensort(L = [random.randrange(0, 100),random.randrange(0, 100),random.randrange(0, 100),random.randrange(0, 100),random.randrange(0, 100),random.randrange(0, 100),random.randrange(0, 100),random.randrange(0, 100),random.randrange(0, 100),random.randrange(0, 100)], temp = []):
   
    if len(L) == 0:
        return temp
    else:
        temp.append(min(L)) # add smallest item to temp list
        L.remove(min(L)) # remove smallest item from original list
        return gensort(L, temp) # opnieuw!

def lingo(string = "poephhhhh", tring = "hanze"):
    if not string or not tring:
        return 0

    similarLetters = 0
    for s in string:
        if s in tring:
            tring = tring.replace(s, '', 1) # Remove first occurence of s
            similarLetters += 1

    return similarLetters