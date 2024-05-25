def obtenerResistencias():
    print("Ingrese el numero de resistencias: ")
    nResist = int(input())
    print("Ingrese las resistencias: ")
    resistencias = []
    for i in range(nResist):
        resistencias.append(float(input()))
    return resistencias

def obtenerVoltaje():
    print("Ingrese el voltaje: ")
    voltaje =float(input())
    return voltaje

def obtenerFrecuencia():
    print("Ingrese la frecuencia: ")
    frecuencia = float(input())
    return frecuencia

def obtenerCapacitancia():
    print("Ingrese la capacitancia: ")
    capacitancia = float(input())
    return capacitancia

def obtenerInductancia():
    print("Ingrese la inductancia: ")
    inductancia = float(input())
    return inductancia