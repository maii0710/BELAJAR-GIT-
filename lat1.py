class siswa:
    def __init__(self , nama):
      self.nama = nama

    def  belajar(self):
     print(self.nama, "sedang belajar python")

siswa1 = siswa("mai")
siswa1.belajar()