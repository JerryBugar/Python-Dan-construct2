nama = {"yahya", "gibran", "novalen"}
kelas = [ "XI RPL 1", "XI RPL 2", "XI RPL 3", "X PPLG 1", "X PPLG 2", "X PPLG 3"]

kelas.remove("XI RPL 2")  
kelas.remove("X PPLG 1")  
kelas.remove("XI RPL 3")  
kelas.remove("X PPLG 2")  

nama.update({"Marsya"})
nama.update({"Ersya"})


print(nama)
print(kelas)