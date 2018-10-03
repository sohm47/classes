"""
***** cryptomath.py *****

Class: CSC 412 - Cryptography Final Project 

Due: Dec 12, 2017

Description: 
    Basic Number Theory : Contains mathematics functions used for various
    algorthms in this project.
"""

from math import floor, ceil
from random import randrange

def gcd(a, b):
    """
    Finds the Greatest Common Divisor of a and b. It's the largest number that 
    divides a and b. 
    """
    if b == 0:
        return a
    else:
        return gcd (b, a%b)
    
    
    
def extendedgcd(a, b):
    """
    Used for finding solutions to equations of the form ax + by = gcd(a, b)
    Returns gcd, x, y 
    """
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extendedgcd(b%a, a)
        return g, y-(b//a)*x, x
   
   
        
def findModInverse(a, n):
    """
    Finding solution to ax congruent to 1 (mod n).
    """
    g, x, _ = extendedgcd(a, n)
    if g == 1:
        return x%n
      

        
def primroot(a, n):
    """
    To verify if a is primitive root (mod n).
    """
    multvalues = []
    for i in range(0, n):
        val  = pow(a, i, n)
        if val not in multvalues:
            multvalues.append(val)
        else:
            return False
    return True
            


def is_perfect_square(n):
    """
    Checks if a number 'n' is a perfect square.
    """
    if n < 0:
        return False
    if n == 1:
        return True

    x = n // 2
    y = set([x])

    while x * x != n:
        x = (x + (n // x)) // 2
        if x in y: return False
        y.add(x)

    return True



def is_prime(n, r):
    """
    Miller-Rabin Primality Test
    Accepts a number 'n' to be tested and a number 'r' for number of rounds to
    test it. The more rounds one tests it, the higher the probability of it 
    being a prime.
    Returns 0 if prime, 1 for probably a prime and 2 for definitely a prime
    """

    # Number less than 2 or an even number
    if n < 2 or (not(n&1)):
        return 0
    
    # Hardcoded some small integers
    if n in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83]:
        return 2
    
    m = n - 1
    k = 0
    # Dividing by 2 until m is not a even number 
    while (not m&1):
        m = m>>1
        k+=1

    # Running this multiple times so that probability of a large number being 
    # prime is high 
    for j in range(r):
        
        # Generating big random number
        a = randrange(1, n)
        
        # a^m (mod n)
        b = pow(a, m, n)
        if b%n in [1, n-1]:
            continue

        i = 0
        # While it is not a even number
        while i < k-2:
            b = pow(b, 2, n)
            if b%n == 1:
                return 0
            if b%n == n-1:
                break
            i+=1
        else:
            b = pow(b, 2, n)
            if b%n != n-1:
                return 0
    
    return 1



def random_prime(b):
    """
    Create a random prime between 2^(b+1)-1 and 2^b-1
    """
    
    # Will try a maximum of 1000 times to generate a random prime
    for i in range(1000):

        # Generating a random number between 2^(b+1)-1 and 2^b-1
        p = randrange(pow(2,b)-1, pow(2,b+1)-1)

        # Testing for prime using Miller-Rabin Primality test
        # Note that the Miller-Rabin implemented in this file returns 1 if it's 
        # probably a prime and 2 if it's definitely a prime
        if is_prime(p, 64) in [1,2]:
            return p
    
    # If it fails to generate a random prime in 1000 tries, it returns false
    return False



def matrixmult(m1, m2):
    """
    Perform modular (26) matrix multiplication of 2 matrices of the 
    order 1x3 and 3x3. Used in Block Cipher encoding and decoding. 
    """
    m = [0,0,0]
    # m1 X m2
    for i in range(1):
        for j in range(3):
            for k in range(3):
                m[j] += (m1[k] * m2[k][j]) 
    m[0] %= 26; m[1] %= 26; m[2] %= 26 

    return m
    


def fermat(n):
    """
    Fermat Factorization: The idea is to express n as a difference of two
    squares, that is, n = x^2 - y^2 = (x+y)*(x-y) which gives the factorization
    for n.
    """
    # Computing n+1^2, n+2^2 + n+3^2 ... until we find a perfect square
    i = 1
    while True:
        s = n + pow(i, 2)
        if is_perfect_square(s):
            root = int(s**0.5)
            return [root + i, root - i]
        i += 1



def g(x, n, newnum):
    """
    Helper function for Pollard Rho. This returns x^2 - 1 mod n
    """
    return (pow(x, 2) + newnum) % n



def pollard_rho(n):
    """
    Pollard Rho:
    
    g ( x ) = ( x 2 + c ) mod n 

    x = 2; y = 2; d = 1
    while d == 1
        x = g(x)
        y = g(g(y))
        d = gcd(|x - y|, n)
    if d == n 
        change c and run again
    else:
        return d
    """
    if is_prime(n, 16) != 0:
        return [n,1] 

    # Special case
    if n == 4:
        return [2, 2]

    while True:
        newnum = randrange(2, n-1)
        x = 2; y = 2; d = 1
        while d==1:
            x = g(x, n, newnum)
            y = g(g(y,n,newnum),n, newnum)
            d = gcd(abs(x-y)%n,n)
    
        if d != n:
            return [d, n/d]



def pollard_p1(n):
    """
    P-1 Factoring Algorithm
    Accepts a composite number n
    """
    a = 2
    bound = 2
    
    if is_prime(n, 16)!=0:
        return [n, 1]

    while True:
        # b1 congreuent to a (mod n)
        b = a % n

        for j in range(2, bound):
            b = pow(b,j,n)
       
        d = gcd(abs(b-1), n)

        if d > 1 and d < n:
            return [d, n/d]
        else:
            a += 1 



def shanks(n, k):   
    """
    Shanks square forms factorization: A method for integer factorization 
    devised by Daniel Shanks as an improvement to Fermat's factorzation method. 
    This returns a non trivial factor of N.
    Accepts:
        n - To be factored. Neither a prime nor a perfect square.
        k - Small multiplier.
    I haven't this function much because I have added a reference to this
    algorithm.

    Reference: 
    https://www.saylor.org/site/wp-content/uploads/2012/07/Shanks-square-
    forms-factorization.pdf
    """

    if is_prime(n, 32):
        print "Number should not be a prime"
        return 
    if is_perfect_square(n):
        print "Number should not be a perfect square"
        return

    if n%2 == 0:
        return 2

    # Initialize
    p = [floor((k*n)**float(0.5))]
    q = [1, k*n - p[0]**2]
    b = []
    
    # Repeating until Qi is a perfect square
    i = 1
    while is_perfect_square(int(q[i])) == False:
        b.append(floor((floor((k*n)**float(0.5)) + p[i-1])/(float(q[i]))))
        p.append(b[i-1]*q[i] - p[i-1])
        q.append(q[i-1] + b[i-1]*(p[i-1] - p[i]))
        i += 1
    
    # Initialization
    b = [floor((floor((k*n)**float(0.5)) + p[i-1])/(float(q[i])))]
    p = [b[0]*(q[i]**(float(0.5))) + p[i-1]]
    q = [q[i]**float(0.5)]  
    q.append((k*n - p[0]**2)/float(q[0]))
    
    # Repeat until P(i+1) = Pi
    i = 1
    while True:
        b.append(floor((floor((k*n)**float(0.5)) + p[i-1])/(float(q[i]))))
        p.append(b[i]*q[i] - p[i-1])
        q.append(q[i-1] + b[i]*(p[i-1] - p[i]))

        if p[i-1] == p[i]:
            break
        i += 1

    # f = gcd(N, Pi)
    f = gcd(int(n), int(p[i]))
    if f not in [1, n]:
        return [f, n/f]
    else:
        print "Try another value of k"
        return None



def seive_sundaram(n):
    """
    Seive of Sundaram to find all prime numbers smaller than n.
    """

    # In general Sieve of Sundaram, produces primes smaller
    # than (2*x + 2) for a number given number x.
    # Since we want primes smaller than n, we reduce n to half
    
    # List of primes
    lst = []

    nNew = long((n-2)/2)

    # This array is used to separate numbers of the form i+j+2ij from other 
    # where 1 <= i <= j and initialize them as not marked
    marked = [False]*(nNew+1)

    # Mark all numbers of the form i+j+2ij as true where 1 <= i <= j
    for i in range (1, nNew+1):
        j = long(i)
        while (i+j+2*i*j) <= nNew:
            marked[i+j+2*i*j] = True
            j+=long(1)

    # Since 2 is a prime number 
    if n>2:
        lst.append(2)

    # Print other primes. Remaining primes are of the form 2*i + 1 such that 
    # marked[i] is false
    for i in range (1, nNew+1):
        if marked[i] == False:
            lst.append(2*i + 1)

    return lst



