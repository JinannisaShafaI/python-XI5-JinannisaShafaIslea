class karyawan:
    '''Dasar kelas untuk semua karyawan'''
    jumlah_karyawan = 0

    def __init__(self, nama, umur, alamat, grup_unit, gaji):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
        self.grup_unit = grup_unit
        self.gaji = gaji
        karyawan.jumlah_karyawan += 1

    def tampilkan_jumlah(self):
        print("Total karyawan : ", karyawan.jumlah_karyawan)
    
    def tampilkan_profil(self):
        print("Nama : ", self.nama)
        print("Umur : ", self.umur)
        print("Alamat : ", self.alamat)
        print("Unit grup : ", self.grup_unit)
        print("Gaji : ", self.gaji)
    
#Membuat objek pertama dari kelas karyawan
karyawan1 = karyawan("Scoups", 26, "Jakal", "Hip-hop", 2000000)
#Membuat objek kedua dan seterusnya dari kelas karyawan
karyawan2 = karyawan("Jeonghan", 26, "Jalan Godean", "Vocal", 2000000)
karyawan3 = karyawan("Joshua", 26, "Bantul", "Vocal", 2000000)
karyawan4 = karyawan("Jun", 25, "Pacitan", "Performance", 1900000)
karyawan5 = karyawan("Hoshi", 25, "Sleman", "Performance", 1900000)
karyawan6 = karyawan("Wonwoo", 25, "Gunung Kidul", "Hip-hop", 1900000)
karyawan7 = karyawan("Woozi", 25, "Jalan Godean", "Vocal", 1900000)
karyawan8 = karyawan("DK", 24, "Bantul", "Vocal", 1800000)
karyawan9 = karyawan("Mingyu", 24, "Jalan Magelang", "Hip-hop", 1800000)
karyawan10 = karyawan("Minghao", 24, "Pacitan", "Performance", 1800000)
karyawan11 = karyawan("Seungkwan", 23, "Jakal", "Vocal", 1700000)
karyawan12 = karyawan("Vernon", 23, "Bantul", "Hip-hop", 1700000)
karyawan13 = karyawan("Dino", 22, "Sleman", "Performance", 1600000)

karyawan1.tampilkan_profil()
karyawan2.tampilkan_profil()
karyawan3.tampilkan_profil()
karyawan4.tampilkan_profil()
karyawan5.tampilkan_profil()
karyawan6.tampilkan_profil()
karyawan7.tampilkan_profil()
karyawan8.tampilkan_profil()
karyawan9.tampilkan_profil()
karyawan10.tampilkan_profil()
karyawan11.tampilkan_profil()
karyawan12.tampilkan_profil()
karyawan13.tampilkan_profil()

print("Total karyawan : ", karyawan.jumlah_karyawan)