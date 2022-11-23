import datetime
from copy import copy
class Duree :
    def __init__(self, h: int, m: int, s: int):
        """
        @pre: h, m et s sont des entiers positifs (ou zéro)
              m et s sont < 60
        @post: Crée une nouvelle durée en heures, minutes et secondes.
        """

        if m > 59 or m < 0 or s > 59 or s < 0 or h < 0:
            raise ValueError

        else:
            self.hour = h
            self.minute = m
            self.second = s

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def to_secondes(self):
        """
        @pre:  -
        @post: Retourne le nombre total de secondes de cette instance de Duree (self).
        Par exemple, une durée de 8h 41m 25s compte 31285 secondes.
        """
        return (self.hour * (60**2)) + (self.minute * 60) + (self.second)

    def delta(self, d):
        """
        @pre:  d est une instance de la classe Duree
        @post: Retourne la différence en secondes entre cette durée (self)
               et la durée d passée en paramètre.
               Cette valeur renovoyée est positif si cette durée (self)
               est plus grand que la durée d, négatif sinon.
        Par exemple, si cette durée (self) est 8h 41m 25s (donc 31285 secondes)
        et la durée d est 0h 1m 25s, la valeur retournée est 31200.
        Inversement, si cette durée (self) est 0h 1m 25s et la durée
        d est 8h 41m 25s, alors la valeur retournée est -31200.
        """
        return (self.to_secondes()) - (d.to_secondes())

    def apres(self, d):
        """
        @pre:  d est une instance de la classe Duree
        @post: Retourne True si cette durée (self) est plus grand que la durée
               d passée en paramètre; retourne False sinon.
        returns: True if self is > than d. Else, returns False
        """
        return self.to_secondes() > d.to_secondes()

    def ajouter(self, d):
        """
        @pre:  d est une instance de la classe Duree
        @post: Ajoute une autre durée d à cette durée (self),
               corrigée de manière à ce que les minutes et les secondes soient
               dans l'intervalle [0..60[, en reportant au besoin les valeurs
               hors limites sur les unités supérieures
               (60 secondes = 1 minute, 60 minutes = 1 heure).
               Ne retourne pas une nouvelle durée mais modifié la durée self.
        """
        sec = (self.second + d.second)
        min = (self.minute + d.minute)
        hour = (self.hour + d.hour)
        count_min = sec // 60
        min2 = min + count_min
        count_hour = min2 // 60
        hour2 = hour + count_hour
        self.hour = hour2
        self.minute = min2 % 60
        self.second = sec % 60
        return self



class Chanson :
    def __init__(self, t: str, a: str, d):
        if isinstance(t, str) and isinstance(a, str):
            self.titre = t
            self.auteur = a
            self.duree = d
        else:
            raise TypeError
    def __str__(self):
        """
           @pre:  -
           @post: Retourne un string décrivant cette chanson sous le format
                  "TITRE - AUTEUR - DUREE".
                  Par exemple: "Let's_Dance - David_Bowie - 00:04:05"
        """
        return f"{self.titre} - {self.auteur} - {self.duree}"

class Album :
    def __init__(self, numero: int):
        if isinstance(numero, int):
            self.num = numero
            self.song_list = []
            self.duration = Duree(0, 0, 0)
            self.time_limit = Duree(1, 15, 0)
        else:
            raise TypeError

    def add(self, chanson):
        '''
        args: an object from the class 'Chanson'
        This function add a song to a list belonging to an object from class 'Album' and also add the duration of the song
        to the album total duration
        return: False if the album list contains 100 songs or the album total duration is longer than 1h15 min.
        Else, it returns True
        '''
        d = copy(self.duration)
        if (len(self.song_list)) == 100 or d.ajouter(chanson.duree).apres(self.time_limit):
            return False
        else:
            self.song_list.append(chanson)
            self.duration.ajouter(chanson.duree)
            return True

    def __str__(self):
        return f"Album {str(self.num)} {str(len(self.song_list))} chansons, {str(self.duration)}\n" + "\n".join([str(e) for e in self.song_list])
if __name__ == "__main__":
    # Grâce à la ligne ci-dessus, le code ci-dessous ne sera exécuté que si on n'exécute ce fichier directement.
    # Ceci nous permet d'éviter que le code ci-dessous sera exécuté lorsqu'on fait un import de ce fichier,
    # par exemple dans notre fichier test.py
    with open('music-db.txt', 'r') as f:
        num = 1
        album_list = [Album(num)]
        for line in f.readlines():
            lst = line.strip('\n').split()
            song = Chanson(lst[0], lst[1], Duree(0, int(lst[2]), int(lst[3])))
            if not album_list[-1].add(song):
                num += 1
                album_list.append(Album(num))
                album_list[-1].add(song)

        for i in range(len(album_list)):
            print(f"{album_list[i]}\n")

