import matplotlib.pyplot as plt

a = int(input('Podaj współczynnik a: '))
b = int(input('Podaj współczynnik b: '))
x_min = int(input('Podaj wartość minimalną x: '))
x_max = int(input('Podaj wartość maksymalną x: '))

x = range(x_min, x_max+1)  # lista argumentów x
# wyrażenie listowe wylicza zbiór wartości y
y = [a * i + b for i in x]

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Wykres f(x) = a*x - b')
ax.grid(True)
plt.show()
