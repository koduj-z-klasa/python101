#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import random

n = int(input("Ile ruchów? "))
x = y = 0

for i in range(0, n):
    # wylosuj kąt i zamień go na radiany
    rad = float(random.randint(0, 360)) * np.pi / 180
    x = x + np.cos(rad)  # wylicz współrzędną x
    y = y + np.sin(rad)  # wylicz współrzędną y
    print(x, y)

# oblicz wektor końcowego przesunięcia
s = np.sqrt(x**2 + y**2)
print("Wektor przesunięcia:", s)
