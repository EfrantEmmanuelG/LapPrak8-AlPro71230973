def tampilakan(namafile):
    with open(namafile, 'r') as f:
        soal_jawaban = f.readlines()
        
    for line in soal_jawaban:
        soal, jawaban = line.strip().split('| |')
        print(soal)
        jawaban_user = input("Jawab: ")
        if jawaban_user.strip().lower() == jawaban.strip().lower():
            print("Jawaban Benar!")
        else:
            print("Jawaban Salah!")
            
nama_file = "soal82.txt"
tampilakan(nama_file)