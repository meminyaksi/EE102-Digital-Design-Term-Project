import numpy as np
from PIL import Image

# TXT dosyasının yolu
txt_path = 'githubtest.txt'

# Görüntü boyutu
width, height = 400, 300
pixels_per_frame = width * height

# Dosyayı oku
with open(txt_path, 'r') as f:
    lines = f.read().splitlines()

# Toplam satır sayısını kontrol et
if len(lines) % pixels_per_frame != 0:
    raise ValueError("Satır sayısı 120000'in katı olmalı.")

# Kaç frame olduğunu hesapla
num_frames = len(lines) // pixels_per_frame

# Her frame için görüntü oluştur
for i in range(num_frames):
    start = i * pixels_per_frame
    end = (i + 1) * pixels_per_frame

    # Binary string'leri uint8 piksel değerlerine çevir
    pixel_values = [int(b, 2) for b in lines[start:end]]

    # 2D numpy array'e dönüştür (height x width)
    img_array = np.array(pixel_values, dtype=np.uint8).reshape((height, width))

    # PIL Image ile kaydet
    img = Image.fromarray(img_array, mode='L')
    img.save(f'frame_{i+1}.png')

    print(f'frame_{i+1}.png oluşturuldu.')
