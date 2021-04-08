class CompteBancaire:
    def __init__(self):
        self.propietaire = "Dupont"
        self.solde = 1000
        
    def deposer(self, somme):
        self.solde = self.solde + somme
        
    def retrait(self, somme):
        self.solde = self.solde - somme
        
    def afficher(self):
        print(("Ce compte appartient a {} et dispose de {} euros").format(self.propietaire, self.solde))

    def decouvert(self):
        if self.solde <= 0:
            print(self.propietaire, "eT a decouvert")
        else:
            print(self.propietaire, "n'est pas a decouvert")

C = CompteBancaire()

#C.decouvert()