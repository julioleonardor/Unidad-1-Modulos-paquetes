historial_temperatura = []

def agregar_historial_temperatura(entrada, resultado):
    historial_temperatura.append({"entrada": entrada, "resultado": resultado})

def ver_historial_temperatura():
    return historial_temperatura

def exportar_historial_temperatura(nombre_archivo="historial_temperatura.csv"):
    with open(nombre_archivo, "w") as archivo:
        archivo.write("Entrada,Resultado\n")
        for item in historial_temperatura:
            archivo.write(f"{item['entrada']},{item['resultado']}\n")
