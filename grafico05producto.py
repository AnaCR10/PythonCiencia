import matplotlib.pyplot as plt

print("-- VENTAS POR PRODUCTO --")
print("------------------------")

print("Introduce el nombre del comercial")
comercial = input()
list_productos = []
list_ventas =[]

i = 1
for i in range(5):
    print(f"Introduce el producto {i}")
    prod = input()
    print(f"Introduce las ventas del producto {i}")
    vent = input()
    i = i + 1
    list_productos.append(prod)
    list_ventas.append(vent)

plt.pie(list_ventas, labels=list_productos)
plt.title(f"Ventas de {comercial} ")
plt.legend()
#podemos almacenar el gráfico en una imagen si queremos
plt.savefig("images/circular.png")
plt.show()




