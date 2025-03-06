import matplotlib.pyplot as plt
#la mayoría de los gráficos suelen tener 2 ejes de coordenadas
#para representar los datos (x,y)
x =['Betis','Atletico de Madrid','Barcelona','Real Madrid']
#valor de mercado
y= [5,10,15,20]

#creamos el gráfico mediante plt y con un método iremos indicando 
#el tipo de gráfico que queremos
#BARRAS
plt.bar(x,y)
#podemos personalizar el gráfico
plt.title("Gráfico de Barras")
plt.xlabel("Equipos")
plt.ylabel("Valor de mercado")
plt.legend("Legenda")
#podemos almacenar el gráfico en una imagen si queremos
plt.savefig("images/barras.png")
plt.show()



