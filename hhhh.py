dic = {"hola": "g"}
import matplotlib.pyplot as plt

x = 4 + 3j
a = [-5 + 7j, 6 + 8j, 6 + 8j, 2 + 4j, -1 + 2j, -8 + 7j, 7 + 5j, 1 + 9j]
X = [x.real for x in a]
Y = [x.imag for x in a]
plt.scatter(X, Y, color="red")
plt.show()
