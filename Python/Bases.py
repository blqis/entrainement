from random import *

### 1

def division_euclidienne(a,b):
    print("Le quotient de la division de", a , "par", b , "est" , a//b , "et le reste est" , a%b)

#division_euclidienne(9, 2)

### 2

def equation_premier_degre(a,b):
    x = -b/a
    print(x)

#equation_premier_degre(5, 10)

def maximum(a,b):
    if a > b:
        return a
    return b

#print(maximum(5,10))

def maximum3(a, b, c):
    if a >= b and a >= c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

##print(maximum3(10,40000,300))

###  4

def estPair(a):
    if a%2 == 1:
        "Ce nombre n'est pas pair"
    return "Ce nombre est pair"

#print(estPair(6))

### 5

def diviseur(n,d):
    if n//d >= 1:
        return True
    return False

#print(diviseur(6,10))

###  6

def med(l):
    l = sorted(l)
    len_l = len(l)
    if len_l % 2 == 0:
        return (l[(len_l-1)/2]) + l([len_l+1]/2) / 2.0
    return l[(len_l-1)] / 2


#l = [1,2,3,4,5]
#print(med(l))

###  7

def aleatoire_1():
    print(uniform(2, 3))

#aleatoire_1()

def aleatoire_2():
    print(uniform(12, 15))

#aleatoire_2()

def aleatoire_3():
    l = []
    for i in range(0,3):
        l.append(randint(1,6))
    return l

#print(aleatoire_3())

def aleatoire_4():
    l = [0,0,0]
    l[0] = randint(1,3)
    l[1] = randint(4,7)
    l[2] = randint(8,11)
    return l

#print(aleatoire_4())

def six_est_la(l):
    if 6 in l:
        return True
    return False

#l = [4,5,9]
#print(six_est_la(l))

