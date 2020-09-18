def leng(s):
    """leng returns the length of s
       Argument: s, which can be a string or list
    """
    if s == '' or s == []:   # als lege string of lege lijst
        return 0
    else:
        return 1 + leng(s[1:])

def mult(n, m):
    """Function for calculating the product of two
        given numbers
    """
    if m == 0:
        return 0
    else:
        return n + mult(n, m - 1)

def dot(L, k):
    """Function for calculating the inproduct of 
        two given lists
    """
    if len(L) > 0 and len(k) > 0:
        return L[0] * k[0] + dot(L[1:], k[1:])
    else:
        return 0

def ind(e, L):
    """Function for seeking the first common index
        in a string or list
    """
    length = len(L) - 1

    if e not in L :
        return length
    elif type(L) == str or type(L) == list :
        if (e == L[length]) :
            print(length)
            return length
        else :
            ind(e, L[:-1])

def letter_score(let):
    """Function for indicating the score of a given
        Scrabble letter
    """
    if type(let) == str and len(let) == 1:
        let = let.lower()

        array = [ ['adeinorst', 1], ['ghl' , 2], ['bcmp', 3], ['jkuvw', 4], ['f', 5], ['z', 6], ['xy', 8], ['q', 10] ]
       
        for i in array:
            if let in i[0]:
                return i[1]
    else:
        return 0

def scrabble_score(s):
    """Function for indicating the score of a given
        Scrabble word
    """
    if type(s) == str and len(s) > 0:  
        s = s.lower()
        array = [ ['adeinorst', 1], ['ghl' , 2], ['bcmp', 3], ['jkuvw', 4], ['f', 5], ['z', 6], ['xy', 8], ['q', 10] ]
        score = 0

        for i in array:
            if s[0] in i[0]:
                score += i[1]
        
        return score + scrabble_score(s[1:])
    else:
        return 0   

# def transcribe(s):
#     """Function for indicating the score of a given
#         Scrabble word
#     """
#     if type(s) == str and len(s) > 0:
#         s = s.lower()
#         s = s.strip()

#         array = [['a', 'u'], ['c', 'g'], ['g', 'c'], ['t', 'a']]

#         transcription = ''

#         for i in array:
#             if s == i[0]:
#                 transcription = transcription + i[1]

#         return transcription + transcribe(s[1:])
#     else:
#         return ''