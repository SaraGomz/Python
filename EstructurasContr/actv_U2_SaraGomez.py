import random







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

# main_U2_11()
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

# main_U2_12()
######### Fin U2.12. Signo del zodiaco según la fecha de nacimiento


######### U2.13. Color de una longitud de onda

def main_U2_13():
    nanometros = float(input("Introduce nanometros: "))

    if nanometros >= 380 and nanometros <= 449 :
        print("Violeta")
    elif nanometros >= 450 and nanometros <= 494 :
        print("Azul")
    elif nanometros >= 495 and nanometros <= 569 :
        print("Verde")
    elif nanometros >= 570 and nanometros <= 589 :
        print("Amarillo")
    elif nanometros >= 590 and nanometros <= 619 :
        print("Naranja")
    else:
        print("queda fuera del intervalo visible considerado en este ejercicio")

# main_U2_13()

######### Fin U2.13. Color de una longitud de onda



######### U2.14. Año bisiesto

def main_U2_14():
    anio = int(input("Escribe un año: "))
    loes = es_bisiesto(anio)

    if loes == True:
        print(f"{anio} es un año bisiesto")
    else:
        print(f"{anio} no es un año bisiesto")

def es_bisiesto(anio):
    comprobacion = None

    if anio % 400 == 0:
        comprobacion = True
    elif anio % 100 == 0:
        comprobacion = False
    elif anio % 4  == 0:
        comprobacion = True
    else:
        comprobacion = False

    return comprobacion

# main_U2_14()

######### Fin U2.14. Año bisiesto



######### U2.15. Generación de una contraseña aleatoria

def main_U2_15():
    contra = generar_contrasena()
    print(contra)

def generar_contrasena():
    longitud = random.randint(7,10)
    caracteres = []

    for i in range(longitud):
        codigo_ascii = random.randint(33,126)
        caracter = chr(codigo_ascii)
        caracteres.append(caracter)

    final_password = "".join(caracteres)
    return final_password

# main_U2_15()

######### Fin U2.15. Generación de una contraseña aleatoria



######### U2.16. Comprobación de una contraseña

def main_U2_16():
    contra = generar_contrasena()
    comprobacion = es_contrasena_valida(contra)

    if comprobacion:
        print("La contraseña es válida")
    else: 
        print("La contraseña no es válida")
def es_contrasena_valida(contrasena):
    cumple = None
    if len(contrasena) >= 8:
        if any("A" <= i <= "Z" for i in contrasena):
            if any(j.islower() for j in contrasena):
                if any(x.isdigit() for x in contrasena):
                    cumple = True
    else:
        cumple = False

    return cumple

# main_U2_16()
######### Fin U2.16. Comprobación de una contraseña



######### U2.17. Generación de una contraseña que cumpla las condiciones

def main_U2_17():
    valida = None
    cont = 0
    while not valida:
        cont += 1
        contrasena = generar_contrasena()
        valida = es_contrasena_valida(contrasena)

    print(f"contraseña apta: {contrasena} intentos requeridos: {cont}")

# main_U2_17()


######### Fin U2.17. Generación de una contraseña que cumpla las condiciones



######### U2.18. Siguiente número primo

def main_U2_18():
    numero = int(input("Introduce un numero entero: "))
    comprobar = es_primo(numero)

    if comprobar:
        print(f"El número {numero} es primo")
    else: 
        print(f"El número {numero} no es primo")

def es_primo(numero):
    es_primo = True
    if numero < 2:
        es_primo = False
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False  

    return es_primo

# main_U2_18()    
######### Fin U2.18. Siguiente número primo


#########  U2.19 Número de días de un mes

def main_U2_19():
    mes = int(input("Introduce un mes, del 1 al 12: "))
    anio = int(input("introduce un año aaaa: "))
    dias = dias_del_mes(mes, anio)

    print(f"el mes {mes} en el año {anio} tiene en total {dias} dias")

def dias_del_mes(mes, anio):
    dias = 0
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dias = 30
    elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or  mes == 12:
        dias = 31
    else:
        bisiesto = es_bisiesto(anio)
        if bisiesto:
            dias = 29
        else:
            dias = 28
    return dias

main_U2_19()
######### Fin  U2.19 Número de días de un mes


#########  U2.20. Fechas mágicas

def main_U2_20():
    for anio in range(1901, 2001):
        for mes in range(1, 13):
            for dia in range(1, dias_del_mes(mes, anio) + 1):

                if es_fecha_magica(dia, mes, anio):
                    print(f"{dia:02d}/{mes:02d}/{anio} (porque {dia} * {mes} = {anio % 100})")

def  es_fecha_magica(dia, mes, anio):
    dos_ultimas_cifras = anio % 100

    if (dia * mes) == dos_ultimas_cifras:
        return True
    else:
        return False


def separar_y_validar_fecha(fecha_str):
    partes = fecha_str.split("/")
    if len(partes) != 3:
        return None

    dia_str, mes_str, anio_str = partes


    if not (dia_str.isdigit() and mes_str.isdigit() and anio_str.isdigit()):
        return None

    dia = int(dia_str)
    mes = int(mes_str)
    anio = int(anio_str)

    if anio <= 0 or mes < 1 or mes > 12:
        return None

    max_dias = dias_del_mes(mes, anio)

    if dia < 1 or dia > max_dias:
        return None

    return dia, mes, anio
#########  Fin   U2.20. Fechas mágicas

import math


def distancia_tierra(latitud1, longitud1, latitud2, longitud2):
  """Recibe las coordenadas de dos puntos en grados, las convierte a radianes

  y calcula la distancia en kilómetros sobre una esfera de radio 6371.01 km.
  Devuelve el valor numérico de la distancia.
  """
  # 1. Convertir los grados a radianes
  t1 = math.radians(latitud1)
  g1 = math.radians(longitud1)
  t2 = math.radians(latitud2)
  g2 = math.radians(longitud2)

  # 2. Aplicar la fórmula trigonométrica
  # argumento_acos = sin(t1)*sin(t2) + cos(t1)*cos(t2)*cos(g1 - g2)
  argumento = math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(
      t2
  ) * math.cos(g1 - g2)

  # 3. NOTA IMPORTANTE: Limitar el argumento al intervalo [-1, 1]
  # para evitar errores de precisión en coma flotante con math.acos()
  if argumento > 1.0:
    argumento = 1.0
  elif argumento < -1.0:
    argumento = -1.0

  # 4. Calcular la distancia final
  radio_tierra = 6371.01
  distancia = radio_tierra * math.acos(argumento)

  return distancia


def main_U2_07():
  print("--- CÁLCULO DE DISTANCIA ENTRE DOS PUNTOS DE LA TIERRA ---")

  # Solicitamos las coordenadas de la primera ciudad/punto
  lat1 = float(input("Introduce la latitud del primer punto (-90 a 90): "))
  lon1 = float(input("Introduce la longitud del primer punto (-180 a 180): "))

  # Solicitamos las coordenadas de la segunda ciudad/punto
  lat2 = float(input("Introduce la latitud del segundo punto (-90 a 90): "))
  lon2 = float(input("Introduce la longitud del segundo punto (-180 a 180): "))

  # Llamamos a la función para obtener la distancia
  distancia_calculada = distancia_tierra(lat1, lon1, lat2, lon2)

  # Mostramos el resultado con dos cifras decimales usando formato :.2f
  print(
      f"\nLa distancia entre los puntos es de"
      f" **{distancia_calculada:.2f} km**."
  )


# Ejecutamos el programa principal
if __name__ == "__main__":
  main_U2_07()