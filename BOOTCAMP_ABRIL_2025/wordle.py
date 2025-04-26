## haremos un wordle.

#defiir palabra a encontrar
palabra_a_encontrar = 'holas'

#definir intentos
cant_intentos = 6
#definir cantidad de letras
cantidad_de_letras = 5
#comparamos las palabras

def verificar_palabra_ingresada(parabra_secreta, palabra_ingresada):
    '''
    esta funcion verifica si las posiciones son correctas, si existe en la palabra o si no existe
    
    '''
    resultado = []
    for posicion in range(cantidad_de_letras):
        posicion_y_valor_coinciden = parabra_secreta[posicion] == palabra_ingresada[posicion]
        valor_coincide = palabra_ingresada[posicion] in parabra_secreta
        if posicion_y_valor_coinciden:
            resultado.append('['+ palabra_ingresada[posicion] +']')
        elif valor_coincide:
            resultado.append('('+ palabra_ingresada[posicion] +')')
        else:
            resultado.append(palabra_ingresada[posicion])
    return resultado


#hacer la grilla
def imprimir_grilla(lista):
    for elemento in lista:
        print(elemento)


#bienvenida al wordle

'''
Las reglas son simples: 
- adivina la palabra oculta en 6 intentos. 
- Cada intento debe ser una palabra valida
- las letras entre [asi] significan que esta es correcta en posicion y valor
- las letras entre (asi) significan que esta existe dentro de la palabra mas no es la posicion correcta

'''

#para la grilla
grilla = []



#restar la cantidad de intentos
while cant_intentos > 0:
    print(f'te quedan {cant_intentos}')
    palabra_ingresada = input('ingrese la palabra: ')
    cant_intentos -= 1

    #verificamos las palabras
    if len(palabra_ingresada) != cantidad_de_letras:
        print(f'ingrese una palabra con {cantidad_de_letras} letras')
        continue
    else:
        linea_verificada = verificar_palabra_ingresada(palabra_a_encontrar, palabra_ingresada)
        grilla.append(linea_verificada)
    imprimir_grilla(grilla)
    if palabra_ingresada == palabra_a_encontrar:
        print('ganaste')
        break
    else:
        print('game over')
        







# def validar_palabra(palabra_ingresada):
#     cantidad_de_letras_user = len(palabra_ingresada)
#     while cantidad_de_letras_user < cantidad_de_letras:
        
