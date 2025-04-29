#crear una tarjeta personal. en input va elegir


#modificar datos
#eliminar datos

#funcion para validar datos
def validar_dato(dato):
    '''
    funcion para validar el ingreso de datos para los procesos
    '''
    while dato != 'C' and dato != 'M' and dato != 'E'and dato != 'F':
        dato = input('''SOLO debe ingresar una letra...
                    vuelva a intentar, recuerde que 
                    si quiere añadir mas datos ingrese "C" 
                    si quiere modificar un dato oprima "M" 
                    si quiere eliminar oprima "E"
                    Si desea finalizar oprima "F" 
                     ''').upper()
    return dato


# validamos existencia en diccionario
def validar_keys(dato,diccionario_keys):
    '''
    funcion para validar claves
    '''
    while not(dato in diccionario_keys) and dato.lower() != 'f':
        dato = input('ingrese un dato correcto.. vuelva a intentar o en su defecto oprima "F" para terminar')
        print(diccionario_keys)
    return dato
# C para crear
# M para modificar
# E eliminar
# L listar

input('BIENVENIDO AL ELABORADOR DE TARJETAS PERSONALES, VAMOS A CREARLE UNA TARJETA. APRETE ENTER PARA CONTINUAR...')
tarjeta = {}
#crear el primer dato
clave = input('\n ingrese que titulo desea ingresar... ')
valor = input(f'\n ingrese su {clave}: ')
print('\n')
tarjeta[clave] = valor
print(tarjeta)

while True:
    # # vamos a pedirle que ingrese que datos quiere
    # clave = input('ingrese que titulo desea ingresar...')
    # valor = input(f'ingrese el valor de {clave}...')
    # tarjeta[clave] = valor
    # print(tarjeta)
    decision = validar_dato(input('''
                                  
si quiere añadir mas datos ingrese "C"; 
si quiere modificar un dato oprima "M" 
y si quiere eliminar oprima "E".'
Si desea finalizar oprima "F"

ingrese la letra: ''').upper())
    if decision.upper() == 'C':#crear datos nuevos
        clave = input('ingrese que titulo desea ingresar: ')
        valor = input(f'\n ingrese el valor de {clave}:')
        tarjeta[clave] = valor
        print(tarjeta)
        print('\n')
        #debe simplemente cargar mas datos
        continue
    elif decision.upper() == 'M': #modificar valores
        #debe poder modificar
        #se debe validar el ingreso de las claves
        # comparar con las keys y si no coincide hacer una validacion
        print(tarjeta.keys())
        dato_a_modificar = validar_keys(input('\n elija el titulo a modificar: '),tarjeta.keys())
        if dato_a_modificar.upper() == 'F':
            print(f'\n la lista final queda asi: \n {tarjeta}')
            break
        else:
            tarjeta[dato_a_modificar] = input(f'\n ingrese el nuevo {dato_a_modificar}: ')
            print(tarjeta)
            print('\n')
    elif decision.upper() == 'E':
        print(tarjeta.keys())
        dato_a_eliminar = validar_keys(input('\n elija el dato a eliminar: '),tarjeta.keys())
        if dato_a_eliminar.upper() == 'F':
            print(f'\n la lista final queda asi: \n {tarjeta}')
            break
        else:
            print(f'\n se va eliminar {dato_a_eliminar}')
            del tarjeta[dato_a_eliminar]
            print(f'queda de la siguiente forma: \n {tarjeta}')
            print('\n')
    elif decision.upper() == 'F':
        print(f'\n la lista final queda asi: \n {tarjeta}')
        break


