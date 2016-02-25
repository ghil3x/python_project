import cv2
import imutils
import numpy as np
from Intersection import Line,intersection
from scipy.spatial import distance

lowThreshold = 5 #init threshold 
max_lowThreshold = 127  #max de threshold
ratio = 3 # ratio pour le calcule de li'mage
kernel_size = 3


#img = cv2.imread('tableau_avant.png')
img = cv2.imread('IMG_4779.jpg')
#img = cv2.imread('IMG_4947.jpg')
#img = cv2.imread('IMG_4948.jpg')
#img = cv2.imread('IMG_4961.jpg')
#img = cv2.imread('IMG_4962.jpg')

#declaler deux variable pour la largeur et la longeur de l'image
h, w = img.shape[:2]
#longueur
print(h)
#largeur
print(w)

img = imutils.resize(img,350,700)
print("ETAPE 1: Conversion de l'image en gris")
# convertion de l'image en gris
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#fonction qui affiche l'image
def affiche(image):

    msg = 'Fermez pour afficher la suite'
    cv2.namedWindow(msg, cv2.WINDOW_NORMAL)
    cv2.imshow(msg, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


#fonction qui propose de choisir le threshold de l'image selon les besoin
#afin de trouver les quatre point d'intersection des lignes
def CannyThreshold(lowThreshold):
#Application du filtre Gaussian
    blur = cv2.GaussianBlur(gray,(3,3),0)
    # application du filtre canny pour la detection des contours(intersection de quatre lignes
    detected_edges = cv2.Canny(blur,lowThreshold,lowThreshold*ratio,apertureSize = kernel_size)
    dst = cv2.bitwise_and(img,img,mask = detected_edges)  # ajouter de couleurs aux bords de l'image originale.

    lines = cv2.HoughLinesP(detected_edges, 1, np.pi / 180, 100, None,  w/20, h/20)

    a, b, c = lines.shape
    for i in range(a):
        cv2.line(detected_edges, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 1,
             cv2.LINE_AA)

    t = cv2.cvtColor(detected_edges, cv2.COLOR_GRAY2BGR)

    # classification des lignes hori ou vert
    hori, vert = [], []
    for i in range(-4,4):
        for l in lines[i]:
            x1, y1, x2, y2 = l
            if abs(x2 - x1) > abs(y1 - y2):
                hori.append(Line(l))
            else:
                vert.append(Line(l))
                cv2.line(t, (x1, y1), (x2, y2), (0, 0, 255), 1,cv2.LINE_AA)

    
    # si les point ne sont pas suffisament detectees
    # agrandissement des lignes trouver au bord de l'image
    # afin de creer une nouvelle ligne
    if len(hori) < 2:
        if not hori or hori[0].c_y > h / 2:
            hori.append(Line((0, 0, w - 1, 0)))
        if not hori or hori[0].c_y <= h / 2:
            hori.append(Line((0, h - 1, w - 1, h - 1)))

    if len(vert) < 2:
        if not vert or vert[0].c_x > w / 2:
            vert.append(Line((0, 0, 0, h - 1)),)
        if not vert or vert[0].c_x <= w / 2:
            vert.append(Line((w - 1, 0, w - 1, h - 1)))

    # lignes trier selon leur point central
    hori.sort(key=lambda l: l.c_y)
    vert.sort(key=lambda l: l.c_x)

    # chercher les corners

    for l in [hori[-1], vert[0], hori[-1], vert[-1]]:
        x1, y1, x2, y2 = l.point
        cv2.line(t, (x1, y1), (x2, y2), (0, 255, 255), 1)

    # echele des petits corners
    image_points = [intersection(hori[0], vert[0]), intersection(hori[0], vert[-1]),
               intersection(hori[-1], vert[0]), intersection(hori[-1], vert[-1])]


    # echel des corners de la taille originale
    for x, y in image_points:
        cv2.circle(t, (int(x), int(y)), 1, (255, 255, 0), 3)
        print(x,'******',y)
    
    affiche(t)
    cv2.imwrite('resultat.jpg',t)

cv2.namedWindow('Canny Manuellement')
cv2.createTrackbar('Min threshold','Canny Manuellement',lowThreshold, max_lowThreshold, CannyThreshold)

#appel de la fonction
CannyThreshold(5)  # initialisation a '5'
if cv2.waitKey(10) == 27:
    cv2.destroyAllWindows()



print('image enregestrer.')
print('Au Revoir')

