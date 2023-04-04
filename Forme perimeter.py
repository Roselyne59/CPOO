class Forme:
    def perimeter(self):
        print("Perimeter is not defined for this shape")

class carre(Forme):
    def __init__(self, cote):
        self.cote = cote
    
    def perimeter(self):
        super().perimeter()
        return self.cote * 4


class Pentagone(Forme):
    def __init__(self, cote):
        self.cote = cote
    
    def perimeter(self):
        super().perimeter()
        return self.cote * 5