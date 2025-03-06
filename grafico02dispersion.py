import matplotlib.pyplot as plt
#la mayoría de los gráficos suelen tener 2 ejes de coordenadas
#para representar los datos (x,y)
x =['Betis','Atletico de Madrid','Barcelona','Real Madrid']
#valor de mercado
y= [5,10,15,20]

#GRAFICO DE DISPERSION
plt.scatter(x,y)
plt.title("Gráfico de dispersión")
plt.xlabel("Equipos")
plt.ylabel("Valor de mercado")
plt.legend("Legenda de colores")
#podemos almacenar el gráfico en una imagen si queremos
plt.savefig("images/dispersion.png")
plt.show()
