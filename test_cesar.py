from cesar import cifrar
def test_cesar_una_letra():
    assert cifrar("H", 1) == "I"