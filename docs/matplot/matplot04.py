import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10.5, 0.5)  # lista argumentów x
a = int(input("Podaj współczynnik a: "))
y1 = [i / -3 + a for i in x if i <= 0]
y2 = [i**2 / 3 for i in x if i >= 0]

fig, ax = plt.subplots()
ax.plot(x[:len(y1)], y1, x[-len(y2):], y2)
ax.set_title('Wykres f(x)')
ax.grid(True)
plt.show()
