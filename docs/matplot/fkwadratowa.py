import matplotlib.pyplot as plt

a = 1
b = -3
c = 1
lx = list(range(-10, 11))  # lista argumentów x
ly = [a * x**2 + b * x + c for x in lx]

fig, ax = plt.subplots()
ax.plot(lx, ly, 'o:b', linewidth=2, alpha=0.5)
ax.set_xlabel('lx')
ax.set_ylabel('ly')
ax.set_title('Funkcja kwadratowa')
ax.grid(True)
plt.show()
plt.show()
