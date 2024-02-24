class Time(object) :     
    def __init__(self, hh = 13, mm = 15, ss = 17):
        self.heure = hh
        self.minute = mm
        self.seconde = ss
    def afficher_heure(self) :
        print("{0}:{1}:{2}".format(self.heure, self.minute, self.seconde))

tStart1 = Time()
tStart2 = Time(19, 27, 31)

tStart1.afficher_heure()
tStart2.afficher_heure()