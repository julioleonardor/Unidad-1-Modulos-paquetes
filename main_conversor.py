from conversor_temperatura import celsius, fahrenheit, kelvin
from conversor_longitud import metros, kilometros, pies, millas
from historiales import *


def convertir_temperatura():
    unidad = input("Ingrese la unidad de temperatura (1 = Celsius, 2 = Fahrenheit, 3 = Kelvin): ")
    valor = float(input("Ingrese el valor de temperatura a convertir: "))
    
    resultado = []
    if unidad == '1':
        resultado.append(f"{valor} °C = {celsius.celsius_a_fahrenheit(valor):.2f} °F")
        resultado.append(f"{valor} °C = {celsius.celsius_a_kelvin(valor):.2f} K")
    elif unidad == '2':
        resultado.append(f"{valor} °F = {fahrenheit.fahrenheit_a_celsius(valor):.2f} °C")
        resultado.append(f"{valor} °F = {fahrenheit.fahrenheit_a_kelvin(valor)} K")
    elif unidad == '3':
        resultado.append(f"{valor} K = {kelvin.kelvin_a_celsius(valor):.2f} °C")
        resultado.append(f"{valor} K = {kelvin.kelvin_a_fahrenheit(valor):.2f} °F")
    else:
        print("Unidad no válida.")
        return convertir_temperatura()
    
    for r in resultado:
        print(r)
        agregar_historial_temperatura(f"{valor} {unidad}", r)

def convertir_longitud():
    unidad = input("Ingrese la unidad de longitud (1 = Metros, 2 = Kilómetros, 3 = Pies, 4 = Millas): ")
    valor = float(input("Ingrese el valor de longitud a convertir: "))
    
    resultado = []
    if unidad == '1':
        resultado.append(f"{valor} m = {metros.metros_a_kilometros(valor):.2f} km")
        resultado.append(f"{valor} m = {metros.metros_a_pies(valor):.2f} pies")
        resultado.append(f"{valor} m = {metros.metros_a_millas(valor):.2f} millas")
    elif unidad == '2':
        resultado.append(f"{valor} km = {kilometros.kilometros_a_metros(valor):.2f} m")
        resultado.append(f"{valor} km = {kilometros.kilometros_a_pies(valor):.2f} pies")
        resultado.append(f"{valor} km = {kilometros.kilometros_a_millas(valor):.2f} millas")
    elif unidad == '3':
        resultado.append(f"{valor} pies = {pies.pies_a_metros(valor):.2f} m")
        resultado.append(f"{valor} pies = {pies.pies_a_kilometros(valor):.2f} km")
        resultado.append(f"{valor} pies = {pies.pies_a_millas(valor):.2f} millas")
    elif unidad == '4':
        resultado.append(f"{valor} millas = {millas.millas_a_metros(valor):.2f} m")
        resultado.append(f"{valor} millas = {millas.millas_a_kilometros(valor):.2f} km")
        resultado.append(f"{valor} millas = {millas.millas_a_pies(valor):.2f} pies")
    else:
        print("Unidad no válida.")
        return convertir_longitud()
    
    for r in resultado:
        print(r)
        agregar_historial_longitud(f"{valor} {unidad}", r)


def mostrar_historial():
    unidad = input("Mostrar el historial (1 = Historial Temperatura, 2 = Historial Longitud, 3 = Historial Completo)")

    if unidad == "1":
        print(ver_historial_temperatura())
    elif unidad == '2':
        print(ver_historial_longitud())
    elif unidad == '3':
        print(ver_historial_general())
    else:
        print("Unidad no válida")


def exportar_historial():
    unidad = input("Seleccione historial a exportar: (1 = Historial Temperatura, 2 = Historial Longitud, 3 = Historial Completo)")

    if unidad == '1':
        exportar_historial_temperatura()
        print("Historial de temperatura exportado")
    elif unidad == '2':
        exportar_historial_longitud()
        print("Historial de longitud exportado")
    elif unidad == '3':
        exportar_historial_general()
        print("Historial completo exportado")
    else:
        print("Opción Inválida")

def main():
    while True:
        opcion = input("Seleccione una opción(1 = Conversión Temperatura, 2 = Conversión Longitud, 3 = Ver Historial, 4 = Exportar Historial, 5 = Salir): ")
        
        if opcion == '1':
            convertir_temperatura()
        elif opcion == '2':
            convertir_longitud()
        elif opcion == '3':
            mostrar_historial()
        elif opcion == '4':
            exportar_historial()
        elif opcion == '5':
            print("Finalizado")
            break
        else:
            print("Opción no válida.")
            return main()

if __name__ == "__main__":
    main()
