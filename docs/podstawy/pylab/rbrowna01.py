#! /usr/bin/env python
# -*- coding: utf-8 -*-

import math
import random

n = int(raw_input("Ile ruchów? "))
x = y = 0

for i in range(0, n):
    rad = float(random.randint(0, 360)) * math.pi / 180
    x = x + math.cos(rad)
    y = y + math.sin(rad)
    print x, y

s = math.sqrt(x**2 + y**2)
