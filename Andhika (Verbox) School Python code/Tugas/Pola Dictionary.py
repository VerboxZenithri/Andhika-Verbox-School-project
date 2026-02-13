data={"role": "admin", "id": 1}

match data:
    case{"role": "admin", "id": id}:
        act=f"Akses penuh untuk admin ID:{id}"
    case{"role": "guest"}:
        act="Akses terbatas untuk tamu"
        
    case _:
        act="User tidak terdaftar"

print(act)