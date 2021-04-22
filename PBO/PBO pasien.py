class pasien:
    #class variabel
    jumlah_pasien = 0
    
    #konstruktor
    def __init__(self, nama, umur, berat, tinggi):
        self.nama = nama
        self.umur = umur
        self.berat = berat
        self.tinggi = tinggi
        pasien.jumlah_pasien += 1

    #methode/fungsi
    def bmi(self):
        print("Nama pasien : ", self.nama)
        bmi = self.berat/(self.tinggi**2)
        print("BMI : ", bmi)
        if bmi < 18.5:
            print("Kekurangan berat badan")
        elif bmi > 18.5 and bmi <= 24.9:
            print("Berat badan ideal")
        elif bmi > 24.9 and bmi <= 29.9:
            print("Berat badan berlebih")
        else:
            print("Obesitas")

    def beratIdeal(self):
        ideal = (self.tinggi*100 - 100) - (10/100 * (self.tinggi*100 - 100))
        print("BB ideal : ", ideal)
        print("----------------------")
    
#instasiasi objek/pembuatan objek
pasien1 = pasien("Jennie", 25, 45, 1.63)
pasien2 = pasien("Jisoo", 26, 44, 1.62)
pasien3 = pasien("Lisa", 24, 44.7, 1.66)
pasien4 = pasien("Rose", 24, 44, 1.68)
#pemanggilan pasien 1
pasien1.bmi()
pasien1.beratIdeal()
#pemanggilan pasien 2
pasien2.bmi()
pasien2.beratIdeal()
#pemanggilan pasien 3
pasien3.bmi()
pasien3.beratIdeal()
#pemanggilan pasien 4
pasien4.bmi()
pasien4.beratIdeal()

print("Jumlah pasien : ", pasien.jumlah_pasien)