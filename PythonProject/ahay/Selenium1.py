from selenium import webdriver

# Inisialisasi driver (misalnya, menggunakan Chrome)
driver = webdriver.Chrome()

# Buka halaman web
driver.get("https://www.google.com")

# Ambil judul halaman
print(driver.title)

# Tutup browser
driver.quit()
