from conversor_temperatura import celsius, fahrenheit, kelvin
from conversor_longitud import metros, kilometros, pies, millas

def convertir_temperatura():
    unidad = input("Ingrese la unidad de temperatura (1 = Celsius, 2 = Fahrenheit, 3 = Kelvin): ")
    valor = float(input("Ingrese el valor de temperatura a convertir: "))
    
    if unidad == '1':
        print(f"{valor} °C = {celsius.celsius_a_fahrenheit(valor)} °F")
        print(f"{valor} °C = {celsius.celsius_a_kelvin(valor)} K")
    elif unidad == '2':
        print(f"{valor} °F = {fahrenheit.fahrenheit_a_celsius(valor)} °C")
        print(f"{valor} °F = {fahrenheit.fahrenheit_a_kelvin(valor)} K")
    elif unidad == '3':
        print(f"{valor} K = {kelvin.kelvin_a_celsius(valor)} °C")
        print(f"{valor} K = {kelvin.kelvin_a_fahrenheit(valor)} °F")
    else:
        print("Unidad no válida.")
        return convertir_temperatura()

def convertir_longitud():
    unidad = input("Ingrese la unidad de longitud (1 = Metros, 2 = Kilómetros, 3 = Pies, 4 = Millas): ")
    valor = float(input("Ingrese el valor de longitud a convertir: "))
    
    if unidad == '1':
        print(f"{valor} m = {metros.metros_a_kilometros(valor)} km")
        print(f"{valor} m = {metros.metros_a_pies(valor)} pies")
        print(f"{valor} m = {metros.metros_a_millas(valor)} millas")
    elif unidad == '2':
        print(f"{valor} km = {kilometros.kilometros_a_metros(valor)} m")
        print(f"{valor} km = {kilometros.kilometros_a_pies(valor)} pies")
        print(f"{valor} km = {kilometros.kilometros_a_millas(valor)} millas")
    elif unidad == '3':
        print(f"{valor} pies = {pies.pies_a_metros(valor)} m")
        print(f"{valor} pies = {pies.pies_a_kilometros(valor)} km")
        print(f"{valor} pies = {pies.pies_a_millas(valor)} millas")
    elif unidad == '4':
        print(f"{valor} millas = {millas.millas_a_metros(valor)} m")
        print(f"{valor} millas = {millas.millas_a_kilometros(valor)} km")
        print(f"{valor} millas = {millas.millas_a_pies(valor)} pies")
    else:
        print("Unidad no válida.")
        return convertir_longitud()

def main():
    opcion = input("Seleccione el tipo de conversión (1 = Temperatura, 2 = Longitud): ")
    
    if opcion == '1':
        convertir_temperatura()
    elif opcion == '2':
        convertir_longitud()
    else:
        print("Opción no válida.")
        return main()

if __name__ == "__main__":
    main()
