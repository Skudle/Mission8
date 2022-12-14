##############################
# Tests pour la classe Duree #
##############################
# Kim Mens, 30-10-2021, à compléter par les étudiants

# Pour le moment, pour tester votre programme orienté objet
# vous allez encore utiliser les instructions "assert" comme
# dans les missions 5 à 7. 
# (Dans une mission futur nous introduirons le nouveau mécanisme
#  des tests unitaires qui est encore mieux approprié pour tester
#  du code orienté objet.)

# D'abord on doit importer les classe à tester
from mission8 import Duree, Chanson, Album

# CREATION DE QUELQUES OBJETS DE LA CLASSE Duree A TESTER
d0 = Duree(0,0,0)
d1 = Duree(10,20,59)
d2 = Duree(8,41,25)
d4 = Duree(0, 0, 0)
# FONCTION POUT TESTER LA METHODE __str__ DE LA CLASSE Duree
def test_Duree_str() :
    assert d1.__str__() == "10:20:59", "Test 1 Duree __str__"
    assert d2.__str__() == "08:41:25", "Test 2 Duree __str__"
    
# FONCTION POUR TESTER LA METHODE toSecondes DE LA CLASSE Duree
def test_Duree_to_secondes() :
    assert d1.to_secondes() == 37259, "Test 1 Duree toSecondes"
    assert d2.to_secondes() == 31285, "Test 2 Duree toSecondes"
    assert d4.to_secondes() == 0, "Test 3 Duree toSecondes"

# FONCTION POUR TESTER LA METHODE delta DE LA CLASSE Duree
def test_Duree_delta():
    assert d1.delta(d2) == 5974, "Test 1 Duree Delta"
    assert d2.delta(d1) == -5974, "Test 2 Duree Delta"
    assert d0.delta(d4) == 0, "Test 3 Duree Delta"

    
# FONCTION POUR TESTER  LA METHODE apres DE LA CLASSE Duree
def test_Duree_apres():
    assert d1.apres(d2),     "Test 1 Duree apres"
    assert not d0.apres(d1), "Test 2 Duree apres"
    assert not d0.apres(d4),  "Test 3 Duree apres"
    
# FONCTION POUR TESTER LA METHODE ajouter DE LA CLASSE Duree
def test_Duree_ajouter():
    assert d0.ajouter(d1) == d0, "Test 1 Duree ajouter"
    assert d0.ajouter(d4) == d4 or d0, "Test 2 Duree ajouter"

def test_error_init():
    try:
        d5 = Duree(-10, -9, -8)
        print("Constructor function doesn't throw an error when args are neg")
    except Exception as e:
        if isinstance(e, ValueError):
            print("First test error passed")
        else:
            print(f"Your function doesn't throw the asked exception: {repr(e)} instead of ValueError")

    try:
        d5 = Duree(61, 62, 62)
        print("Constructor function doesn't throw an error when args are neg")
    except Exception as e:
        if isinstance(e, ValueError):
            print("Second test error passed")
        else:
            print(f"Your function doesn't throw the asked exception: {repr(e)} instead of ValueError. Your object {d5} is must be higher than higher or equal to 0 or lower or equal to 59")


# APPEL DES DIFFERENTES FONCTIONS TEST
test_Duree_str()
test_Duree_to_secondes()
test_Duree_delta()
test_Duree_apres()
test_Duree_ajouter()
test_error_init()
################################
# Tests pour la classe Chanson #
################################

# CREATION DE QUELQUES OBJETS DE LA CLASSE Chanson A TESTER
c1 = Chanson("Let's Dance", "David Bowie", Duree(0,4,5))
c2 = Chanson("Je suis un sniper", "Locklear", Duree(0,1,38))

def test_chanson_error_init():
    try:
        c3 = Chanson(88, 4, Duree(0, 2, 4))
        print("test failed")
    except TypeError:
        print("Third test error passed")

# FONCTION POUR TESTER LA METHODE __str__ DE LA CLASSE Chanson
def test_Chanson_str(chanson) :
    assert c1.__str__() == "Let's_Dance - David_Bowie - 00:04:05", "Test 1 Chanson __str__"
    assert c2.__str__() == "Je_suis_un_sniper - Locklear - 00:01:38", "Test 2 Chanson __str__"



# APPEL DES DIFFERENTES FONCTIONS TEST
test_Chanson_str(c1)
test_chanson_error_init()

##############################
# Tests pour la classe Album #
##############################
a1 = Album(1)
a2 = Album(2)
a4 = Album(4)
Squeezie = Chanson("Placement de produit", "Squeezie", Duree(0, 4, 24))
Squeezie2 = Chanson("Placement de produit", "Squeezie", Duree(0, 0, 0))
a6 = Album(6)
a5 = Album(5)


# CREATION D'UN OBJET DE LA CLASSE Album A TESTER
def test_album_str():
    try:
        a3 = Album("ere")
    except TypeError:
        print("Fourth test passed")
assert a1.__str__() == "Album 1 0 chansons, 00:00:00\n"
assert a2.__str__() == "Album 2 0 chansons, 00:00:00\n"

# FONCTION POUR TESTER LA METHODE add DE LA CLASSE Album
def test_add():
    assert a4.add(Squeezie) == True
    assert a4.song_list[0] == Squeezie
    for i in range (99):
        a5.add(Squeezie2)
    assert a5.add(Squeezie) == True

    for o in range (100):
        a6.add(Squeezie2)
    assert a6.add(Squeezie2) == False
    assert a4.duration.to_secondes() == Squeezie.duree.to_secondes()


# APPEL DES DIFFERENTES FONCTIONS TEST
test_album_str()
test_add()

#####################################
# Test du comportement du programme #
#####################################
def test_program_behavior(line_num):
    with open('music-db.txt', 'r') as f:
        num = 1
        album_list = [Album(num)]
        for i in range(line_num):
            line = f.readline()
            lst = line.strip('\n').split()
            song = Chanson(lst[0], lst[1], Duree(0, int(lst[2]), int(lst[3])))
            if not album_list[-1].add(song):
                num += 1
                album_list.append(Album(num))
                album_list[-1].add(song)
        return(f"{album_list[0]}")
assert test_program_behavior(3) == '''Album 1 3 chansons, 00:13:47
Let's_Dance - David_Bowie - 00:04:05
Relax - Frankie_Goes_To_Hollywood - 00:03:54
Purple_Rain - Prince - 00:05:48'''