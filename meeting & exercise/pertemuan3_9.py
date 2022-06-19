# Metode format()
# menggunakan posisi default
default_order = "{}, {} dan {}". format("Budi", "Galih", "Ratna")
print('\n--- Urutan Default ---')
print(default_order)
# menggunakan argument posisi
positional_order = "{1}, {0} dan {2}". format("Budi", "Galih", "Ratna")
print('\n--- Urutan Berdasarkan Posisi ---')
print(positional_order)
