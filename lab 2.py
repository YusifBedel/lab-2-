import numpy as np

A = np.array([[1, 1, 1, 1],
              [2, 3, 1, 2],
              [-1, 2, 4, 1],
              [2, -1, 1, -1]])

b = np.array([1, 1, 18, -12])

# Matris denklem sistemini çözüyoruz
x = np.linalg.solve(A, b)

print("Çözüm:")
print("x =", x[0])
print("y =", x[1])
print("z =", x[2])
print("w =", x[3])
