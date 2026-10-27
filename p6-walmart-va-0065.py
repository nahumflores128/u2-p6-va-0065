# nahum flores NC 0065

import matplotlib.pyplot as plt
import numpy as np

cant_productos = [100, 150, 200, 300, 500]
precio = [4000, 5000, 6000, 7000, 8000]

# Personalizar gráfica
plt.plot(cant_productos, precio, color="purple", marker="o",
         linestyle="--", linewidth=2, markersize=12)
plt.title("ventas de walamart 0065")
plt.xlabel("cant de productos")
plt.xlabel("precio")

plt.show()

print("nahum flores Nc 0065")
