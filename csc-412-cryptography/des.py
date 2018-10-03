"""
***** des.py *****

Class: CSC 412 - Cryptography Final Project 

Due: Dec 12, 2017

Description: 
    Have implemented:
        1. A Simplified DES-type Algorithm, with four rounds and two S-boxes
        2. A Differential Cryptanalysis for Three rounds
        3. The full 64-DES by using the tables given in the textbook. 
"""



def fullsboxes(bits, num, row, col):
    """
    S-Boxes for full 64-DES.
    num is the S-box number.
    """
    sboxes = {1: [[14, 4,  13, 1, 2,  15, 11, 8,  3,  10, 6,  12, 5, 9,  0, 7],
                  [0,  15, 7,  4, 14, 2,  13, 1,  10, 6,  12, 11, 9, 5,  3, 8],
                  [4 , 1,  14, 8, 13, 6,  2,  11, 15, 12, 9,  7,  3, 10, 5, 0],
                  [15, 12, 8,  2, 4,  9,  1,  7,  5,  11, 3,  14, 10, 0, 6, 13]],

              2: [[15, 1,  8,  14, 6,  11, 3,  4,  9,  7, 2,  13, 12, 0, 5,  10],
                  [3,  13, 4,  7,  15, 2,  8,  14, 12, 0, 1,  10, 6,  9, 11, 5],
                  [0,  14, 7,  11, 10, 4,  13, 1,  5,  8, 12, 6,  9,  3, 2,  15],
                  [13, 8,  10, 1,  3,  15, 4,  2,  11, 6, 7,  12, 0,  5, 14, 9]],


              3: [[10, 0,  9,  14, 6, 3,  15, 5,  1,  13, 12, 7,  11, 4,  2,  8],
                  [13, 7,  0,  9,  3, 4,  6,  10, 2,  8,  5,  14, 12, 11, 15, 1],
                  [13, 6,  4,  9,  8, 15, 3,  0,  11, 1,  2,  12, 5,  10, 14, 7],
                  [1,  10, 13, 0,  6, 9,  8,  7,  4,  15, 14, 3,  11, 5,  2, 12]],

              4: [[7,  13, 14, 3, 0,  6,  9,  10, 1,  2, 8, 5,  11, 12, 4,  15],
                  [13, 8,  11, 5, 6,  15, 0,  3,  4,  7, 2, 12, 1,  10, 14, 9],
                  [10, 6,  9,  0, 12, 11, 7,  13, 15, 1, 3, 14, 5,  2,  8,  4],
                  [3,  15, 0,  6, 10, 1,  13, 8,  9,  4, 5, 11, 12, 7,  2,  14]],

              5: [[2,  12, 4, 1,  7,  10, 11, 6,  8,  5,  3,  15, 13, 0, 14, 9],
                  [14, 11, 2, 12, 4,  7,  13, 1,  5,  0,  15, 10, 3,  9, 8,  6],
                  [4,  2,  1, 11, 10, 13, 7,  8,  15, 9,  12, 5,  6,  3, 0, 14],
                  [11, 8,  12, 7, 1,  14, 2,  13, 6,  15, 0,  9,  10, 4, 5, 3]],

              6: [[12, 1,  10, 15, 9, 2,  6,  8,  0,  13, 3,  4,  14, 7,  5,  11],
                  [10, 15, 4,  2,  7, 12, 9,  5,  6,  1,  13, 14, 0,  11, 3,  8],
                  [9,  14, 15, 5,  2, 8,  12, 3,  7,  0,  4,  10, 1,  13, 11, 6],
                  [4,  3,  2,  12, 9, 5,  15, 10, 11, 14, 1,  7,  6,  0,  8, 13]],

              7: [[4,  11, 2,  14, 15, 0, 8,  13, 3,  12, 9, 7,  5,  10, 6, 1],
                  [13, 0,  11, 7,  4,  9, 1,  10, 14, 3,  5, 12, 2,  15, 8, 6],
                  [1,  4,  11, 13, 12, 3, 7,  14, 10, 15, 6, 8,  0,  5,  9, 2],
                  [6,  11, 13, 8,  1,  4, 10, 7,  9,  5,  0, 15, 14, 2,  3, 12]],

              8: [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
                  [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
                  [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
                  [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
        }

    # Converting decimal to binary and returning 4 bits 
    return bin(sboxes[num][row][col])[2:].zfill(4)



def SBoxes(bits, s):
    """
    S boxes for a Simplified DES-type Algorithm.
    """
    # Gettin row
    row = bits[0]
    # Getting column
    col = int(bits[1:], 2)
    num = '' 
    
    # S-boxes
    sboxes = {1: {'0':['101', '010', '001', '110', '011', '100', '111','000'],
                    '1':['001', '100', '110', '010', '000', '111', '101','011']
                   },
              2: {'0':['100', '000', '110', '101', '111', '001', '011','010'],
                    '1': ['101', '011', '000', '111', '110', '010', '001','100'] 
             }} 
    
    return sboxes[s][row][col]



def fullgetKey(c, d, i):
    """
    For full 64-DES.
    Returns key of 48 bits obtained from 56 bits
    """
    key = ''
    # Number of key bits shifted per round
    shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    # Key permutation
    ki = [14, 17, 11, 24, 1,  5,  3,  28, 15, 6,  21, 10,
          23, 19, 12, 4,  26, 8,  16, 7,  27, 20, 13, 2,
          41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
          44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
    
    # Shifts for the corresponding round i
    s = shifts[i-1]
    # Keys from previous round
    ci1 = c[i-1]; di1 = d[i-1]
    
    newc = ''; newd = ''
    # Shifing left by 1
    if s == 1:
        newc = ci1[1:] + ci1[0]
        newd = di1[1:] + di1[0]
    # Shifing left by 2
    else:
        newc = ci1[2:] + ci1[:2]
        newd = di1[2:] + di1[:2]

    newkey = newc + newd

    # Permuting key based on the permutation table
    newkey48 = ''
    for i in range(48):
        newkey48 = newkey48 + newkey[ki[i]-1] 

    # Appending keys to lists so that they can used in the next round
    c.append(newc)
    d.append(newd)

    return newkey48, c, d



def getKey(keys, i):
    """
    For a Simplified DES-type Algorithm.
    Returns a 8 bit key from the 9 bit key, by shifting it by a certain value. 
    """
    if i==1:
        return keys[:8]
    elif i ==2:
        return keys[1:]
    elif i ==3:
        return keys[2:] + keys[:1]
    elif i==4:
        return keys[3:] + keys[:2]



def fullexpand(m):
    '''
    For full 64-DES.
    Expands 32 bit msg to 48 bits.
    '''
    # Permutation
    ep = [32, 1,  2,  3,  4,  5,  4,  5,  6,  7,  8,  9, 
          8,  9,  10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
          16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 
          24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
    
    er = ''    
    # Expanding message
    for i in range(48):
        er = er + m[ep[i]-1]

    return er



def expand(m):
    """
    For a Simplified DES-type Algorithm.
    Expands 6 bit message to 8 bits.
    """
    return m[0] + m[1] + m[3] + m[2] + m[3] + m[2] + m[4] + m[5]



def fullF(ri1, ki):
    """
    The f function for the full 64-DES.
    """
    cperm = [16, 7, 20, 21, 29, 12, 28, 17, 1,  15, 23, 26, 5,  18, 31, 10,
             2,  8, 24, 14, 32, 27, 3,  9,  19, 13, 30, 6,  22, 11, 4,  25]

    # expanding to 48 bits
    expd = fullexpand(ri1) 

    # E(R) xor Ki    
    xored = bin(long(expd, 2) ^ long(ki, 2))[2:].zfill(48)
    
    # Writing b1, b2, b3..b8 where bj has 6 bits
    b = []    
    for i in range(8):
        b.append(xored[i*6 : i*6+6])
    
    
    # Here, S-box values are obtained by passing in E(R) xor Ki
    # E(R) xor Ki is obtained from the previous step
    sb = []
    output = ''
    for i in range(8):
        bi = b[i]
        # row is given b1b6
        birow = int(bi[0]+bi[5], 2)
        # column is given by b2b3b4b5b6 
        bicol = int(bi[1] + bi[2] + bi[3] + bi[4], 2)
        output = output + fullsboxes(b[0], i + 1, birow, bicol)

    # Converting 48 bit key to 32 bits by using the permutation table
    outputperm = ''
    for i in range(32):
        outputperm = outputperm + output[cperm[i]-1]

    return outputperm



def f(ri1, ki):
    """
    The f function for the Simplified DES-type Algorithm.
    """
    # Expanding 6 bit input to 8 bits
    expd = expand(ri1)
    # The input R(i-1) is XORed with Ki
    xored = bin(int(expd, 2) ^ int(ki, 2))[2:].zfill(8)
    # Getting values from s boxes
    s_box = SBoxes(xored[:4], 1) + SBoxes(xored[4:], 2)
    return s_box



def simpleDesAttack(msg, keys, start):
    """
    For a Simplified DES-type Algorithm.
    Accepts a message (bits), key and starting round and returns message after
    encrypting for the specified number of rounds. 
    """

    l = [msg[:6]]
    r = [msg[6:]]

    for i in range(start+1, 5):
        # Getting li
        li = r[i-(start+1)]
        # Key for ith round
        ki = getKey(keys, i)
        # Getting ri
        ri = bin(int(l[i-(start+1)], 2) ^ int(f(li, ki), 2))[2:].zfill(6)
        l.append(li)
        r.append(ri)

    return l[len(l)-1] + r[len(r)-1]



def fullDES():
    '''
    Implementation of the full 64 DES
    '''
    # Testing DES by using message and key given in the project file.
    msgs = '0123456789ABCDEF'
    keys = '133457799BBCDFF1'
    c = '85e813540f0ab405'

    # Converting to 64 bits
    m = bin(long(msgs, 16))[2:].zfill(64)
    k = bin(long(keys, 16))[2:].zfill(64)

    # Permutaion for the key
    kp = [57, 49, 41, 33, 25, 17, 9,  1,  58, 50, 42, 34, 26, 18,
          10, 2,  59, 51, 43, 35, 27, 19, 11, 3,  60, 52, 44, 36,
          63, 55, 47, 39, 31, 23, 15, 7,  62, 54, 46, 38, 30, 22, 
          14, 6,  61, 53, 45, 37, 29, 21, 13, 5,  28, 20, 12, 4] 

    # Getting 56 bit key from 64 bits by permuting it
    kperm = ''
    for i in range(56):
        kperm = kperm + k[kp[i]-1]

    c = [kperm[:28]]
    d = [kperm[28:]]

    # Fixed initial permutation
    ip = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 
          62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 
          57, 49, 41, 33, 25, 17, 9,  1, 59, 51, 43, 35, 27, 19, 11, 3, 
          61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
    
    # Inverse of initial permutation
    ipi = [40, 8, 48, 16, 56, 24, 64, 32, 
           39, 7, 47, 15, 55, 23, 63, 31, 
           38, 6, 46, 14, 54, 22, 62, 30,
           37, 5, 45, 13, 53, 21, 61, 29,
           36, 4, 44, 12, 52, 20, 60, 28,
           35, 3, 43, 11, 51, 19, 59, 27,
           34, 2, 42, 10, 50, 18, 58, 26,
           33, 1, 41, 9,  49, 17, 57, 25]

    # First step
    # The bits of m are permuted using a fixed initital permutation
    m0 = ''
    for i in range(64):
        m0 = m0 + m[ip[i]-1]

    l = [m0[:32]]
    r = [m0[32:]]
    
    # Second step
    for i in range(1,17):
        # l(i) = r(i-1)
        li = r[i-1]
        # k(i) is the string of 48 bits obtained from the original key
        ki, c, d = fullgetKey(c, d, i)
        # r(i) = l(i-1) XOR f(r(i-1), k(i))    
        ri = bin(long(l[i-1], 2) ^ long(fullF(li, ki), 2))[2:].zfill(32)
        l.append(li)
        r.append(ri)

    # Switch left and right to obtain R16L16    
    r16l16 = r[len(r)-1] + l[len(l)-1]
    ciphertext = ''
    # Apply the inverse of the initial permutation to get the ciphertext
    for i in range(64):
        ciphertext = ciphertext + r16l16[ipi[i]-1]

    print "%X" % int(ciphertext, 2)
    

def simplifiedDES(msg, keys):
    """
    Implementation of the Simplified DES-type Algorithm, with four rounds and
    two S-boxes. 
    Accepts a message of 12 bits and a key of 9 bits, both without spaces. It
    assumes that the user will only enter bits. 
    """

    if len(msg) != 12 and len(keys) !=9:
        return 
    
    print simpleDesAttack(msg, keys, 0)



def diff_cryp_anly():
    """
    Differential cryptanalysis: A chosen plaintext attack, meaning that the
    attacker is able to select inputs and examine outputs in an attempt to
    derive the key. This is for 3 rounds only.
    This function implements the example in the book. 
    """
    l1 = ''; r1 = ''
   
    # l1r1's
    msg0 = ['000111011011', '010111011011']
    # l1r1_stars's
    msg1 = ['101110011011', '101110011011']
    # key
    keys = '001001101'    
    
    print "First pair of bits:"
    print "L1R1:  ", msg0[0]
    print "L1R1*: ", msg1[0]
    print "Second pair of bits:"
    print "L1R1:  ", msg0[0]
    print "L1R1*: ", msg1[1]    

    # Will store the pairs to be tested for keys
    startpairs = []
    endpairs = []

    # Testing for 2 inputs 
    for i in range(2):
        sp = []
        ep = []
        # L4R4
        l4r4 = simpleDesAttack(msg0[i], keys, 1)
        # L4R4*
        l4r4_star = simpleDesAttack(msg1[i], keys, 1)

        # Key    
        k40 = getKey(keys, 4)
        
        # E(L4)
        el4 = expand(l4r4[:6])
        
        # E(L4*)
        el4_star = expand(l4r4_star[:6])

        # L4'
        l4_a = bin(int(l4r4[:6], 2) ^ int(l4r4_star[:6], 2))[2:].zfill(6)
        # R4'
        r4_a = bin(int(l4r4[6:], 2) ^ int(l4r4_star[6:], 2))[2:].zfill(6)
        # L1'
        l1_a = bin(int(msg0[i][:6], 2) ^ int(msg1[i][:6], 2))[2:].zfill(6)
        
        # Output bits        
        outputs = bin(int(r4_a, 2) ^ int(l1_a, 2))[2:].zfill(6)
        
        # E(L4)'
        el4_a = expand(l4_a)
        
        # Checking numbers 0 to 15
        for i in range(0, 16):
            
            # Checking for first four bits

            # iel4_a = i xor E(L4)'(first 4 bits)
            iel4_a = bin(int(el4_a[:4], 2) ^ i)[2:].zfill(4)
            # S-box value for iel4_a 
            s1 = SBoxes(iel4_a, 1)
            # S-box value for i
            s1_1 = SBoxes(bin(i)[2:].zfill(4), 1)
            s1s1 = int(s1, 2) ^ int(s1_1, 2)
            # Checks if it's equal to the first 3 bits of the output
            if s1s1 == int(outputs[:3],2): 
                # If yes, then save the pair
                sp.append([iel4_a, bin(i)[2:].zfill(4)])

            # Checking for last four bits

            # iel4_a = i xor E(L4)'(last 4 bits)
            iel4_a = bin(int(el4_a[4:], 2) ^ i)[2:].zfill(4)
            # S-box value for iel4_a 
            s2 = SBoxes(iel4_a, 2)
            # S-box value for i
            s2_2 = SBoxes(bin(i)[2:].zfill(4), 2)
            s2s2 = int(s2, 2) ^ int(s2_2, 2)
            # Checks if it's equal to the last 3 bits of the output
            if s2s2 == int(outputs[3:],2): 
                # If yes, then save the pair
                ep.append([iel4_a, bin(i)[2:].zfill(4)])

        # XORing the pair values with E(L4) first 4 bits
        sset = []
        for p in sp:
            sset.append(bin(int(p[0], 2) ^ int(el4[:4], 2))[2:].zfill(4))
        startpairs.append(sset)
    
        # XORing the pair values with E(L4) last 4 bits
        eset = []
        for p in ep:
            eset.append(bin(int(p[0], 2) ^ int(el4[4:], 2))[2:].zfill(4))
        endpairs.append(eset)

    # Getting key by checking for common bits in pairs

    key8bits = ''
    for s in startpairs[0]:
        if s in startpairs[1]:
            key8bits = s
    for s in endpairs[0]:
        if s in endpairs[1]:
            key8bits = key8bits + s

    # Since this is the key to the 4th round, we need the actual key
    key9bits_0 = key8bits[6:] + "0" + key8bits[:6]
    key9bits_1 = key8bits[6:] + "1" + key8bits[:6]

    check = simpleDesAttack(msg0[0], keys, 1)
    # Now there are 2 posibilities of k since, * can be 0 or 1 
    if simpleDesAttack(msg0[0], key9bits_0, 1) == check:
        print "Key is:", key9bits_0
    else:
        print "Key is:", key9bits_1



