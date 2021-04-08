

#Exercice 1
B={"Les misérables": ["Victor Hugo",1],"Notre Dame de Paris": ["Victor Hugo",2],"Quatrevingt-treize": ["Victor Hugo",0],"Harry Potter à l'école des sorciers": ["J. K. Rowling",2],"Harry Potter et la chambre des secrets": ["J. K. Rowling",1],"Harry Potter et le prisonnier d'Azkaban": ["J. K. Rowling",0],"Harry Potter et la coupe de feu": ["J. K. Rowling",3],"Harry Potter et l'ordre du phoenix": ["J. K. Rowling",1],"Harry Potter et le prince de sang-mélé":["J. K. Rowling",0],"Harry Potter et les reliques de la mort":["J. K. Rowling",2],"PHP pour les nuls":["Laure Dinateur",5]}

def Auteurs(D):
    a=[]
    for value in D.values():
        if value[0] not in a:
            a.append(value[0])
    return a

def TitresDispo(D):
    a=[]
    for key,value in D.items():
        if value[1] not in a:
            if value[1]>0:
                a.append(key)
    return a

def TitresAuteur(D,nom):
    a=[]
    for key,value in D.items():
        if value[0]==nom:
            if value[1]>0:
                a.append(key)
    return a