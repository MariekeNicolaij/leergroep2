#
# Ik heb alle STRING-opgaven van CodingBat gemaakt.
#

#
# Ik heb alle LIJST-opgaven van CodingBat gemaakt.
#


# ---------------------------------------------------



# - - - CodingBat en Python-strings - - -
# Maak alle Python string opgaven op de CodingBat String-1 pagina.
# Neem in jouw bestand het volgende op om aan te geven dat je de opgaven
#   hebt gemaakt, we vertouwen er op dat je hier eerlijk bent!

# Basic python string problems -- no loops.
# Use + to combine strings, len(str) is the number of chars in a String,
#   str[i:j] extracts the substring starting at index i and 
#   running up to but not including index j.

# Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
def hello_name(name):
  return 'Hello ' + name + "!"

# Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
def make_abba(a, b):
  return a + b + b + a

# The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".
def make_tags(tag, word):
  return '<' + tag + '>' + word + '</' + tag + '>'

# Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".
def make_out_word(out, word):
  return out[0:2] + word + out[2::]

# Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.
def extra_end(str):
  return str[-2:] * 3

# Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".
def first_two(str):
  if len(str) < 2:
    return str
  return str[0:2]

# Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
def first_half(str):
  return str[:len(str)/2]

# Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.
def without_end(str):
  return str[1:len(str)-1]

# Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).
def combo_string(a, b):
  short = a if len(a) < len(b) else b
  long = b if len(a) < len(b) else a
  return short + long + short

# Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.
def non_start(a, b):
  a = a[1::]
  b = b[1::]
  return a + b

# Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.
def left2(str):
  return str[2::] + str[0:2]

#
# ----------------------------------------------------
#

# Maak alle Python list opgaven op de CodingBat List-1 pagina.
# Neem in jouw bestand het volgende op om aan te geven
#   dat je de opgaven hebt gemaakt, we vertouwen er op
#   dat je hier eerlijk bent!

# Basic python list problems -- no loops..
# Use a[0], a[1], ... to access elements in a list, 
#   len(a) is the length.

# Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.
def first_last6(nums):
  return True if nums[0] == 6 or nums[len(nums)-1] == 6 else False

# Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.
def same_first_last(nums):
  return  True if len(nums) >= 1 and nums[0] == nums[len(nums)-1] else False

# Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
def make_pi():
  return [3, 1, 4]

# Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.
def common_end(a, b):
  return True if a[0] == b[0] or a[len(a)-1] == b[len(b)-1] else False

# Given an array of ints length 3, return the sum of all the elements.
def sum3(nums):
  return nums[0] + nums[1] + nums[2]

# Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
def rotate_left3(nums):
  temp = nums[0]
  nums[0] = nums[1]
  nums[1] = nums[2]
  nums[2] = temp
  return nums

# Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.
def reverse3(nums):
  temp = nums[0]
  nums[0] = nums[2]
  nums[2] = temp
  return nums

# Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.
def max_end3(nums):
  h = nums[0] if nums[0] > nums[2] else nums[2]
  nums[0] = h
  nums[1] = h
  nums[2] = h
  return nums

# Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.
def sum2(nums):
  if not nums:
    return 0
  elif len(nums) == 1:  
    return (nums[0])
  else:
    return (nums[0] + nums[1])

# Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.
def middle_way(a, b):
  return [a[1], b[1]]

# Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.
def make_ends(nums):
  if len(nums) == 1:
    return [nums[0], nums[0]]
  else:
    return [nums[0], nums[len(nums)-1]]

# Given an int array length 2, return True if it contains a 2 or a 3.
def has23(nums):
  return True if 2 in nums or 3 in nums else False


#
# -----------------------------------------------------
#

def piglet_latin(s = 'oudervrucht'):
    """
        Ja
    """

    s.lower()
    
    # Als het argument helemaal geen letters heeft (de lege string) moet de functie een lege string teruggeven
    if not s:
        print('')
        return ''

    # als start met klinker dan += hee
    if is_character_a_klinker(s, 0):
        s += 'hee'
    else: # als medevowel dan += s[0] + ee
        t = s[0]
        s = s[1::]
        s += t + 'ee'

    return s

def is_character_a_klinker(string, index):
    s = string[index]

    if s in ['a', 'e', 'i', 'o', 'u']:
        return True
    return False

def pig_latin(s = 'ypsilon'):
    s.lower()
    letters = ''
    prefix = ''

    index = 0

    # eerst eem de 'y' checken
    if s[0] == 'y':
        if is_character_a_klinker(s, 1):
            prefix = 'ee'
            temp = s[0]
            s = s[1::]
            return s + temp + prefix
        else:
            prefix = 'hee'
            return s + prefix

    # ja i know, dit kan geheid korter of hoe je dat ook spelt 🥴
    if is_character_a_klinker(s, 0):
        for i in s:
            if is_character_a_klinker(s, index):
                # letters += s[index]
                prefix = 'hee' # beetje slordig zo in de for maar ik ben moe
            else:
                break
            index += 1
    else:
        for i in s:
            if not is_character_a_klinker(s, index):
                letters += s[index]
                prefix = 'ee'
            else:
                break
            index += 1

    return s[len(letters)::] + letters + prefix