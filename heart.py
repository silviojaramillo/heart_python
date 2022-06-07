from math import sqrt
from matplotlib import pyplot as plt
#Inicializando los arreglos que contendrán
#los valores de f(x) de la función
x, y, y1 = [], [], []

#Creando contadores para evaluar la función
counter1 = -2
counter2 = 2
#Evaluando la función en cada punto
i = 0
while i <= 999:
    x.append(counter1)
    if i != 999:
        y.append(sqrt(1-(abs(counter1)-1)**2))
        counter1 += 0.004
    else:
        y.append(0)
    
    y1.append(-2.5*sqrt(1-sqrt(abs(counter2)/2)))
    counter2 -= 0.004

    if (i == 999):
        counter1 += 0.004
        x.append(counter1)
        y.append(0)
        y1.append(0)
        

    i += 1
    # Colocando límites a los ejes
    plt.xlim(-2.5, 2.5)
    plt.ylim(-3.5,1.5)
      
    # Graficando la función
    plt.plot(x, y, color = 'c')
    plt.plot(x, y1, color = 'c')
    if i >= 250 and i <= 900:
        plt.title("Programming")
    if i >= 500 and i <= 930:
        plt.xlabel("I love programming...")
    if i >= 750 and i <= 960:
        plt.ylabel("Corazón hecho con Python...")
    plt.xticks([])
    plt.yticks([])
    plt.pause(0.01)
plt.show()



