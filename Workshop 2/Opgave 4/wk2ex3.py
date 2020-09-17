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

# def ind(e, L):
#     """Function for calculating the inproduct of 
#         two given lists
#     """
#     if e not in L:
#         return len(L)
#     elif type(L) == string:
#         print('string')
#     elif type(L) == list:
#         print('list')