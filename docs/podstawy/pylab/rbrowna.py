#! /usr/bin/env python
# -*- coding: utf-8 -*-

import math
import random
import pylab as p

n = int(raw_input("Ile ruchów? "))
x = y = 0
wsp_x = [0]
wsp_y = [0]
nazwapliku = "rbrowna.xls"
with open(nazwapliku, "w") as plik:
    print >>plik, "x\ty"
    print >>plik, str(x) + "\t" + str(y)
    for i in range(0, n):
        rad = float(random.randint(0, 360)) * math.pi / 180
        x = x + math.cos(rad)
        y = y + math.sin(rad)
        # print x, y
        print >>plik, str(x) + "\t" + str(y)
        wsp_x.append(x)
        wsp_y.append(y)

print wsp_x, wsp_y

# oblicz wektor końcowego przesunięcia
s = math.fabs(math.sqrt(x**2 + y**2))
print "Wektor przesunięcia:", s

p.plot(wsp_x, wsp_y, "o:", color="green", linewidth="3", alpha=0.5)
# r:., r:+, r., r+, o:, +:, color="green"
p.legend(["Dane x, y\nPrzemieszczenie: " + str(s)], loc="upper left")
p.xlabel("Wsp_x")
p.ylabel("Wsp_y")
p.title("Ruchy Browna")
p.grid(True)
p.show()
