historial_longitud = []

def agregar_historial_longitud(entrada, resultado):
    historial_longitud.append({"entrada": entrada, "resultado": resultado})

def ver_historial_longitud():
    return historial_longitud

def exportar_historial_longitud(nombre_archivo="historial_longitud.csv"):
    with open(nombre_archivo, "w") as archivo:
        archivo.write("Entrada,Resultado\n")
        for item in historial_longitud:
            archivo.write(f"{item['entrada']},{item['resultado']}\n")
