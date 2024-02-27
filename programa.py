import pandas as pd

# Ruta del archivo CSV
ruta_archivo = "archive/dataset.csv"

try:
    datos = pd.read_csv(ruta_archivo)
except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{ruta_archivo}'")
except Exception:
    print("Ocurrio un error en la lectura del archivo")

#Alternativa 1
print(datos)


#Alternativa 2
titles = datos.columns
print([t for t in titles])
for index, row in datos.iterrows():
    row_to_show = [row[title] for title in titles]

    print(row_to_show)

#Alternativa 3
titulos = datos.columns
for titulo in titulos:
    print(f"{titulo:<15}", end="")
print()

for indice, fila in datos.iterrows():
    for titulo in titulos:
        print(f"{fila[titulo]:<15}", end="")
    print()

