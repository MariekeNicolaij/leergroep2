
# encipher

# De functie encipher moet een nieuwe string teruggeven waarin de letters
# in s met n letters voorwaarts zijn "geroteerd" in het alfabet, 
# en terug naar het begin van het alfabet als dat nodig is.
def encipher(string, number):
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

def decipher(s):
    return encipher(s, -1)

def bisort(L):
    return L