# INHERITANCE / PEWARISAN
# super class / kelas induk
class Manusia:
    # kostruktor
    def __init__(self, nama, jk, usia):
        self.nama = nama
        self.jk = jk
        self.usia = usia

    def info(self):
        print("Nama : {}\nJenis Kelamin : {}\nUsia : {}".format(self.nama, self.jk, self.usia))
        print("---------------------------")

    def makan(self):
        print("sedang makan roti")
        print("---------------------------")

# sub class / kelas anak
class Pelajar(Manusia):
    #kostruktor anak
    def __init__(self, nama, jk, usia, nis, nilai):
        Manusia.__init__(self, nama, jk, usia)
        self.nis = nis
        self.nilai = nilai

    def belajar(self):
        print("{} sedang belajar".format (self.nama))
        print("---------------------------")

    # methode overriding
    def makan(self):
        print("{} sedang sarapan pagi dengan roti".format(self.nama))
        print("---------------------------")

# sub class /kelas anak
class Pekerja(Manusia):
    def __init__(self, nama, jk, usia, nip, gaji):
        Manusia.__init__(self, nama, jk, usia)
        self.nip = nip
        self.gaji = gaji

    def bekerja(self):
        print("{} sedang bekerja".format(self.nama))
        print("---------------------------")

# instansiasi objek
Jeje = Pelajar("Julianto", "Laki-laki", 17, "17263", 95)
Maemunah = Pekerja("Maemunah", "Perempuan", 23, "1234567", 7500000)

#pemanggilan
Jeje.info()
Jeje.belajar()
Jeje.makan()  # memanggil methode anak
Maemunah.info()
Maemunah.bekerja()
Maemunah.makan()  # memanggil methode induk