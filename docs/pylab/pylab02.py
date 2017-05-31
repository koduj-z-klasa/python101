#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pylab

a = int(input('Podaj współczynnik a: '))
b = int(input('Podaj współczynnik b: '))
x = range(-10, 11)  # lista argumentów x

# wyrażenie listowe wylicza dziedzinę y
y = [a * i + b for i in x]  # lista wartości

pylab.plot(x, y)
pylab.title('Wykres f(x) = a*x - b')
pylab.grid(True)
pylab.show()
