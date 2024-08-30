#Progammer     : Andi Ahmad Zaelani
#Nama aplikasi : Berpacu Dalam Lirik V1


import os, random   
song_data = os.listdir('./lagu')
song_data = [v.replace(".txt","") for v in song_data]

#Menampilkan logo
def start_game():
    print("="*50)
    print("""
███████╗████████╗███████╗██████╗ ███╗   ██╗███████╗███████╗██╗ █████╗ 
██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗  ██║██╔════╝██╔════╝██║██╔══██╗
███████╗   ██║   █████╗  ██████╔╝██╔██╗ ██║█████╗  ███████╗██║███████║
╚════██║   ██║   ██╔══╝  ██╔═══╝ ██║╚██╗██║██╔══╝  ╚════██║██║██╔══██║
███████║   ██║   ███████╗██║     ██║ ╚████║███████╗███████║██║██║  ██║
╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝  ╚═══╝╚══════╝╚══════╝╚═╝╚═╝  ╚═╝
""")
    print("="*50)
    print("""                                                
    ____                                  
   / __ )___  _________  ____ ________  __
  / __  / _ \/ ___/ __ \/ __ `/ ___/ / / /
 / /_/ /  __/ /  / /_/ / /_/ / /__/ /_/ / 
/_____/\___/_/  / .___/\__,_/\___/\__,_/  
               /_/                DALAM                                                                                               
                    ydys+:-`                 
                    sM+oyhmNNmy              
        .odh`       +MNdhso//sM-             
       +NdyMd       -M/`-/+syhMo   /o        
      oMo` NM.      `Mo      `dm   -Ny`      
      NN  +Mm        Nh       oM.   -Ny`     
      Mm.sNm-    .--.dN       -M+    -Ny`    
      hMmMy.   /dNNNmNM`  .:::-Nd     -Nh`   
    -yNMN/     NMMMMMMN. smNMMNMM`     :Nh`  
  .sNMmNN.     +dNNNds- `MMMMMMMN.      :Nh` 
 -mMNo:hMmdhy+- `.oh/`   /dmNmds.   `:oyymMh`
-NMm-omMMMmmNMNs` /MNdy/-``...`     oMMMMMMMs
yMM-.MMhhMo.-sMM+  sMMMMNmh+.       oMMMMMMN/
hMN  yd`:Md   NMs  `hM+:+ymMmo`      /hmmds- 
:MM+` -  mM- :MN:   .mm`  `/mMs        ``    
 +mMh+-..sMdyNm/     :Nh`   .dN              
  .+hmNNNNMMd+`       +Ms    /m              
     `-::-hMo          yM+   .:              
    /dmmy`:Mm      `-++oNM:                  
   `MMMMM:-Md     :mMMMMMMN.                 
    oNMMNhNm-     mMMMMMMMN.                 
     .+yys/`      yMMMMMMm-                  
                   :shhs:                    
   
 ██▓     ██▓ ██▀███   ██▓ ██ ▄█▀
▓██▒    ▓██▒▓██ ▒ ██▒▓██▒ ██▄█▒ 
▒██░    ▒██▒▓██ ░▄█ ▒▒██▒▓███▄░ 
▒██░    ░██░▒██▀▀█▄  ░██░▓██ █▄ 
░██████▒░██░░██▓ ▒██▒░██░▒██▒ █▄
░ ▒░▓  ░░▓  ░ ▒▓ ░▒▓░░▓  ▒ ▒▒ ▓▒
░ ░ ▒  ░ ▒ ░  ░▒ ░ ▒░ ▒ ░░ ░▒ ▒░
  ░ ░    ▒ ░  ░░   ░  ▒ ░░ ░░ ░ 
    ░  ░ ░     ░      ░  ░  ░   
  """)
    print("~"*50)
    print("""
Penjelasan Game Berapacu Dalam Lirik :
1. Masukan nama pemain
2. Terdapat 2 jenis tingkatan kesulitan,
a. Normal dengan 3 nyawa
b. Expert dengan 1 nyawa.
3. Terdapat 4 baris penggalan lirik lagu
4. Pemain harus menebak 1 baris lirik lagu
selanjutnya secara tepat.
5. Sistem poin diambil dari jumlah karakter
jawaban pemain yang benar.
6. Jawaban pemain dikatakan salah ketika tidak
sesuai dengan lirik lagu selanjutnya
dan nyawa akan berkurang satu.
7. Diakhir game, jumlah nilai peserta akan
terlihat sesuai yang diraih selama
game berlangsung.

Selamat bermain Stepnesian :v 
""")
    print("~"*50)
    nama = ""
    score = 0
    mode = ""
    nyawa = 0
    ronde = 0
    check_highscore_exist()
    nama = input("Nama Pemain : ")
    while nama == "null" or nama == "":
        nama = input("Harap gunakan nama yang valid.\nNama Pemain : ")
    while mode.lower() not in ["normal", "expert"]:
        mode = input("mode (normal/expert)  : ")
    if(mode.lower() == "normal"):
        nyawa = 3
    else:
        nyawa = 1
    print("Semangat dan Jangan Menyerah")
    print("~"*50)
    completed_song = []
    while nyawa != 0:
        ronde += 1 
        result = guess(score,mode,nyawa,ronde,completed_song)
        score += result[0]
        nyawa = result[2] 
        completed_song.append(str(result[4]))       
    os.system("cls" if os.name == "nt" else "clear")
    print("GAME OVER!")
    print("Sayang sekali {nama}, ada berhenti disini\nHasil akhir")
    print(f"Score   : {score}") 
    print("~"*50)
    check_highscore(nama,score,mode) 


#Memilih 5 line lirik secara acak
def get_lines(song):
    lagu_terpilih = open(f'./lagu/{song}.txt')
    lirik = lagu_terpilih.read().split("\n")
    line = random.randrange(0,len(lirik)-5)
    return lirik[line:line+5]

#Memasukan jawaban
#Bila jawabannya benar mendapat score sesuai jumlah kata
#Bila jawabannya salah tidak medapatkan score dan nyawa berkurang
def guess(score,mode,nyawa,ronde,completed):
    selected_song = random.choice(song_data)
    if(mode == "normal"):
        while (selected_song.lower() in ["secre","homework"]):
            selected_song = random.choice(song_data)
    while (selected_song in completed):
        selected_song = random.choice(song_data)
    lines = get_lines(selected_song)
    title = selected_song 
    if(selected_song.lower() == "secret"):
        title = "You Will Be Okay // Stola's Lullaby"
    elif(selected_song.lower() == "homework"):
        title = "nuzzle wuzzle"
    os.system("cls" if os.name == "nt" else "clear")
    print("Ronde ",ronde)
    print(f"Nyawa   : {nyawa}\nScore    : {score}")
    print(f"Judul lagu : {title}")
    print("~"*50)
    for line in lines:
        if(line == lines[-1]):
            break
        print(line,"\n")
    jawaban = input("Tebakan anda : ")
    if(jawaban.lower() == lines[-1].lower()):
        return [len(lines[-1].replace(" ","")),mode,nyawa,ronde,selected_song]
    else:
        nyawa -= 1
        print("Jawaban Salah")
        print("Jawaban : ",lines[-1])
        return [0,mode,nyawa,ronde,selected_song]

#Membuat highscore
def check_highscore_exist():
    highscore_txt = open('./highscore.txt','w')
    username = ""
    score = 0
    if(os.stat('./highscore.txt').st_size == 0):
        highscore_txt.write(f"[Normal] {username} {score}\n[expert] {username} {score}")
    highscore_txt.close()
    
#Menampilkan highscore di mode normal atau expert
def check_highscore(nama,score,mode):
    highscore = open('./highscore.txt').read().split('\n')
    normal = highscore[0].split(" ") 
    expert = highscore[1].split(" ")
    scored = False 
    if(mode.lower() == "normal"):
        if(score >= int(normal[2])): 
            normal[1] = nama 
            normal[2] = score 
            scored = True 
    else:
        if(score >= int(expert[2])): 
            expert[1] = nama 
            expert[2] = score
            scored = True 
    highscore = normal + ["\n"] + expert
    highscore = " ".join([str(elem) for elem in highscore])
    if scored == True:
        temp = open("./highscore.txt",'w')
        temp.write(highscore)
        temp.close()

        print("NEW HIGH SCORES!!!")
        print("Username     : ",nama)
        print("Score       : ",score)
        print("Berhasil meraih highscore di mode ",mode.upper())
    print("""
████████╗███████╗██████╗ ██╗███╗   ███╗ █████╗     
╚══██╔══╝██╔════╝██╔══██╗██║████╗ ████║██╔══██╗    
   ██║   █████╗  ██████╔╝██║██╔████╔██║███████║    
   ██║   ██╔══╝  ██╔══██╗██║██║╚██╔╝██║██╔══██║    
   ██║   ███████╗██║  ██║██║██║ ╚═╝ ██║██║  ██║    
   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚═╝  ╚═╝    
██╗  ██╗ █████╗ ███████╗██╗██╗  ██╗                
██║ ██╔╝██╔══██╗██╔════╝██║██║  ██║                
█████╔╝ ███████║███████╗██║███████║                
██╔═██╗ ██╔══██║╚════██║██║██╔══██║                
██║  ██╗██║  ██║███████║██║██║  ██║                
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═╝                
    """)

#Game siap dimainkan
start_game() 


  
