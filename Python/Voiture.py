class Voiture:
  def __init__(self, marque, couleur):
    marque = "Ford"
    couleur = "rouge"
    pilote = "personne"
    vitesse = 0
    self.marque = marque
    self.couleur = couleur
    self.vitesse = vitesse
    self.pilote = pilote

  def choix_conducteur(self, nom):
    self.pilote = nom

  def acceler_vitesse(self, vitesse2):
    if self.plote == "personne":
      print("Un pilote n'est pas encore designe")
    else:
      self.vitesse = self.vitesse + vitesse2

  def afficher_tout(self):
    print(("Cette voiture est une {} de couleur {} avec pour conducteur {} et allant a une vitesse de {}").format(self.marque, self.couleur, self.pilote, self.vitesse))

V = Voiture("Mercedes", "noire")
V.choix_conducteur("Chaima")
V.acceler_vitesse(-37)
V.afficher_tout()
