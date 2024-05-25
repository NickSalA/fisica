from datos import obtenerCapacitancia, obtenerFrecuencia, obtenerInductancia, obtenerResistencias, obtenerVoltaje
import math

def menu():
    print("Bienvenido al programa de circuitos eléctricos!")
    print("Seleccione una opcion: ")
    print("1. Circuito resistivo")
    print("2. Circuito RLC")
    print("3. Salir")
    opcion = int(input())
    print("\n")
    return opcion

def menutwo():
    print("Seleccione una opcion: ")
    print("1. Circuito en serie")
    print("2. Circuito en paralelo")
    print("3. Retroceder")
    opcionCircuito = int(input())
    print("\n")
    return opcionCircuito

def resistenciaResist(serie):
    resistencias = obtenerResistencias()
    resistenciaTotal = 0
    if serie:
        for i in range(len(resistencias)):
            resistenciaTotal += resistencias[i]
    else:
        for i in range(len(resistencias)):
            resistenciaTotal += 1/resistencias[i]
    return resistenciaTotal, resistencias

def obtenerCorriente(voltaje,resistenciaTotal):
    return voltaje/resistenciaTotal

def resultadosResistivo(voltaje, resistenciaTotal, resistencias,corriente, serie):
    print(f'Los resultados son:')
    print(f'La corriente total es: {corriente:.5f} A')
    if serie:
        print(f'La corriente en todas las resistencias en serie siempre es la misma: {corriente:.5f} A')
        for i in range(len(resistencias)):
            print(f'La caida de voltaje en la resistencia {i+1} es: {resistencias[i]*corriente:.5f} V')
    else:
        print(f'El voltaje en todas las resistencias en paralelo siempre es el mismo: {voltaje:.5f} V')
        for i in range(len(resistencias)):
            print(f'La corriente en la resistencia {i+1} es: {voltaje/resistencias[i]:.5f} V')
    print(f'La resistencia total es: {resistenciaTotal:.5f} Ohmios\n\n')

def resistenciaRLC(serieRLC):
    print("Circuito RLC en serie\n")
    voltaje = obtenerVoltaje() # 0 grados
    resistenciaTotal = resistenciaResist(serie=True)
    frecuencia = obtenerFrecuencia()
    inductancia = obtenerInductancia()
    capacitancia = obtenerCapacitancia()
    XL=2*3.1416*frecuencia*inductancia #90 grados
    XC=1/(2*3.1416*frecuencia*capacitancia) #-90 grados
    if serieRLC:
        X=XL-XC
        Z, Zgrados=(resistenciaTotal**2+X**2)**0.5, math.atan(X/resistenciaTotal)
    else:
        X=1/XC-1/XL
        Z, Zgrados=1/((resistenciaTotal**-2+X**2)**0.5), math.acos(-X/resistenciaTotal)
    corriente, corrienteGrados=voltaje/Z, 0-Zgrados 
    return voltaje, resistenciaTotal, XL, XC,Z, Zgrados, corriente, corrienteGrados

def main():
    while True:
        opcion = menu()
        if opcion == 1:
            while True:
                opcionCircuito = menutwo()
                if opcionCircuito == 1:
                    print(f'Circuito resistivo en serie\n')
                    resistenciaTotal, resistencias = resistenciaResist(serie=True)
                    voltaje = obtenerVoltaje()
                    corriente = obtenerCorriente(voltaje, resistenciaTotal)
                    resultadosResistivo(voltaje, resistenciaTotal, resistencias, corriente, serie=True)
                elif opcionCircuito == 2:
                    print(f'Circuito resistivo en paralelo\n')
                    resistenciaTotal, resistencias = resistenciaResist(serie=False)
                    voltaje = obtenerVoltaje()
                    corriente = obtenerCorriente(voltaje, resistenciaTotal)
                    resultadosResistivo(voltaje, resistenciaTotal, resistencias, corriente, serie=False)
                elif opcionCircuito == 3:
                    break
        elif opcion == 2:
            while True:
                opcionCircuito = menutwo()
                if opcionCircuito == 1:
                    print(f'Circuito RLC en serie\n')
                    voltaje, resistenciaTotal, XL, XC,Z, Zgrados, corriente, corrienteGrados = resistenciaRLC(serieRLC=True)
                if opcionCircuito == 2:
                    print(f'Circuito RLC en paralelo\n')
                    voltaje, resistenciaTotal, XL, XC,Z, Zgrados, corriente, corrienteGrados = resistenciaRLC(serieRLC=False)
        elif opcion == 3:
            print("Saliendo del programa.")
            break
main()