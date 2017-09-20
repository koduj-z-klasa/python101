#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import random
import pylab as p

n = int(input("Ile ruchów? "))
x = y = 0
lx = [0]
ly = [0]
nazwapliku = "rbrowna.xls"
with open(nazwapliku, "w") as plik:
    plik.write("x\ty")
    plik.write(str(x) + "\t" + str(y))
    for i in range(0, n):
        rad = float(random.randint(0, 360)) * math.pi / 180
        x = x + math.cos(rad)
        y = y + math.sin(rad)
        # print(x, y)
        plik.write(str(x) + "\t" + str(y))
        lx.append(x)
        ly.append(y)

print(lx, ly)

# oblicz wektor końcowego przesunięcia
s = math.fabs(math.sqrt(x**2 + y**2))
print("Wektor przesunięcia:", s)

p.plot(lx, ly, "o:", color="green", linewidth=2, alpha=0.5)
# r:., r:+, r., r+, o:, +:, color="green"
p.legend(["Dane x, y\nPrzemieszczenie: " + str(s)], loc="upper left")
p.xlabel("Wsp_x")
p.ylabel("Wsp_y")
p.title("Ruchy Browna")
p.grid(True)
p.show()
