from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

entrada = "IPDI-2025-Grupo16/tp00/Lena128C.png"

img = Image.open(entrada).convert("RGB")

#modificar
arr = np.array(img)
invertida = 255 - arr
gris = arr.mean(axis=2, keepdims=True).astype(np.uint8)
gris3 = np.repeat(gris, 3, axis=2)

#guardar
Image.fromarray(invertida).save("invertida.png")
Image.fromarray(gris3).save("gris.png")

#graficar
plt.subplot(1, 3, 1); plt.imshow(img); plt.title("Original"); plt.axis("off")
plt.subplot(1, 3, 2); plt.imshow(invertida); plt.title("Invertida"); plt.axis("off")
plt.subplot(1, 3, 3); plt.imshow(gris3); plt.title("Grises"); plt.axis("off")
plt.show()


