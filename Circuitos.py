from datos import obtenerCapacitancia, obtenerFrecuencia, obtenerInductancia, obtenerResistencias, obtenerVoltaje
import math
import matplotlib.pyplot as plt
import numpy as np

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

def suma_Resistencia(resistencias,serie):
    resistenciaTotal=0
    if serie:
        for i in range(len(resistencias)):
            resistenciaTotal += resistencias[i]
    else:
        for i in range(len(resistencias)):
            resistenciaTotal += 1/resistencias[i]
        resistenciaTotal = 1 / resistenciaTotal
    return resistenciaTotal

def resistenciaContinuo(serie):
    voltaje=obtenerVoltaje()
    resistencias = obtenerResistencias()
    resistenciaTotal = suma_Resistencia(resistencias,serie)
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
    voltaje, resistencias, resistenciaTotal, _ = resistenciaContinuo(serie=True)
    frecuencia = obtenerFrecuencia()
    inductancia = obtenerInductancia()
    capacitancia = obtenerCapacitancia()
    XL=2*math.pi*frecuencia*inductancia #90 grados
    XC=1/(2*math.pi*frecuencia*capacitancia) #-90 grados
    if serieRLC:
        X=XL-XC
        Z =(resistenciaTotal**2+X**2)**0.5
        Zgrados = math.atan(X/resistenciaTotal)*180/math.pi #Aca falla algo
    else:
        X=1/XC-1/XL
        Z =1/((resistenciaTotal**-2+X**2)**0.5) 
        Zgrados = -1*math.acos(X/(1/resistenciaTotal))*180/math.pi #Aca falla algo
    corriente= voltaje/Z 
    corrienteGrados = 0-Zgrados 
    return voltaje, resistencias, resistenciaTotal, XL, XC,Z, Zgrados, corriente, corrienteGrados

def resultadosRLC(voltaje, resistenciaTotal, XL, XC,Z, Zgrados, corriente, corrienteGrados, serieRLC):
    print(f'Los resultados son:')
    print(f'La resistencia total es: {resistenciaTotal:.5f} Ohmios')
    print(f'La reactancia inductiva es: {XL:.5f} Ohmios con un desfase de 90 grados')
    print(f'La reactancia capacitiva es: {XC:.5f} Ohmios con un desfase de -90 grados')
    print(f'La impedancia total es: {Z:.5f} Ohmios con un desfase de {Zgrados:.5f} grados')
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
    print(f'El voltaje total es: {voltaje:.5f} V con un desfase de 0 grados\n\n')

def graficarCircuito(voltaje, resistencias, serie, rlc=False, XL=None, XC=None):
    fig, ax = plt.subplots()

    ax.plot([0, 0], [0, 1], 'k-')  # Línea izquierda
    ax.plot([0, 1], [1, 1], 'k-')  # Línea superior
    ax.plot([1, 1], [1, 0], 'k-')  # Línea derecha
    ax.plot([1, 0], [0, 0], 'k-')  # Línea inferior

    componentes = resistencias
    if rlc:
        resistenciaTotal=suma_Resistencia(resistencias,serie)
        componentes =[resistenciaTotal, XL, XC]
        nombres = ['R','RL', 'RC']

    else:
        nombres = ['R' + str(i + 1) for i in range(len(resistencias))]
        
    if serie:
        num_componentes = len(componentes)
        tercio = num_componentes // 3
        resto = num_componentes % 3

        # Línea superior
        for i, (comp, nombre) in enumerate(zip(componentes[:tercio], nombres[:tercio])):
            ax.plot([i / (tercio + 1), (i + 1) / (tercio + 1)], [1, 1], 'k-')
            ax.text((i + 0.5) / (tercio + 1), 1.05, nombre + '\n' + f'{comp:.2f} Ω', ha='center')
            am=((i + 0.5) / (tercio + 1))
            x = np.array([am-0.08,am-0.06,am-0.04,am-0.02,am,am+0.02,am+0.04,am+0.06,am+0.08])
            y = np.array([1, 1.03,1,0.97,1, 1.03,1,0.97,1])
            ax.plot(x, y, 'k-')
        # Línea derecha
        for i, (comp, nombre) in enumerate(zip(componentes[tercio:2*tercio], nombres[tercio:2*tercio])):
            ax.plot([1, 1], [1 - (i + 1) / (tercio + 1), 1 - i / (tercio + 1)], 'k-')
            ax.text(1.05, 1 - (i + 0.5) / (tercio + 1), nombre + '\n' + f'{comp:.2f} Ω', va='center')
            am=(1 - (i+0.5) / (tercio + 1))
            x = np.array([1, 1.03,1,0.97,1, 1.03,1,0.97,1])
            y= np.array([am-0.08,am-0.06,am-0.04,am-0.02,am,am+0.02,am+0.04,am+0.06,am+0.08])
            ax.plot(x, y, 'k-') 
        # Línea inferior
        for i, (comp, nombre) in enumerate(zip(componentes[2*tercio:], nombres[2*tercio:])):
            ax.plot([1 - i / (tercio + resto), 1 - (i + 1) / (tercio + resto)], [0, 0], 'k-')
            ax.text(1 - (i + 0.5) / (tercio + resto), -0.05, nombre + '\n' + f'{comp:.2f} Ω', ha='center', va='top')
            am=((1 - (i+0.5) / (tercio + resto)))
            x= np.array([am-0.08,am-0.06,am-0.04,am-0.02,am,am+0.02,am+0.04,am+0.06,am+0.08])
            y = np.array([0,0.03,0,-0.03,0, 0.03,0,-0.03,0])
            ax.plot(x, y, 'k-')             
    else: #Paralelo
        num_componentes = len(componentes)
        for i, (comp, nombre) in enumerate(zip(componentes, nombres)):
            y_pos = 1 - i / (num_componentes - 1) if num_componentes > 1 else 0.5
            ax.plot([0, 1], [y_pos, y_pos], 'k-')
            ax.text(0.5, y_pos, nombre + '\n' + f'{comp:.2f} Ω', ha='center', va='center')
            y= np.array([y_pos,y_pos+0.03,y_pos,y_pos-0.03,y_pos,y_pos+0.03,y_pos,y_pos-0.03,y_pos])
            x = np.array([0.42,0.44,0.46,0.48,0.5, 0.52,0.54,0.56,0.58])
            ax.plot(x, y, 'k-')
    ax.text(-0.1, 0.5, f'{voltaje:.2f} V', va='center', ha='center', fontsize=12, bbox=dict(facecolor='white', edgecolor='black'))

    ax.set_xlim(-0.2, 1.2)
    ax.set_ylim(-0.2, 1.2)
    ax.axis('off')
    plt.title('Esquema del Circuito')
    plt.show()

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
                    graficarCircuito(voltaje,resistencias, serie=True)
                elif opcionCircuito == 2:
                    print(f'Circuito de corriente continua en paralelo\n')
                    voltaje, resistencias, resistenciaTotal, corriente = resistenciaContinuo(serie=False)
                    resultadosContinuo(voltaje, resistencias, resistenciaTotal, corriente, serie=False)
                    graficarCircuito(voltaje, resistencias, serie=False)
                elif opcionCircuito == 3:
                    break
        elif opcion == 2:
            while True:
                opcionCircuito = menutwo()
                if opcionCircuito == 1:
                    print(f'Circuito RLC en serie\n')
                    voltaje, resistencias, resistenciaTotal, XL, XC,Z, Zgrados, corriente, corrienteGrados = resistenciaRLC(serieRLC=True)
                    resultadosRLC(voltaje, resistenciaTotal, XL, XC, Z, Zgrados, corriente, corrienteGrados, serieRLC=True)
                    graficarCircuito(voltaje, resistencias, serie=True, rlc=True, XL=XL, XC=XC)
                elif opcionCircuito == 2:
                    print(f'Circuito RLC en paralelo\n')
                    voltaje, resistencias,resistenciaTotal, XL, XC, Z, Zgrados, corriente, corrienteGrados = resistenciaRLC(serieRLC=False)
                    resultadosRLC(voltaje, resistenciaTotal, XL, XC, Z, Zgrados, corriente, corrienteGrados, serieRLC=False)
                    graficarCircuito(voltaje, resistencias, serie=False, rlc=True, XL=XL, XC=XC)
                elif opcionCircuito == 3:
                    break
        elif opcion == 3:
            print("Saliendo del programa.")
            break
main()