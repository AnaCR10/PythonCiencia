import matplotlib.pyplot as plt
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
temperatura = []
i=0

for i in dias_semana:
    print(f"Introduzca la temperatura para el {i}")
    temp = int(input())
    temperatura.append(temp)

plt.plot(dias_semana,temperatura)
plt.title("Evolución temperatura semanal")
plt.xlabel("Días")
plt.ylabel("Temperaturas")
plt.legend()
#podemos almacenar el gráfico en una imagen si queremos
plt.savefig("images/temperaturas.png")
plt.show()