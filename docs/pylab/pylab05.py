#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# ZADANIE: wykonaj wykres funkcji f(x), gdzie x = <-10;10> z krokiem 0.5
# f(x) = x/-3 + a dla x <= 0
# f(x) = x*x/3 dla x >= 0

import pylab

x = pylab.arange(-10, 10.5, 0.5)  # lista argumentów x
a = int(input("Podaj współczynnik a: "))
y1 = [i / -3 + a for i in x if i <= 0]

y2 = [i**2 / 3 for i in x if i >= 0]

pylab.plot(x[:len(y1)], y1, x[-len(y2):], y2)
pylab.title('Wykres f(x)')
pylab.grid(True)
pylab.show()
