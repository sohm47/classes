"""
***** crypfunc.py *****

Class: CSC 412 - Cryptography Final Project 

Due: Dec 12, 2017

Description: 
    Classical Cryptosystems : This file contains some classical cryptosystems 
    (affine, vigenere, block) and attacks on the vigenere and affine ciphers.
"""

import numpy as np
from cryptomath import *
import sys

# Frequences of english letters
FREQ = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.070, 0.002,
        0.008, 0.040, 0.024, 0.067, 0.075, 0.019, 0.001, 0.060, 0.063, 0.091,
        0.028, 0.010, 0.023, 0.001, 0.020, 0.001] 

# Maps letters to numbers
NUMS = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 
        'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 
        'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 
        'z':25 }

# Maps numbers to letter
CHARS = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 
         9:'j', 10:'k', 11:'l', 12:'m', 13:'n', 14:'o', 15:'p', 16:'q', 
         17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w', 23:'x', 24:'y', 
         25:'z' } 


def freqCalc(sentence):
    """
    Accepts a string of letters and calculates the frequency of each letter 
    in the string. 
    Note that it considers uppercase and lowercase letters as 2 different types
    of characters.
    """
    # Goes though the string and keeps count of each unique character in a 
    # dictionary
    freq = dict()
    for s in sentence:
        if s not in freq:
            freq[s] = 0
        else:
            freq[s] += 1
        
    print freq 



def affine(alpha, beta, plaintext, ciphertext):
    """
    Affine Cipher: Takes in alpha, beta, plaintext and ciphertext, and prints
    the encoded and decoded text respectively 
    It assumes that the user will provide valid text.
    """
    plaintext = plaintext.lower()
    ciphertext = ciphertext.lower()
    encodedtext = ""
    decodedtext = ""
    
    if gcd(alpha, 26) == 1:
        # Encode: X = alpha*(numeric value of x) + beta  (mod 26)
        for p in plaintext:
            encodedtext = encodedtext + CHARS[(alpha*NUMS[p] + beta)%26]
        
        # Decode: x = (X - beta)*inverse_alpha  (mod 26)
        for c in ciphertext:
            decodedtext = decodedtext + \
                            CHARS[(NUMS[c] - beta) * \
                            findModInverse(alpha, 26) % 26]
        
        print "Encoded Text:", encodedtext.upper()
        print "Decoded Text:", decodedtext
    else:
        print "GCD of alpha and 26 should be 1"
        


def affine_attack1():
    """
    Ciphertext only: this uses the brute force technique and finds all the keys.
    One can then try each key and choose the one that gives a meaningful text. 
    """
    # Getting alpha values: gcd(alpha, 26) = 1
    alpha = filter(lambda i: gcd(i, 26) == 1, range(26))
    beta = range(1,27)
    
    print "All alpha values:", alpha

    print "All beta values:", beta

    print "Total values to be tried:", len(alpha)*len(beta)



def affine_attack2(ciphertext):
    """
    Chosen plaintext: Accepts ciphertext and chooses 'ab' as the plaintext. 
    The first character of the ciphertext will be alpha*0 + beta = beta, and 
    the second character will be alpha + beta. Therefore we can find the key.
    """
    plaintext = "ab"
    ciphertext = ciphertext.lower()

    # alpha*0 + beta = beta 
    beta = NUMS[ciphertext[0]]%26
    
    # alpha = secondLetter - beta
    alpha = (NUMS[ciphertext[1]] - beta)%26

    print "alpha:", alpha 
    print "beta:", beta

    if gcd(alpha, 26) != 1:
        print "This encryption/decryption cannot happen because",
        print "gcd(alpha, 26) is not 1"
        


def vigenere(plaintext, ciphertext, keyl):
    """
    Vigenere cipher (multi alphabet cipher): Accepts plaintext, ciphertext, and 
    key length from the user. It then askes the user to enter the keys, and 
    it then prints the encoded and decoded text. 
    """             
             
    plaintext = plaintext.lower()
    encodedtext = ""
    ciphertext = ciphertext.lower()
    decodedtext = ""

    # Accepting keys from user    
    print "Enter the integer keys (0 to 25): "
    keys = []
    for i in range(0, keyl):
        keys.append(int(raw_input())%26)
    
    # Encode
    # Each letter in plaintext is shifted forward by a certain value
    # (numbers in key)
    count = 0
    for p in plaintext:
        encodedtext += CHARS[(NUMS[p] + keys[count])%26]
        count += 1
        
        # Taking the first value of the key again
        if count == len(keys):
            count = 0
       
    # Decode
    # Each letter in plaintext is shifted backward by a certain value
    # (numbers in key)
    count = 0
    for c in ciphertext:
        decodedtext += CHARS[(NUMS[c] - keys[count])%26]
        count += 1

        # Taking the first value of the key again
        if count == len(keys):
            count = 0
            
    print encodedtext.upper()
    print decodedtext
    


def vig_attack():
    """
    An attack on Vigenere Cipher by finding the key length and the key.
    Displays the ciphertext and the corresponding plaintext.    
    """
    # Ciphertext chosen in this implementation
    cphTxt1 = "vvhqwvvrhmusgjgthkihtssejchlsfcbgvwcrlryqtfsvgahw"
    cphTxt2 = "kcuhwauglqhnslrljshbltspisprdxljsveeghlqwkasskuwe"
    cphTxt3 = "pwqtwvspgoelkcqyfnsvwljsniqkgnrgybwlwgoviokhkazkq"
    cphTxt4 = "kxzgyhcecmeiujoqkwfwvefqhkijrclrlkbienqfrjljsdhgr"
    cphTxt5 = "hlsfqtwlauqrhwdmwlgusgikkflryvcwvspgpmlkassjvoqxe"
    cphTxt6 = "ggveyggzmljcxxljsvpaivwikvrdrygfrjljslveggveyggei"
    cphTxt7 = "apuuisfpbtgnwwmuczrvtwglrwugumnczvile"    
    cipherText = cphTxt1+cphTxt2+cphTxt3+cphTxt4+cphTxt5+cphTxt6+cphTxt7
    
    print "CipherText is:\n", cipherText.upper()

    # Finding key
    keys = []
    coincidences = []
    # Displacement
    for i in range(1, 7):
        # Going through the entire text, each time shifting the text by 1 to the
        # right and placing it on top of the original text and finding number of
        # matching letters
        # Coincidences[0] will containing number of coincidences for shift of 1
        coincidences.append(0)
        for j in range (0, len(cipherText) - i):
            if cipherText[j].lower() == cipherText[j+i].lower():
                coincidences[i-1] += 1
  
    # Keylength will be the displacement with the most coincidences
    keyLength = coincidences.index(max(coincidences)) + 1

    print "\nKey Length:", keyLength
    
    # Finding the key: 2nd method from the textbook
    
    # Finding Aj, where j is shift caused by the first element in the key
    # Making new lists consisting of shifted values
    freqShifted = [FREQ]
    for j in range(1, 26):
        l = FREQ[-j:] + FREQ[:(len(FREQ) - j)]
        freqShifted.append(l) 
    
    # Computing dot product and finding key
    for i in range(0, keyLength):

        # Finding number of occurences
        # In the first iteration it will check for 1st, 6th, 11th etc
        v = [float(0)] * 26; t = i+1
        while t < len(cipherText):
            v[NUMS[cipherText[t].lower()]] += float(1)
            t += keyLength
            
        # Dividing by total number of letters counted
        w = [x / float(len(cipherText)) for x in v]

        summ = [0] * 26; k = 0
        # 0 <= <=25
        # Dot product: W.Al
        for l in range(0, 26):
            for g in range(0,26):
                summ[k] = w[g] * freqShifted[l][g] + summ[k] 
            k += 1

        # Getting index of largest value
        ind = summ.index(max(summ))
        keys.append(CHARS[ind])
    
    keys = keys[-1:] + keys[:4]
    
    # Decrypting
    # Getting alphabet number of the key
    keys = [NUMS[k] for k in keys]
    
    # Going though the cipher text
    i = 0; p = ''
    for c in cipherText:
        # Getting corresponding letter
        p = p + CHARS[(NUMS[c] - keys[i])%26]
        i+=1
        # Note that the key repeats itself
        if i==len(keys):
            i = 0 

    print "\nPlainText is:\n", p 



def blockC(plaintext):
    """
    Block cipher: encode and decode.
    Accepts plaintext from user, and encodes and decodes the texts 
    """
    plaintext = plaintext.lower()

    # Adding 'x' to the end to make it a multiple of 3 since out int length is 3
    if len(plaintext)%3 == 1:
        plaintext = plaintext + "x"*2
    elif len(plaintext)%3 == 2:
        plaintext = plaintext + "x"

    # Using n = 3
    n = 3
    # Key is a nxn matrix. In this case it is matrix 'm2'
    m2 = [[1,2,3],[4,5,6],[11,9,8]] 
    # Inverse of the above matrix
    invm2 = [[22, 5, 1], [6, 17, 24], [15, 13, 1]]

    # Converting plaintext to 1x3 matrices    
    m1 = [] 
    for i in range(0, len(plaintext), 3):
        m1.append([NUMS[plaintext[i]], NUMS[plaintext[i+1]], NUMS[plaintext[i+2]]])

    # Encrypting by performing a modular matrix multiplication   
    m3 = []
    for matrix in m1:
        m3.append(matrixmult(matrix, m2))
        
    # Getting corresponding letter for each number in the matrices
    ciphertext = ""
    for i in range(len(m3)):
        ciphertext =ciphertext + CHARS[m3[i][0]] + CHARS[m3[i][1]] + CHARS[m3[i][2]]
    print "Encoded text:", ciphertext.upper()
    
    # Note that gcd (det(m2), 26) = 1, so we can proceed
    # Decrypting by performing a modular matrix multiplication
    pm = []
    for m in m3:
        pm.append(matrixmult(m, invm2))

    # Getting corresponding letter for each number in the matrices
    plaintext = ''
    for i in range(len(m3)):
        plaintext = plaintext + CHARS[pm[i][0]] + CHARS[pm[i][1]] + CHARS[pm[i][2]]

    # Note that there may be an 'x' in the end, because it was used for 
    # encrypting
    print "Decoded text:", plaintext
    


