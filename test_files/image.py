from PIL import Image
import numpy as np

# Text dosyasını oku ve her satırı binary'den integer değere çevir
with open("pixel_output.txt", "r") as f:
    lines = f.readlines()
    pixel_values = [int(line.strip(), 2) for line in lines]  # Binary string → int

# 256 pikseli 16x16 matrise çevir
pixels_array = np.array(pixel_values, dtype=np.uint8).reshape((16, 16))

# Görüntüyü oluştur ve kaydet
img = Image.fromarray(pixels_array, mode='L')  # 'L' = 8-bit grayscale
img.save("reconstructed_image.png")
img.show()  # Ekranda da göster
