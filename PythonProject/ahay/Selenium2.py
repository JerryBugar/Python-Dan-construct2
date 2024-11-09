from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Inisialisasi driver
driver = webdriver.Chrome()

# Buka Google
driver.get("https://www.google.com")

# Cari elemen input untuk pencarian
search_box = driver.find_element(By.NAME, "q")

# Masukkan teks "Selenium Python" ke dalam kotak pencarian
search_box.send_keys("Selenium Python")

# Tekan Enter untuk memulai pencarian
search_box.send_keys(Keys.RETURN)

# Perulangan untuk menunggu hasil pencarian muncul
while True:
    try:
        # Coba untuk menemukan elemen hasil pencarian
        results = driver.find_element(By.ID, "search")
        break  # Jika elemen ditemukan, keluar dari perulangan
    except:
        # Jika elemen belum ditemukan, tunggu 1 detik dan ulangi
        time.sleep(1)

# Cetak judul halaman hasil pencarian
print(driver.title)

# Tutup browser
driver.quit()
