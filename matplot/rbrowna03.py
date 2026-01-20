import numpy as np
import random
import matplotlib.pyplot as plt

n = int(input('Ile ruchów? '))
x = y = 0
lx = [0]
ly = [0]

for i in range(0, n):
    # wylosuj kąt i zamień go na radiany
    rad = random.randint(0, 360) * np.pi / 180
    x = x + np.cos(rad)  # wylicz współrzędną x
    y = y + np.sin(rad)  # wylicz współrzędną y
    print(f'x = {x:.2f}, y = {y:.2f}')
    lx.append(x)
    ly.append(y)

# oblicz i wypisz wektor końcowego przesunięcia
s = np.fabs(np.sqrt(x ** 2 + y ** 2))
print(f'Wektor przesunięcia: {s:.2f}')

fig, ax = plt.subplots()
ax.plot((0, lx[-1]), (0, ly[-1]), color='blue')
ax.plot(lx, ly, 'o:g', linewidth=2, alpha=0.5)
ax.legend([f'Dane x, y\nPrzemieszczenie: {s:.2f}'], loc='upper left')
ax.set_xlabel('lx')
ax.set_ylabel('ly')
ax.set_title('Ruchy Browna')
ax.grid(True)
plt.show()
plt.show()
