# Sistem Pembayaran SPP Menggunakan Class

class Siswa:
    def __init__(self, id_siswa, nama, kelas):
        self.id_siswa = id_siswa
        self.nama = nama
        self.kelas = kelas
        self.spp_terbayar = 0  # total SPP yang sudah dibayar

    def bayar_spp(self, jumlah):
        if jumlah <= 0:
            print("Jumlah pembayaran harus lebih dari 0!")
            return
        self.spp_terbayar += jumlah
        print(f"Pembayaran berhasil! Total SPP terbayar {self.nama}: Rp{self.spp_terbayar}")

    def tampilkan_info(self):
        print(f"{self.id_siswa}\t{self.nama}\t{self.kelas}\tRp{self.spp_terbayar}")


class SistemSPP:
    BIAYA_SPP = 500000  # biaya SPP per bulan

    def __init__(self):
        # Membuat daftar siswa
        self.daftar_siswa = {
            "001": Siswa("001", "Andi", "10A"),
            "002": Siswa("002", "Budi", "10B"),
            "003": Siswa("003", "Citra", "11A")
        }

    def tampilkan_siswa(self):
        print("\nDaftar Siswa:")
        print("ID\tNama\tKelas\tSPP Terbayar")
        for siswa in self.daftar_siswa.values():
            siswa.tampilkan_info()

    def proses_pembayaran(self):
        id_siswa = input("Masukkan ID Siswa: ")
        if id_siswa in self.daftar_siswa:
            try:
                jumlah = int(input("Masukkan jumlah pembayaran: Rp"))
                self.daftar_siswa[id_siswa].bayar_spp(jumlah)
            except ValueError:
                print("Input harus berupa angka!")
        else:
            print("ID Siswa tidak ditemukan!")

    def menu(self):
        while True:
            print("\n=== Sistem Pembayaran SPP ===")
            print("1. Lihat Daftar Siswa")
            print("2. Bayar SPP")
            print("3. Keluar")

            pilihan = input("Pilih menu: ")
            if pilihan == "1":
                self.tampilkan_siswa()
            elif pilihan == "2":
                self.proses_pembayaran()
            elif pilihan == "3":
                print("Terima kasih! Program selesai.")
                break
            else:
                print("Pilihan tidak valid!")


# Jalankan program
sistem = SistemSPP()
sistem.menu()
