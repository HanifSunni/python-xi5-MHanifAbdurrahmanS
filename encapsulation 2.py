class Siswa:
    
    def __init__(self, nis, nama, kelas):
        self.__nis = nis
        self.__nama = nama
        self.__kelas = kelas

    #getter
    def getnis(self):
        return self.__nis

    #setter
    def setnis(self, newnis):
        self.__nis = newnis

udin = Siswa(17133, "Udin Cakale", "XI MIA 5")

print(udin.getnis())
udin.setnis(66666)
print(udin.getnis())