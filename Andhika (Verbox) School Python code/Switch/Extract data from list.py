#Ganti Nilainya Di Sini:
command=["mv",67,29] 

match command:
    case ["stop"]:
        act="Berhenti di tempat."
    case ["mv",x,y]:
        act = f"Bergerak Ke Koordinat X:{x},Y:{y}"
    case ["rotate",dir]if dir in["left","right"]:
        act=f"Putar ke arah{dir}"
        
    case _:
        act="Perintah tidak dikenali"
print(act)