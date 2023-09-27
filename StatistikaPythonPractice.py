import math
import statistics

# Disini function dijabarkan terlebih dahulu

def OlahData_FisikaIa():
  
  Qty_Nilai = int(input("Banyaknya Mahasiswa: "))
  Nilai_Mahasiswa = []

# for loop untuk menginput nilai mahasiswa sesuai dengan
# banyaknya mahasiswa yang ditetapkan

  for i in range(Qty_Nilai) :
    nilai_input = int(input(f"Masukkan nilai mahasiswa ke-{i + 1}: "))
    
    if nilai_input > 100:
      print("Nilai input tidak boleh melebihi 100")
      break

    Nilai_Mahasiswa.append(nilai_input)
  
  # Menghitung total nilai 

  Total_Nilai = sum(Nilai_Mahasiswa)

  # Menghitung rata-rata
  
  rata_rata = Total_Nilai / Qty_Nilai

  # Menghitung variansi

  variansi = statistics.pvariance(Nilai_Mahasiswa, rata_rata)

  # Menghitung standar deviasi (akar kuadrat dari variansi)

  standar_deviasi = math.sqrt(variansi)

  # Output Analisis

  print("--------------------------------------------------")
  print("STATISTIK NILAI")
  print(f"Rata-rata: {rata_rata}")
  print(f"Variansi: {variansi}")
  print(f"Standard Deviasi: {standar_deviasi}")

  # Output Kelulusan tiap siswa
  print("---------------------")
  for i in range(len(Nilai_Mahasiswa)):
    if Nilai_Mahasiswa[i] > 70 and Nilai_Mahasiswa[i] > rata_rata:
        print(f"Nilai Mahasiswa ke-{i+1} sudah layak lulus: {bool(1)}")
    else :
      print(f"Nilai Mahasiswa ke-{i+1} sudah layak lulus: {bool(0)}")
  
OlahData_FisikaIa()