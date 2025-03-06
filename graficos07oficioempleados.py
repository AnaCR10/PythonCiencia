import oracledb 
import matplotlib.pyplot as plt

print("Gráficos con BBDD")
#creamos la conexión a la bbdd, con el cursor
connection = oracledb.connect(user="SYSTEM", password='oracle', dsn='localhost/xe')
cursor = connection.cursor()
sql ="select OFICIO, avg(SALARIO) as MEDIA from EMP group by OFICIO"
cursor.execute(sql)
oficios = []
medias =[]
#recogemos los datos de la BBDD
for row in cursor:
    oficios.append(row[0])
    medias.append(row[1])
cursor.close()

#creamos el gráfico mediante plt y con un método iremos indicando 
#el tipo de gráfico que queremos
#TARTA
plt.pie(medias,labels=oficios)
#podemos personalizar el gráfico
plt.title("Media Salarial por Oficio")
plt.legend()
#podemos almacenar el gráfico en una imagen si queremos
plt.savefig("images/oficioempleados.png")
plt.show()
