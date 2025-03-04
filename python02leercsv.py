import pandas as pd

print("--- Lectura de csv ---")
#almacenamos los datos de csv dentro de un DATAFRAME
df = pd.read_csv('data/datos.csv',delimiter=';')
print(df)
#así imprime un nº de filas delimitado, en este caso 5
print(df.head(5))

#podemos ordenar por edad
df_sorted = df.sort_values('edad')
print (df_sorted)

#podemos recuperar datos estadísticos, como la media de edad
media_edad = df['edad'].mean()
print(f"Media de edad: {media_edad}")

#podemos agrupar por columnas y recuperar datos
df_grupo = df.groupby('ocupacion').size()
print(df_grupo)