import pandas as pd
print("Hola Mundo")
print("Primer ejemplo DataFrame")

#Vamos a crear un diccionario con elementos que se llamen series
#No deja de ser un diccionario con valores que van correspondientes entre
#ellos, aunque podrían no ser correspondientes.
datos = {
    'nombre': ['Lucía', 'Andrea', 'Alex','Antonia'],
    'edad': [22,17,48,70],
    'ciudad':['Segovia', 'Parla', 'Madrid','Toledo']
         }
#almacenamos los datos en un DATAFRAME
#y nos declaramos una variable dataframe
df = pd.DataFrame (datos)
print(df)

#podemos filtrar los datos de un dataframe
#la forma de filtrar es mediante la siguiente sintaxis:
#df[df[COLUMNA]== valor]
print(" ---- DataFrame Filtrado ----")
df_filtrado = df[df['edad']>30]
print(df_filtrado)

#también podemos ordenar por una o varias columnas:
#   df.sort_values(COLUMNA)
print(" ---- DataFrame ordenado ----")
df_sorted = df.sort_values('edad')
print(df_sorted)

