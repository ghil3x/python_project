Bonjour, 
ceci est le premier commit pour le projet Python2015 avec Mr Pascal VANIER.

Voici ce que nous avons pu faire jusqu'à la : 
	1-Lecture de l'image
	2-Convertion de l'image en gris
	3-Application du filtre Canny pour afficher l'image en en noir et blanc
	
La suite etant de trouver les lignes du tableau avec le filtre HoughLines qui nous affiches toutes les lignes disponible dans l'image.
La suite sera, choisir les lignes qui nous intiresse et trouver leur intersection pour faire le redressment.

------Ajout du filtre Gaussian.
------Modification de la methode de HoughLinesP au lieu de HoughLines.
------Création d'une fonction "affiche" a laquelle nous faisons appel pour affiche l'image résultante des testes.

-----Ajour du fichier intersection avec 
    -Ajout de la fonction d'intersection de deux lignes 
    -Aussi la définition de la classe Line

-----Ajout de la fonction qui propose de choisir le threshold de l'image selon les besoin de l'image a tester
afin de trouver les quatre point d'intersection des lignes

-----Nous avons des problemes pour le redressement de l'image, ca affiche en premiere la bonne image avec les quatre points récuperer,
ensuite, elle affiche toutes les images avec :
    les coordonnées enregistrer chaque fois que nous deplacons le curseur.
    
Cette méthode, nous la rajouterrons demain.