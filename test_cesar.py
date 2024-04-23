import cesar 
def test_cesar_una_letra():
    assert cesar.cifrar("H", 1) == "I"

def test_crear_cifrador():
    cifrar3 = cesar.crearCesar(3)
    descifrar3 = cesar.crearCesar(-3)

    assert cifrar3("H") == "K"
    assert descifrar3("K") == "H"