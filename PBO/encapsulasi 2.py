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

jinan = Siswa(16354, "Jinannisa Shafa", "XI MIPA 5")

print(jinan.getnis())
jinan.setnis(16089)
print(jinan.getnis())