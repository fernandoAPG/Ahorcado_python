from palabras import palabras
import random
from ahorcado_diagramas import vidas_diccionario_visual

def palabra_secreta():
    secreta = random.choice(palabras)
    return secreta


def usuario():
    user_palabra = input("Ingrese letra: ").lower()
    if len(user_palabra) == 1 and user_palabra.isalpha():
        print("Letra valida")
        return user_palabra
    else:
        print("Letra invalida")
        return False

def progreso_barra(secret):
    progreso = []
    for i in secret:
        progreso += "_"
    return progreso

def diagrama_visual(v):
    if v == 7:
        print(vidas_diccionario_visual[v])
    elif v==6:
        print(vidas_diccionario_visual[v])
    elif v==5:
        print(vidas_diccionario_visual[v])      
    elif v==4:
        print(vidas_diccionario_visual[v])
    elif v==3:
        print(vidas_diccionario_visual[v])
    elif v==2:
        print(vidas_diccionario_visual[v])
    elif v==1:
        print(vidas_diccionario_visual[v])
    elif v==0:
        print(vidas_diccionario_visual[v])  
def main():
    secreta = palabra_secreta()
    letras_secreta = [i for i in secreta]
    vidas = 7
    letras_adivinadas = set()
    letras_por_adivinar = len(set(letras_secreta))
    barra_progreso = progreso_barra(secreta)
    print("====================")
    print("Bienvenido al juego")
    print("====================")
    print(" ".join(barra_progreso))
    print(f"Tienes {vidas} vidas")
    while vidas > 0 and letras_por_adivinar > 0:
        palabra_usuario = usuario()
        while palabra_usuario== False:
            print("Vuelve a ingresar Letra")
            palabra_usuario = usuario()
        if palabra_usuario in letras_secreta:
            if not palabra_usuario in letras_adivinadas:
                letras_adivinadas.add(palabra_usuario)
                letras_por_adivinar -= 1
            else:
                print("Ya usaste esta letra , ingrese otra letra")
            for y in range(len(secreta)):
                if palabra_usuario == secreta[y]:
                    barra_progreso[y] = palabra_usuario
                else:
                    pass
            print(f"Letras por adivinar: {letras_por_adivinar}")
            diagrama_visual(vidas)
            print(" ".join(barra_progreso).upper())
        else:
            if not palabra_usuario in letras_adivinadas:
                letras_adivinadas.add(palabra_usuario)
                vidas -= 1
                print(f"Tienes {vidas} vidas")
                diagrama_visual(vidas)
            else:
                print("Ya usaste esta letra, Ingrese otra letra")
                print(f"Tienes {vidas} vidas")
                diagrama_visual(vidas)
    if letras_por_adivinar==0 and vidas >0:
        print("¡Feliciades! ganaste el juego")
    else:
        print("Perdiste")
    print(f"La palabra secreta es : {secreta}")


if __name__ == "__main__":
    main()
