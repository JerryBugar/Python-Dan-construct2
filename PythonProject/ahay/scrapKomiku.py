from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import requests

# Inisialisasi WebDriver
driver = webdriver.Chrome()

# URL dari halaman komik
url = 'https://shinigami03.com/series/academys-genius-swordmaster/chapter-64/'

# Membuka halaman
driver.get(url)

# Tunggu beberapa detik agar halaman sepenuhnya dimuat
time.sleep(5)

# Scroll down untuk memuat semua gambar (scroll 3 kali sebagai contoh)
for i in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)  # Memberikan waktu untuk gambar dimuat

# Membuat folder untuk menyimpan gambar
os.makedirs('komik', exist_ok=True)

# Mengambil elemen gambar (menggunakan XPath yang lebih umum)
images = driver.find_elements(By.XPATH, "//img")

# Debug: Print jumlah gambar yang ditemukan
print(f'Jumlah gambar yang ditemukan: {len(images)}')

# Loop untuk menyimpan gambar
for i, img in enumerate(images):
    img_url = img.get_attribute('data-src') or img.get_attribute('src')  # Memeriksa kedua atribut
    if img_url:
        print(f'Mengambil gambar dari URL: {img_url}')
        try:
            img_data = requests.get(img_url).content
            img_name = f'komik/{i+1}.jpg'
            
            # Menyimpan gambar
            with open(img_name, 'wb') as handler:
                handler.write(img_data)
            
            print(f'Gambar {i+1} berhasil disimpan sebagai {img_name}')
        except Exception as e:
            print(f'Gagal mengunduh gambar dari {img_url}: {e}')
    else:
        print(f'URL gambar tidak ditemukan untuk elemen {i+1}')

# Tutup browser
driver.quit()

# Tambahan: Keterangan akhir
if len(images) > 0:
    print(f'Selesai! Total gambar yang ditemukan: {len(images)}')
else:
    print('Tidak ada gambar yang ditemukan.')