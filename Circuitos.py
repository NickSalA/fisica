from datos import obtenerCapacitancia, obtenerFrecuencia, obtenerInductancia, obtenerResistencias, obtenerVoltaje
import math

def menu():
    print("Bienvenido al programa de circuitos eléctricos!")
    print("Seleccione una opcion: ")
    print("1. Circuito de corriente continua")
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

def resistenciaContinuo(serie):
    voltaje=obtenerVoltaje()
    resistencias = obtenerResistencias()
    resistenciaTotal = 0
    if serie:
        for i in range(len(resistencias)):
            resistenciaTotal += resistencias[i]
    else:
        for i in range(len(resistencias)):
            resistenciaTotal += 1/resistencias[i]
        resistenciaTotal = 1 / resistenciaTotal
    corriente=voltaje/resistenciaTotal        
    return voltaje, resistencias, resistenciaTotal, corriente

def resultadosContinuo(voltaje,resistencias, resistenciaTotal, corriente, serie):
    print(f'Los resultados son:')
    if serie:
        print(f'La corriente en todas las resistencias en serie siempre es la misma: {corriente:.5f} A')
        for i in range(len(resistencias)):
            print(f'La caida de voltaje en la resistencia {i+1} es: {resistencias[i]*corriente:.5f} V')
    else:
        print(f'El voltaje en todas las resistencias en paralelo siempre es el mismo: {voltaje:.5f} V')
        for i in range(len(resistencias)):
            print(f'La corriente en la resistencia {i+1} es: {voltaje/resistencias[i]:.5f} V')
    print(f'La resistencia total es: {resistenciaTotal:.5f} Ohmios')
    print(f'La corriente total es: {corriente:.5f} A\n\n')

def resistenciaRLC(serieRLC):
    voltaje,_,resistenciaTotal,_ = resistenciaContinuo(serie=True)
    frecuencia = obtenerFrecuencia()
    inductancia = obtenerInductancia()
    capacitancia = obtenerCapacitancia()
    XL=2*3.14159265*frecuencia*inductancia #90 grados
    XC=1/(2*3.14159265*frecuencia*capacitancia) #-90 grados
    if serieRLC:
        X=XL-XC
        Z, Zgrados=(resistenciaTotal**2+X**2)**0.5, math.atan(X/resistenciaTotal)
    else:
        X=1/XC-1/XL
        Z, Zgrados=1/((resistenciaTotal**-2+X**2)**0.5), math.acos(-X/resistenciaTotal)
    corriente, corrienteGrados=voltaje/Z, 0-Zgrados 
    return voltaje, resistenciaTotal, XL, XC,Z, Zgrados, corriente, corrienteGrados

def resultadosRLC(voltaje, resistenciaTotal, XL, XC,Z, Zgrados, corriente, corrienteGrados, serieRLC):
    print(f'Los resultados son:')
    print(f'La resistencia total es: {resistenciaTotal:.5f} Ohmios')
    print(f'La reactancia inductiva es: {XL:.5f} Ohmios con un desfase de 90 grados')
    print(f'La reactancia capacitiva es: {XC:.5f} Ohmios con un desfase de -90 grados')
    print(f'La impedancia total es: {Z:.5f} Ohmios con un desfase de {Zgrados:.5f} grados\n\n')
    if serieRLC:
        print(f'La corriente total en todas las resistencias en serie siempre es la misma: {corriente:.5f} A con un desfase de {corrienteGrados:.5f} grados')
        print(f'La caida de voltaje en la resistencia es: {resistenciaTotal*corriente:.5f} V')
        print(f'La caida de voltaje en la reactancia inductiva es: {XL*corriente:.5f} V')
        print(f'La caida de voltaje en la reactancia capacitiva es: {XC*corriente:.5f} V')
    else:
        print(f'El voltaje en todas las resistencias en paralelo siempre es el mismo: {voltaje:.5f} V con un desfase de 0 grados')
        print(f'La corriente en la resistencia es: {voltaje/resistenciaTotal:.5f} A con un desfase de 0 grados')
        print(f'La corriente en la reactancia inductiva es: {voltaje/XL:.5f} A con un desfase de 90 grados')
        print(f'La corriente en la reactancia capacitiva es: {voltaje/XC:.5f} A con un desfase de -90 grados')
    print(f'La corriente total es: {corriente:.5f} A con un desfase de {corrienteGrados:.5f} grados')
    print(f'El voltaje total es: {voltaje:.5f} V con un desfase de 0 grados')
def main():
    while True:
        opcion = menu()
        if opcion == 1:
            while True:
                opcionCircuito = menutwo()
                if opcionCircuito == 1:
                    print(f'Circuito de corriente continua en serie\n')
                    voltaje, resistencias, resistenciaTotal, corriente = resistenciaContinuo(serie=True)
                    resultadosContinuo(voltaje, resistencias, resistenciaTotal, corriente, serie=True)

                elif opcionCircuito == 2:
                    print(f'Circuito de corriente continua en paralelo\n')
                    voltaje, resistencias, resistenciaTotal, corriente = resistenciaContinuo(serie=False)
                    resultadosContinuo(voltaje, resistencias,resistenciaTotal, corriente, serie=False)
                    
                elif opcionCircuito == 3:
                    break
        elif opcion == 2:
            while True:
                opcionCircuito = menutwo()
                if opcionCircuito == 1:
                    print(f'Circuito RLC en serie\n')
                    voltaje, resistenciaTotal, XL, XC,Z, Zgrados, corriente, corrienteGrados = resistenciaRLC(serieRLC=True)
                    resultadosRLC(voltaje, resistenciaTotal, XL, XC, Z, Zgrados, corriente, corrienteGrados, serieRLC=True)

                elif opcionCircuito == 2:
                    print(f'Circuito RLC en paralelo\n')
                    voltaje, resistenciaTotal, XL, XC,Z, Zgrados, corriente, corrienteGrados = resistenciaRLC(serieRLC=False)
                    resultadosRLC(voltaje, resistenciaTotal, XL, XC, Z, Zgrados, corriente, corrienteGrados, serieRLC=False)

                elif opcionCircuito == 3:
                    break
        elif opcion == 3:
            print("Saliendo del programa.")
            break
main()