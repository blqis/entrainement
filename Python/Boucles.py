from random import *

###  1

i,s = int, int

s = 1
for i in range(1,3):
    s *= 10

#print(s)

###  2

a = 100
for i in range(1,4):
    a += 25

#print(a)

###  3

l = 20000
for i in range(15):
    l +=100

#print(l)

###  4

def suite(n):
    s = 0
    for i in range(1,n+1):
        s += i
        if s > 12520:  # quel moment on depasse 125200, eventuelle optimisation suite(n, m) if s >m:
            return i
    return s


#print(suite(500))

def suite_2(n):
    if n == 1:
        return 1
    return suite_2(n-1) + n

#print(suite_2(158))

###  5

def prix(n):
    s = 8
    for i in range(n):
        s *= 1.05
        if s >= 11:
            return (i+1), s
    return s

#print(prix(7))


###  6

def lancer_de_de(n):
    count = 0
    for i in range(0,n):
        lancer = randint(1,6)
        if lancer == 6:
            count+=1
    frequence = count/n
    print("Pour", n, "lancers,", "on a obtenu", count, "fois 6, avec une fréquence d'apparition de", frequence, ".")

#lancer_de_de(5)

### 7

def feu():
    feu_rouge = 0
    for i in range(0,3):
        feux = randint(1,2)
        if feux == 2:
            feu_rouge += 1
    if feu_rouge == 1:
        print("Nicolas a rencontré un seul feu rouge ce matin.")
    else:
        print("Nicolas a rencontré", str(feu_rouge), "feux rouges ce matin.")

#feu()


