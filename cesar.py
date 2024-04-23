abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def cifrar(frase, distancia):
    mensaje = frase.upper()
    
    result = ""
    for letter in mensaje:
        i=0
        if letter == " ":
            result += " "
        elif letter not in abecedario:
            result += letter
        while i < len(abecedario):
            if letter == abecedario[i]:
                puntero = i + distancia
                if puntero >= 26:
                    puntero = distancia - 1
                    result += abecedario[puntero]
                else:
                    result += abecedario[puntero]
            i+=1
    return result



def crearCifrador(distancia):
    def cifrador(mensaje):
        return cifrar(mensaje, distancia)
    return cifrador




cifrarDidier = crearCifrador(9)
cifrarMontse = crearCifrador(-9)


cifrarDidier("Hola")


def crearPareja(distancia):
    def cifrador(mensaje):
        return cifrar(mensaje, distancia)
    
    def descifrador(mensaje):
        return cifrar(mensaje, -distancia)
    
    return cifrador, descifrador

cifrador, descifrar = crearPareja(11)

print(cifrador("hola"))
print(descifrar("szwl"))