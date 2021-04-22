class siswa:
    #class variabel
    jumlah_siswa = 0

    #konstruktor
    def __init__(self, nama, kelas, kejurusan, sekolah, nilai):
        self.nama = nama
        self.kelas = kelas
        self.kejurusan = kejurusan
        self.sekolah = sekolah
        self.nilai = nilai
        siswa.jumlah_siswa += 1
    
    #methode
    def viewSiswa(self):
        print("=================")
        print("Data Siswa")
        print("Nama : ", self.nama)
        print("Kelas : ", self.kelas)
        print("Sekolah : ", self.sekolah)
        print("=================")

    def viewNilai(self):
        print("Data Nilai dan Jurusan")
        print("Nama : ", self.nama)
        print("Kejurusan : ", self.kejurusan)
        for nilai in self.nilai:
            print("Nilai : ", nilai)
        print("=================")
    
    def viewKeterangan(self):
        print("Keterangan")
        print("Nama : ", self.nama)
        print("Kelas : ", self.kelas)
        rata = sum(self.nilai)/len(self.nilai)
        print("Rata-rata : ", rata)
        if rata >= 75 :
            keterangan = "LULUS."
        else:
            keterangan = "TIDAK LULUS."
        print("Keterangan : ", keterangan)

#instansiasi objek
siswa1 = siswa("Lilian", "XI-3", "IPA", "SMA 1", [75, 80, 86, 78])
siswa2 = siswa("Anya", "XI-2", "IPA", "SMA 3", [88, 70, 80, 68])
siswa3 = siswa("Damian", "XI-5", "IPS", "SMA 2", [95, 80, 74, 78])

#pemanggilan objek siswa 1
siswa1.viewSiswa()
siswa1.viewNilai()
siswa1.viewKeterangan()
print("Jumlah siswa : ", siswa.jumlah_siswa)
print("=================")
#pemanggilan objek siswa 2
siswa2.viewSiswa()
siswa2.viewNilai()
siswa2.viewKeterangan()
print("Jumlah siswa : ", siswa.jumlah_siswa)
print("=================")
#pemanggilan objek siswa 3
siswa3.viewSiswa()
siswa3.viewNilai()
siswa3.viewKeterangan()
print("Jumlah siswa : ", siswa.jumlah_siswa)
print("=================")