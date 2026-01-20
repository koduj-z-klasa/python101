import matplotlib.pyplot as plt

a = 1
b = 2

x = range(-10, 11)  # lista argumentów x
y = []  # lista wartości
for i in x:
    y.append(a * i + b)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Wykres f(x) = a*x - b')
ax.grid(True)
plt.show()
