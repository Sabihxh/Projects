from fractions import Fraction
import operator
text = 'aBbCccDddd...'

#converts sentences to list, where each character is an element of the list
def text_to_list(text):
    letter_list = []
    for char in text:
        letter_list.append(char.lower())
    return letter_list

#converts text into dictionary where key is distinct character and its value
#is the number of its occurences
def list_count(text):
    a_dict = {}
    a_list = text_to_list(text)
    for x in a_list:
        a_dict[x] = a_list.count(x)
    return a_dict

# print list_count(text)

#caluclates the probablity of each letter occuring in text
def probablities(text):
    a_dict = list_count(text)
    total = len(text)
    for key in a_dict:
        a_dict[key] = Fraction(a_dict[key], total)
    return a_dict

def sorted_dict(text):
    a_dict = probablities(text)
    sorted_dict = sorted(a_dict.items(), key = operator.itemgetter(1)) 
    return sorted_dict

def encode(text):
    pass

print sorted_dict(text)