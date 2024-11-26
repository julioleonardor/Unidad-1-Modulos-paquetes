from .historial_longitud import historial_longitud
from .historial_temperatura import historial_temperatura

def ver_historial_general():
    return {"temperatura": historial_temperatura, "longitud": historial_longitud}

def exportar_historial_general(nombre_archivo="historial_general.csv"):
    with open(nombre_archivo, "w") as archivo:
        archivo.write("Tipo,Entrada,Resultado\n")
        for item in historial_temperatura:
            archivo.write(f"Temperatura,{item['entrada']},{item['resultado']}\n")
        for item in historial_longitud:
            archivo.write(f"Longitud,{item['entrada']},{item['resultado']}\n")
