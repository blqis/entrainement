from random import *

###  1

def entier(n):
    if n//2 == 0:
        return "Ce nombre est bel et bien un entier."
    return "Ce nombre n'est pas un entier."

#print(entier(5))

###  2


def mention(l):
    if sum(l)//len(l) >= 10:
        return "admis"
    elif sum(l)//len(l) >= 8 and sum(l)//len(l) < 10:
        return "rattrapage"
    elif sum(l)//len(l) < 8:
        return "refusé"

#l = [10, 12, 5, 6, 20]
#print(mention(l))

###  3

def maximum_mdp(s):
    if len(s) <=  10:
        return True
    return False

#l = "ndej"
#print(maximum_mdp(l))

def entre_mdp(s):
    if len(s) >= 4 and len(l) <= 12:
        return True
    return False

#print(entre_mdp(l))

def contient_e_mdp(s):
    if "e" in s:
        return True
    return False

#print(contient_e_mdp(l))

### 5


def lancer_de_de(nbe_fois, chiffre, total):
    count = 0
    for i in range(0,nbe_fois):
        lancer = randint(1,6)
        if lancer == chiffre:
            count+=1
    if total == count:
        print("Vrai")
    else:
        print("Non.", "Le chiffre voulu est apparu", count, "fois.")

#lancer_de_de(1, 2, 1)


###  6

def tirage():
    a , b, c = 1, 2, 3
    boule_tiree = randint(1,3)
    if boule_tiree == a:
        print("La boule tirée est blanche.")
    elif boule_tiree == b:
        print("La boule tirée est verte.")
    elif boule_tiree == c:
        print("La boule tirée est bleue.")


#tirage()

def tirage_de_deux():
    a , b, c = 1, 2, 3
    boule_tiree = randint(1,3)
    if boule_tiree == a:
        print("La boule tirée est blanche.")
    elif boule_tiree == b:
        print("La boule tirée est verte.")
    elif boule_tiree == c:
        print("La boule tirée est bleue.")










