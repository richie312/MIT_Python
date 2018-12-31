
## Import neccessary modules
import os
os.getcwd()
os.chdir(r"C:\Users\Richie\OneDrive\Python_MIT\ps4")


import string
from ps4 import *

def build_coder(shift):
    
    dict={}
    alphabets_upper = []
    alphabets_lower = []
    '''uppercase letter'''
    for letter in range(65,91):
        alphabets_upper.append(chr(letter))
    alphabets_upper.insert(0,' ')
    '''lowercase letter'''
    for letter in range(97,123):
        alphabets_lower.append(chr(letter))
    alphabets_lower.insert(0,' ')    
    
    shifted_alpha_upper=alphabets_upper[shift:]+alphabets_upper[:shift]
    shifted_alpha_lower = alphabets_lower[shift:]+alphabets_lower[:shift]
    for i in range(len(alphabets_upper)):
        dict[alphabets_upper[i]]= shifted_alpha_upper[i]
    
    
    shifted_alpha_lower=alphabets_lower[shift:]+alphabets_lower[:shift]
    for i in range(len(alphabets_lower)):
        dict[alphabets_lower[i]]= shifted_alpha_lower[i]

    return dict
print(build_coder(3))

encoder = build_coder(3)

def apply_coder(text,coder):
    encoded_text = ''
    for letter in text:
        if letter in coder:
            encoded_text += coder[letter]
        else:
            encoded_text += letter
    return encoded_text


def freq(text):
    freq = {}
    for letter in text:
        keys = freq.keys()
        if letter in keys:
            freq[letter] += 1
        else:
            freq[letter] = 1
    return freq

text = 'Apq hq hiham'

def is_word(wordlist, word):
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in wordlist


def apply_shift(text,shift):
    coder = build_coder(shift)
    encoded_text = apply_coder(text,coder)
    return encoded_text


def best_shift(text,wordlist):
    max_num_real_words = 0
    best_shift = 0
    
    for shift in range(27):
        shifted_text = apply_shift(text,shift)
        potential_words = shifted_text.split()
        num_real_words = 0    
        for word in potential_words:
            if is_word(wordlist,word):
                num_real_words += 1
            if num_real_words > max_num_real_words:
                max_num_real_words = num_real_words
                best_shift = shift
    return best_shift


Text = " This is a test"

encrypt=apply_shift(Text,8)

best_shift(encrypt,wordlist)
    
apply_shift(encrypt,19)

## Muti level encryption

def apply_shifts(text, shifts):
    initial_layer = text[shifts[0][0]:]
    for i in range(len(shifts)):
        layer =  initial_layer[:shifts[i][0]] + apply_coder(initial_layer[shifts[i][0]:],build_coder(shifts[i][1]))           
        initial_layer = layer
    return initial_layer
        
        
def test():
    shifts = [(0,6), (3, 18), (12, 16)]
    text = "Do Androids Dream of Electric Sheep?"
    test_result = apply_shifts(text,shifts)
    if test_result == 'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?':
        print("Successful")
    else:
        print("There seems to be problem with the shifts functions,FAILED")
test()

## Multi Level Code Breaking using recurssion
text='JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'


def find_best_shifts(wordlist,text):
    best_shifts = []
    max_num_real_words = 0
    best_shift = 0
    words = []    
    for shift in range(27):
        shifted_text = apply_shift(text,shift)
        potential_words = shifted_text.split()
        num_real_words = 0    
        for word in potential_words:
            if is_word(wordlist,word):
                num_real_words += 1
            
            if num_real_words > max_num_real_words:
                max_num_real_words = num_real_words
                words.append(word)
    string = ''            
    for letter in words:
        string += str(letter)
    print(string)
    loc = len(shifted_text) - len(string)       
    print(words)
                best_shift = shift
                string = ''        
                for letter in z:
                    print(letter)
                    string += str(letter)
                string
    print(z)

    




