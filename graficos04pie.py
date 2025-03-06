import matplotlib.pyplot as plt
#la mayoría de los gráficos suelen tener 2 ejes de coordenadas
#para representar los datos (x,y)
etiquetas =['Betis','Atletico de Madrid','Barcelona','Real Madrid']
#valor de mercado
valores= [5,10,15,20]

#creamos el gráfico mediante plt y con un método iremos indicando 
#el tipo de gráfico que queremos
#TARTA
plt.pie(valores, labels=etiquetas)
#podemos personalizar el gráfico
plt.title("Gráfico de TARTA")
plt.legend()
#podemos almacenar el gráfico en una imagen si queremos
plt.savefig("images/circular.png")
plt.show()