#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pylab

a = 1
b = 2
x = range(-10, 11)  # lista argumentów x

y = []  # lista wartości
for i in x:
    y.append(a * i + b)

pylab.plot(x, y)
pylab.title('Wykres f(x) = a*x - b')
pylab.grid(True)
pylab.show()
