class siswa:
    def __init__(self , nama , kelas , nilai):
        self.nama = nama
        self. kelas = kelas
        self. nilai = nilai

    def tampilkan_data(self):
        print("nama:", self.nama)
        print("kelas:", self.kelas)
        print("nilai:", self.nilai)

    def status_kelulusan(self):
         if self.nilai >= 75:
             print("status : Lulus")
         else:
             print("status :Tidak lulus")          
    
            
siswa1 = siswa("Maii imop", "x pplg", 95)
siswa1.tampilkan_data()
siswa1.status_kelulusan()

siswa2 = siswa("Nesya kupluk", "ix tjkt", 70)
siswa2.tampilkan_data()
siswa2.status_kelulusan()


