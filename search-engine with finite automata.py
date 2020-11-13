from glob import glob
# ganti directory folder di dalam string di bawah ini!
# P.S : Untuk (+ "\*.txt") dibiarkan saja
Directory = r"D:\Semester 5\Teori Bahasa dan Otomata\DokumenBasaBali" + "\*.txt"

# input
input_user = input("Masukan keyword pencarian: ")
input_user = str(input_user)

# array user memisahkan setiap kata dari input
# misal input = Gatra Becik, maka array user = ['Gatra',' ','Becik']
array_user = input_user.split()

match = 0
jumlah_file = 0
# membuka dir penyimpanan file txt
for filepath in glob(Directory):
    jumlah_file += 1
    # proses match string
    # looping x isi dari array_user
    for x in array_user:
        f = open(str(filepath), mode='r+', encoding='utf-8', errors='ignore')
        
        # inisialisasi variable output
        terdeteksi = 0
        file = f
        
        # inisialisasi state
        if (x!= ' '):
            state = 0
            jumlah_state = len(x)

        # cek apakah inputan ada terdapat dalam artikel?
        j = 0
        for line in file:
            for i in line:
                if state == 0:
                    if i == x[j]:
                        state += 1
                        j+=1
                elif state != 0:
                    if state == jumlah_state:
                        terdeteksi+=1
                        break
                    elif i == x[j]:
                        state += 1
                        j+=1
                    else:
                        state = 0
                        j = 0   
            if terdeteksi!=0:
                break
            # end loop char in line
        if terdeteksi!=0:
            print('\n\033[1m.... ' + line[0:500])
            break
        # end loop line in file
    # end loop x in array_user

    if terdeteksi!=0:
        match += 1
        print('\033[0m' + '\nSource: ', str(filepath), "\n\n")
    # else:
    #     continue 
    f.close()
if match>0:
    print("\n","-"*30,match," dari ", jumlah_file ," artikel ditemukan!","-"*30)
elif match==0:
    print("\n Tidak ada artikel yang ditemukan...")
# end loop filepath

