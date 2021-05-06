#INHERITANCE / PEWARISAN
#super class / parent class
class Manusia:
    #konstruktor
    def __init__(self, nama, jk, usia) :
        self.nama = nama
        self.jk = jk
        self.usia = usia

    def info(self) :
        print("Nama : {}\nJenis Kelamin : {}\nUsia : {}".format(self.nama, self.jk, self.usia))
        print("------------------------")
        
    def makan(self) :
        print("Sedang makan nasi")
        print("------------------------")

#sub class / child class
class Pelajar(Manusia):
    #konstruktor anak
    def __init__(self, nama, jk, usia, nis, nilai):
        Manusia.__init__(self, nama, jk, usia)
        self.nis = nis
        self.nilai = nilai

    def belajar(self):
        print("{} sedang belajar".format(self.nama))
        print("------------------------")

    #methode overriding
    def makan(self):
        print("{} sedang sarapan pagi dengan nasi".format(self.nama))
        print("------------------------")

#sub class / child class
class Pekerja(Manusia):
    #konstruktor anak
    def __init__(self, nama, jk, usia, nip, gaji):
        Manusia.__init__(self, nama, jk, usia)
        self.nip = nip
        self.gaji = gaji

    def bekerja(self):
        print("{} sedang bekerja".format(self.nama))
        print("------------------------")

#instansi objek
Hoshi = Pelajar("Kwon Hoshi", "laki-laki", 18, 15066, 100)
Jeonghan = Pekerja("Yoon Jeonghan", "laki-laki", 24, 1995104, 4000000)

#pemanggilan
Hoshi.info()
Hoshi.belajar()
Hoshi.makan() #memanggil methode anak
Jeonghan.info()
Jeonghan.bekerja()
Jeonghan.makan() #memanggil methode induk