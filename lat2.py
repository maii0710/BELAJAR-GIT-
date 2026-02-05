# ===============================
# Class Mahasiswa
# ===============================
class mahasiswa:
    def __init__(self, nama, nim):
        self.__nama = nama
        self.__nim = nim

    # Getter
    def get_nama(self):
        return self.__nama

    def get_nim(self):
        return self.__nim

    # Setter
    def set_nama(self, nama):
        self.__nama = nama

    def set_nim(self, nim):
        self.__nim = nim

    # Method untuk menampilkan data
    def info(self):
        print("Nama :", self.__nama)
        print("NIM  :", self.__nim)


# ===============================
# Program Utama (Main Program)
# ===============================

# Membuat objek mahasiswa
mhs1 = mahasiswa("Andi", "123456")
mhs2 = mahasiswa("Budi", "654321")

# Menampilkan data mahasiswa
print("Data Mahasiswa 1")
mhs1.info()

print("\nData Mahasiswa 2")
mhs2.info()

# Mengubah data menggunakan setter
mhs1.set_nama("Siti")
mhs1.set_nim("987654")

# Menampilkan data setelah diubah
print("\nData Mahasiswa 1 Setelah Diubah")
mhs1.info()
