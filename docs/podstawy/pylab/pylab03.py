#! /usr/bin/env python
# -*- coding: utf-8 -*-

# ZADANIE: wykonaj wykres funkcji f(x), gdzie x = <-10;10> z krokiem 0.5
# f(x) = x*x/3 dla x < 1 i x > 0
# f(x) = x/-3 + a dla x <= 0

import pylab

x = pylab.frange(-10, 11, 0.5) # lista argumentów x
y1 = [i**2/3 for i in x if i < 1 or i > 0]

pylab.plot(x,y1)
pylab.title('Wykres f(x)')
pylab.grid(True)
pylab.show()
