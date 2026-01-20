import numpy as np
import random
import matplotlib.pyplot as plt

n = int(input('Ile ruchów? '))
x = y = 0

for i in range(0, n):
    # wylosuj kąt i zamień go na radiany
    rad = random.randint(0, 360) * np.pi / 180
    x = x + np.cos(rad)  # wylicz współrzędną x
    y = y + np.sin(rad)  # wylicz współrzędną y
    print(f'x = {x:.2f}, y = {y:.2f}')
