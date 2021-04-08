#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <time.h>






/*Noeud*/
typedef struct noeud_s * ab_t;
typedef unsigned int elt_t;
struct noeud_s{
  elt_t etiq;
  ab_t gauche;
  ab_t droit;
};


/*Element*/
typedef struct Element Element;
struct Element
{
    noeud_s noeud;
    Element *suivant;
};

/*File*/
typedef struct File File;
struct File
{
    Element *premier;
};


double p = 0.25;

/*Création d'un noeud*/
noeud_s creer_noeud(ab_t, int);

/*Fonctions de file*/
void enfiler(File *, noeud_s);
noeud_s defiler(File *);

/*Hauteur d'un arbre*/
int hauteur_c(ab_t);

/*Fonctions de calcul*/
unsigned int min(unsigned int, unsigned int);
unsigned int max(unsigned int, unsigned int);
double moyenne(int *);
double ecart_type(int, int *);




int main()
{
	File file;
	file.premier = NULL;

	FILE* fichier = NULL;

	int nocreation ;

	int largeur_n = 0;
	int hauteur_n = 0;

	int tirage_0 ; 		   			 
	int tirage_1 ;		   		      
	int tirage_2 ;  	   

	File arbre[1000];		  
                              
	int hauteur[1000] ;  		  
	int largeur[1000] ;	
	int mesure_h_1;
	int mesure_h_2;

	double minimum_hauteur, maximum_hauteur, minimum_largeur, maximum_largeur = 0 ;

	srand(time(NULL));


int random = 0;






	for(int i = 0; i<1000; i++)
	{
		nocreation = 0;

		hauteur_n, largeur_n = 0;

		tirage_0 = rand();
		random = p*RAND_MAX;
		printf("%d, %d, %d", tirage_0, RAND_MAX, random);
		if(tirage_0 >0)
		{

            noeud_s Racine ;	
			printf("Est-ce que ça marche ?\n");
			Racine.etiq = nocreation;
			Racine.gauche = NULL;
			Racine.droit = NULL;

			enfiler(&arbre[i], Racine);	 					
			enfiler(&file, Racine);			
		}




		while (file.premier != NULL)
		{
	
			tirage_1 = rand();

			mesure_h_1 = hauteur_c(file.premier->noeud);

			if(tirage_1 >= p*RAND_MAX && tirage_1 <= RAND_MAX /*&& tirage_2>= p*RANDMAX && tirage_2<= RANDMAX */)
			{
				enfiler(&file, creer_noeud(file.premier->noeud->gauche, nocreation));
				largeur_n++;
			}
            tirage_1 = rand();
            if (tirage_1 >= p*RAND_MAX && tirage_1 <= RAND_MAX)
            {
                enfiler(&file, creer_noeud(file.premier->noeud->droit, nocreation));
                largeur_n++;
            }

				defiler(&file);								
				enfiler (&arbre, file.premier);			
			}
			mesure_h_2 = hauteur_c(file.premier->noeud);		

			if (mesure_h_1 != mesure_h_2)
				{
					largeur[i] = max(largeur[i], largeur_n);		
					largeur_n = 0;
				}
            hauteur[i] = hauteur_c(arbre[i].premier->noeud);
		}

	/*-------------- T R A I T E M E N T --------------------*/
	for (int i = 0; i++; i<1000)
	{
		minimum_hauteur = min(minimum_hauteur, hauteur[i]);
		maximum_hauteur = max(minimum_hauteur, hauteur[i]);

		minimum_largeur = min(minimum_largeur, largeur[i]);
		maximum_largeur = max(minimum_largeur, largeur[i]);
	}

	fichier = fopen("donnees.txt", "w+");
    if (fichier != NULL)
    {
        fprintf(fichier,
				"Moyenne Hauteur : %f \t Moyenne Largeur : %f \t Ecart-Type Hauteur : %f \t Ecart-Type Largeur : %f \n Hauteur Minimum : %d \t Hauteur Maximum : %d \t Largeur Minimum : %d \t Largeur Maximum : %d",moyenne(hauteur[1000]),	moyenne(largeur[1000]), ecart_type(moyenne(hauteur[1000]), hauteur[1000]), ecart_type(moyenne(largeur[1000]), largeur[1000]),minimum_hauteur, maximum_hauteur, minimum_largeur, maximum_largeur);
        fclose(fichier);
    }

	return EXIT_SUCCESS;
}






noeud_s creer_noeud(ab_t node, int nocreation)
{
	nocreation++;											 
	node->etiq = nocreation;
	node->gauche = NULL;
	node->droit = NULL;

	return node;
}



void enfiler(File *file, noeud_s nvNoeud)
{
    Element *nouveau = (Element*)malloc(sizeof(Element));		
    if (file == NULL || nouveau == NULL) exit(EXIT_FAILURE);	

    nouveau->noeud = nvNoeud;									
    nouveau->suivant = NULL;									

    if (file->premier != NULL)									
    {
        Element *elementActuel = file->premier;					
        while (elementActuel->suivant != NULL) elementActuel = elementActuel->suivant;

        elementActuel->suivant = nouveau; 					
    }
    else file->premier = nouveau;								
}


noeud_s defiler(File *file)
 {
	if(file == NULL) return (EXIT_FAILURE); 					

	noeud_s noeudDefile = NULL;									

	if(file->premier!=NULL)										
	{
		Element *elementDefile = file->premier;					

		noeudDefile = elementDefile->noeud;
		file->premier = elementDefile->suivant;
		free(elementDefile);									
	}

	return noeudDefile ;
 }

int hauteur_c(ab_t arbustre)
{
	return 1 + max(hauteur_c(arbustre->gauche), hauteur_c(arbustre->droit));
}


double moyenne(int* t)
{
	int somme = 0;
	for(int i = 0; i++; i<1000)
	{
		somme = somme + t[i];
	}

	return somme/1000;
}

double ecart_type(int moyenne, int* t){

	double somvar = 0;
	for(int i = 0; i++; i<1000)
	{
		somvar = somvar + pow(t[i]-moyenne, 2.0);
	}

	return sqrt(somvar/1000);
}

unsigned int max(unsigned int a, unsigned int b)
{
	return (a>=b)? a : b ;
}

unsigned int min(unsigned int a, unsigned int b)
{
	return (a<=b)? a : b ;
}