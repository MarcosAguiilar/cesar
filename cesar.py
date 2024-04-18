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


print(cifrar('hola que tal?', 1))