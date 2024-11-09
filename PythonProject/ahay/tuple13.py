buah = ("semangka", "jeruk", "apel")
x = ("Anggur",)  
buah += x
uhuy = list(buah)
uhuy.remove("semangka")
buah = tuple(uhuy)
print(buah)