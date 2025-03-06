import matplotlib.pyplot as plt
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'] #puede ser una lista o una tupla
temperatura = []
i=0

#realizamos un bucle para rellenar los datos
for i in dias_semana:
    print(f"Introduzca la temperatura para el {i}")
    temp = int(input())
    temperatura.append(temp)

plt.plot(dias_semana, temperatura, label="Semana 1")
#podemos incluir más gráficos dentro del gráfico lineal
#siempre que pongamos un label a cada plot()
#podemos poner más label
temperaturas2 =[5,20,8,12,19,22,30]
plt.plot(dias_semana,temperaturas2, label="Semana 2")
#podemos repetirlo tantas veces como queramos


plt.title("Evolución temperatura semanal")
plt.xlabel("Días")
plt.ylabel("Temperaturas")
plt.legend()
#podemos almacenar el gráfico en una imagen si queremos
plt.savefig("images/temperaturas.png")
plt.show()