from datos import resistencias, voltaje, frecuencia, capacitancia, inductancia


def menu():
    print("Bienvenido al programa de circuitos eléctricos!")
    print("Seleccione una opcion: ")
    print("1. Circuito resistivo")
    print("2. Circuito RLC")
    print("3. Salir")
    opcion = int(input())
    return opcion

def menutwo():
    print("Seleccione una opcion: ")
    print("1. Circuito en serie")
    print("2. Circuito en paralelo")
    print("3. Retroceder")
    opcionCircuito = int(input())
    return opcionCircuito

def circuitoResistivoSerie():
    print("Circuito resistivo en serie")
    resistencias = resistencias()
    voltaje = voltaje()
    resistenciaTotal = 0
    for i in range(len(resistencias)):
        resistenciaTotal += resistencias[i]
    corriente = voltaje / resistenciaTotal
    return corriente, resistenciaTotal, resistencias


def circuitoResistivoParalelo():
    print("Circuito resistivo en paralelo")
    resistencias = resistencias()
    voltaje = voltaje()
    resistenciaTotal = 0
    for i in range(len(resistencias)):
        resistenciaTotal += 1/resistencias[i]
    resistenciaTotal = 1/resistenciaTotal
    corriente = voltaje / resistenciaTotal
    return corriente, resistenciaTotal, resistencias

def resultados(corriente, resistenciaTotal, resistencias):
    print("Los resultados son: ")
    print("La corriente total es: ", corriente)
    for i in range(len(resistencias)):
        print("La corriente en la resistencia ", i+1, " es: ", corriente)
        print("La caida de voltaje en la resistencia ", i+1, " es: ", corriente * resistencias[i])
    print("La resistencia total es: ", resistenciaTotal)
    print("La resistencia equivalente es: ", resistenciaTotal)

def main():
    while True:
        opcion = menu()
        if opcion == 1:
            while True:
                opcionCircuito = menutwo()
                if opcionCircuito == 1:
                    corriente, resistenciaTotal, resistencias = circuitoResistivoSerie()
                    resultados(corriente, resistenciaTotal, resistencias)
                elif opcionCircuito == 2:
                    corriente, resistenciaTotal, resistencias = circuitoResistivoParalelo()
                    resultados(corriente, resistenciaTotal, resistencias)
                elif opcionCircuito == 3:
                    break
        elif opcion == 2:
            # Aquí puedes añadir la lógica para los circuitos RLC
            print("Funcionalidad para circuitos RLC aún no implementada.")
        elif opcion == 3:
            print("Saliendo del programa.")
            break
main()