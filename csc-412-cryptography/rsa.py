"""
***** rsa.py *****

Class: CSC 412 - Cryptography Final Project 

Due: Dec 12, 2017

Description: 
    RSA algorithm: Explained using example from the book.
        1. Bob chooses secret primes p and q and computes n=p*q
        2. Bob chooses e with gcd(e, (p-1)*(q-1)) = 1
        3. Bob computes d with d*e congruent to 1 (mod (p-1)*(q-1))
        4. Bob makes n and e public, and keeps p, q, d secret
        5. Alice encrypts m as c congruent to m^e (mod n) and sends c to Bob
        6. Bob decrypts by computing m congruent to c^d (mod n) 
"""

from cryptomath import *
from sys import *

def rsa(message):
    """
    RSA algorithm
    Accepts a message consisting of alphabets only.
    Note that this algorithm is not case sensitive and it creates a new 
    'p', 'q', 'e' everytime.
    """

    message = message.lower()
    msg = ''

    # Converting message to numbers
    for m in message:
        num = ord(m) - 96
        if num<10:
            num = "0" + str(num)
        else:
            num = str(num)
        msg = msg + num 

    # Decimal representation of the message
    msg = long(msg)

    # Generating large primes p and q
    p=q=0
    while isinstance(p, (int, long)) and isinstance(q, (int, long)) and p==q:  
        p = random_prime(40)
        q = random_prime(40)

    n = p*q
    p1q1 = (p-1)*(q-1)

    print "Numbers generated:"
    print "p:", p
    print "q:", q
    print "n:", n
    print "(p-1)(q-1):", p1q1

    # Generating encryption exponent e
    while True:
        e = random_prime(15)
        if gcd(e, p1q1) == 1:
            break

    # finding inverse of e mod (p-1)*(q-1)
    d = findModInverse(e, p1q1)

    # encrypting message    
    encryp = pow(msg, e, n)
    
    decryp = str(pow(encryp, d, n))

    print "e:", e
    print "d:", d
    print "encrypted msg:", encryp

    # decrypting message
    decryptedmsg = ''
    i = len(decryp)-1
    while i>0:
        decryptedmsg = chr(int(decryp[i-1]+decryp[i])+96) + decryptedmsg
        i = i-2
    if len(decryp)%2 == 1:
        decryptedmsg = chr(int(decryp[0])+96) + decryptedmsg
        


