#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import random
import matplotlib.pyplot as plt

n = int(input("Ile ruchów? "))
x = y = 0
lx = [0]
ly = [0]

for i in range(0, n):
    # wylosuj kąt i zamień go na radiany
    rad = float(random.randint(0, 360)) * np.pi / 180
    x = x + np.cos(rad)  # wylicz współrzędną x
    y = y + np.sin(rad)  # wylicz współrzędną y
    # print(x, y)
    lx.append(x)
    ly.append(y)

print(lx, ly)

# oblicz wektor końcowego przesunięcia
s = np.fabs(np.sqrt(x**2 + y**2))
print("Wektor przesunięcia:", s)

plt.plot(lx, ly, "o:", color="green", linewidth=2, alpha=0.5)
plt.legend(["Dane x, y\nPrzemieszczenie: " + str(s)], loc="upper left")
plt.xlabel("lx")
plt.ylabel("ly")
plt.title("Ruchy Browna")
plt.grid(True)
plt.show()
