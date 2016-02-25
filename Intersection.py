class Line:

    def __init__(self, l):
        self.point = l
        x1, y1, x2, y2 = l
        self.c_x = (x1 + x2) / 2
        self.c_y = (y1 + y2) / 2

def intersection( l1, l2):
    """
    Calculer point d'intersection des deux lignes L1 et L2
    l1: Ligne
    l2: Ligne
    return: Point d'intersection
    """
    #coordonees de la lignes 1
    x1, y1, x2, y2 = l1.point
    #coordonees de la lignes 2
    x3, y3, x4, y4 = l2.point
    #
    a1 = y2 - y1
    b1 = x1 - x2
    a2 = y4 - y3
    b2 = x3 - x4
    #
    c1 = a1 * x1 + b1 * y1
    #
    c2 = a2 * x3 + b2 * y3
    #
    det = a1 * b2 - a2 * b1
    assert det, "lines are parallel"
    return (1. * (b2 * c1 - b1 * c2) / det, 1. * (a1 * c2 - a2 * c1) / det)