def resistencias():
    print("Ingrese el numero de resistencias: ")
    nResist = int(input())
    print("Ingrese las resistencias: ")
    resistencias = []
    for i in range(nResist):
        resistencias.append(float(input()))
    return resistencias, nResist

def voltaje():
    print("Ingrese el voltaje: ")
    voltaje =float(input())
    return voltaje

def frecuencia():
    print("Ingrese la frecuencia: ")
    frecuencia = float(input())
    return frecuencia

def capacitancia():
    print("Ingrese la capacitancia: ")
    capacitancia = float(input())
    return capacitancia

def inductancia():
    print("Ingrese la inductancia: ")
    inductancia = float(input())
    return inductancia