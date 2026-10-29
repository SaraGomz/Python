############ U2.01 fizzbuzz

def main_U2_01():
    resultado = None
    for i in range( 100):
        if i % 3 == 0 and i % 5  == 0:
            resultado = "FizzBuzz"
        elif i % 3 == 0 and not i % 5 == 0:
            resultado = "fizz"
        elif i % 5 == 0 and not i % 3  == 0:
            resultado = "buzz"
        else:
            resultado = i

        print(resultado)

# main_U2_01()

######### Fin U2.01 fizzbuzz


######### U2.02. Dirección postal

nombre = "Pepa"
apellido1 = "Soriano"
apellido2 = "Martínez"
via = "calle valencia bonita, 6"
numero = 18
codigo_postal = 46020
localidad = "Valencia"
pais = "España"


def main_U2_02(nombre,apellido1,apellido2,via,numero,codigo_postal,localidad,pais):
    print(f"Destinatario: {nombre} {apellido1} {apellido2} \n Domicilio: {via} num {numero} \n Código Postal: {codigo_postal}  Población:  {localidad},{pais} ")

# main_U2_02(nombre,apellido1,apellido2,via,numero,codigo_postal,localidad,pais)


######### Fin U2.02. Dirección postal



######### U2.03. Saludo personalizado

def main_U2_03():
    nombre = str(input("Introduce tu nombre:"))

    print(f"Hola, {nombre}")

# main_U2_03()

######### Fin U2.03. Saludo personalizado



######### U2.04. Cuenta de un restaurante
PROPINA = 18

def main_U2_04():
    comida_sin_impuesto = float(input("Introduce el importe de la comida:"))
    impuestos = int(input("Introduce el impuesto a aplicar:"))

    impuesto = imp_comida_inicial(comida_sin_impuesto,impuestos)

    comida_con_imp = impuesto + comida_sin_impuesto

    propina = calc_propina(comida_sin_impuesto,PROPINA)

    total = comida_con_imp + propina
    print(f"Comida: {comida_sin_impuesto} \n Impuesto añadido: {impuesto} \n Propina: {propina} \n Total: {total}")

def imp_comida_inicial(comida_sin_impuesto,impuestos):
    return comida_sin_impuesto * (impuestos / 100)

def calc_propina(comida_sin_impuesto, PROPINA):
    return comida_sin_impuesto * (PROPINA / 100)

# main_U2_04()

######### Fin U2.04. Cuenta de un restaurante


######### U2.05. Suma de los primeros números enteros positivos

def main_U2_05():
    numero = pedir_num()
    sumaIter = suma_iterativa(numero)
    sumaRecur = suma_recursiva(numero)

    print(f"Suma Iterativa: {sumaIter} , Suma Recursiva: {sumaRecur}")

    expresion = numero * (numero +1) /2
    print(f"Expresión: {expresion}")


def pedir_num():
    peticion = int(input("Introduce un número entero positivo"))
    bien = False
    while (bien == False):
        if peticion < 0 :
            print("Tienes que introducir un número positivo")
            peticion = int(input("Introduce un número entero positivo"))
        else:
            bien = True
    return peticion


def suma_iterativa(numero):
    suma = 0
    for i in range(1,numero + 1):
        suma += i
    return suma

def suma_recursiva(numero):
    if numero <= 0:
        return 0

    suma_n_1 = suma_recursiva(numero -1)
    # si se calcualr suma(n-1),  la suma de n =>  n + suma(n-1)
    return suma_n_1 + numero

# main_U2_05()
    
######### Fin U2.05. Suma de los primeros números enteros positivos




######### U2.06. Interés compuesto

def main_U2_06():
    saldo = float(pedir_num())

    interes = saldo * (4/100)

    for i in range(3):
        saldo += interes
        print(f"El saldo el {i} año es de : {saldo}")

# main_U2_06()

######### Fin U2.06. Interés compuesto



######### U2.07. Distancia entre dos puntos de la Tierra


######### Fin U2.07. Distancia entre dos puntos de la Tierra


######### U2.08. Conversión de temperaturas

def main_U2_08 ():
    celsius = float(input("Introduce la temperatura en celsius "))
    
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{fahrenheit} ºF")
    kelvin = celsius_a_kelvin(celsius)
    print(f"{kelvin} K")

def celsius_a_fahrenheit(celsius):
    return celsius * 9 /5 + 32

def celsius_a_kelvin(celsius):
    return celsius + 273.15

# main_U2_08()


######### Fin U2.08. Conversión de temperaturas


######### U2.09. Suma de las cifras de un número

def main_U2_09():
    numero = num_ent_cuatro()
    digitos = []
    suma = 0

    while numero > 0:
        digitos.append(numero%10)
        numero = numero // 10

    for i in digitos:
        suma += i    

    print(f"{digitos[0]} + {digitos[1]} + {digitos[2]} + {digitos[3]} = {suma}")

def num_ent_cuatro():
    peticion = int(input("Introduce un número entero positivo entre 1000 y 9999 "))
    bien = False
    while (bien == False):
        if peticion <= 1000 and peticion >= 9999 :
            print("Tienes que introducir un número positivo  entre 1000 y 9999")
            peticion = int(input("Introduce un número entero positivo "))
        else:
            bien = True
    return peticion

# main_U2_09()

######### Fin U2.09. Suma de las cifras de un número


######### U2.10. Conversión de edad humana a edad canina

def main_U2_10():
    edad = float(input("Introduce tu edad: "))
    if edad <= 0:
        print("La edad tiene q ser positiva")
    else:
        conversion = edad_canina(edad)
        print(conversion)

def edad_canina(edad):
    equivalencia = 0
    for i in range(1 , int(edad) +1):
        if i == 1 or i == 2:
            equivalencia += 10.5
        else:
            equivalencia += 4
    return equivalencia

# main_U2_10()

######### Fin U2.10. Conversión de edad humana a edad canina

#########  U2.11. Color de una casilla de ajedrez

def main_U2_11():
    casilla = input("Introduce una casilla válida para un ajedrez: ")
    lista_casilla = list(casilla)
    letra = lista_casilla[0]
    numero = int(lista_casilla[1])

    match letra:
        case "a":
            if numero % 2 == 0:
                print("Blanca")
            else:
                print("Negra")
        case "b":
            if not numero % 2 == 0:
                print("Blanca")
            else:
                print("Negra")
        case "c":
            if not numero % 2 == 0:
                print("Blanca")
            else:
                print("Negra")
        case "d":
            if not numero % 2 == 0:
                print("Blanca")
            else:
                print("Negra")
        case "e":
            if numero % 2 == 0:
                print("Blanca")
            else:
                print("Negra")
        case "f":
            if not numero % 2 == 0:
                print("Blanca")
            else:
                print("Negra")
        case "g":
            if numero % 2 == 0:
                print("Blanca")
            else:
                print("Negra")
        case "h":
            if not numero % 2 == 0:
                print("Blanca")
            else:
                print("Negra")

main_U2_11()
######### Fin U2.11. Color de una casilla de ajedrez


######### U2.12. Signo del zodiaco según la fecha de nacimiento

def main_U2_12():
    signo = ""
    fecha_cumple = str(input("Introduce tu fecha de cumpleaños dd/mm/aaaa: "))
    d,m,a = fecha_cumple.split("/")
    dia = int(d)
    mes = int(m)
    anio = int(a)


    match mes:
        case 1:
            if dia <= 19:
                signo = "Capricornio"
            else:
                signo = "Acuario"
        case 2:
            if dia <= 18:
                signo = "Acuario"
            else:
                signo = "Piscis"
        case 3:
            if dia <= 20:
                signo = "Piscis"
            else:
                signo = "Aries"
        case 4:
            if dia <= 19:
                signo = "Aries"
            else:
                signo = "Tauro"
        case 5:
            if dia <= 20:
                signo = "Tauro"
            else:
                signo = "Géminis"
        case 6:
            if dia <= 20:
                signo = "Géminis"
            else:
                signo = "Cáncer"
        case 7:
            if dia <= 22:
                signo = "Cáncer"
            else:
                signo = "Leo"
        case 8:
            if dia <= 22:
                signo = "Leo"
            else:
                signo = "Virgo"
        case 9:
            if dia <= 22:
                signo = "Virgo"
            else:
                signo = "Libra"
        case 10:
            if dia <= 22:
                signo = "Libra"
            else:
                signo = "Escorpio"
        case 11:
            if dia <= 21:
                signo = "Escorpio"
            else:
                signo = "Sagitario"
        case 12:
            if dia <= 21:
                signo = "Sagitario"
            else:
                signo = "Capricornio"

    print(f"Tu signo es {signo}")

main_U2_12()
######### Fin U2.12. Signo del zodiaco según la fecha de nacimiento