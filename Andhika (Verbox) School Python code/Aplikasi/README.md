# Aplikasi Absensi Sekolah

Aplikasi absensi berbasis web yang dibangun dengan Flask sesuai dengan flowchart yang diberikan.

## Fitur Utama

### Admin
- Login dengan autentikasi
- Kelola kelas (tambah, hapus)
- Kelola user (guru dan admin)
- Lihat laporan absensi semua kelas
- Dashboard dengan statistik

### Guru
- Login dengan autentikasi
- Isi absensi untuk kelas yang tersedia
- Lihat riwayat absensi yang telah diinput
- Dashboard dengan statistik absensi hari ini

## Instalasi

1. Install dependencies:
```bash
pip install -r requirements.txt --break-system-packages
```

2. Jalankan aplikasi:
```bash
python app.py
```

3. Buka browser dan akses:
```
http://localhost:5000
```

## Akun Default

### Admin
- Username: `admin`
- Password: `admin123`

### Guru
- Username: `guru1`
- Password: `guru123`

## Struktur Folder

```
aplikasi-absensi/
├── app.py                 # File utama aplikasi Flask
├── requirements.txt       # Dependencies Python
├── data/                  # Folder penyimpanan data JSON
│   ├── users.json        # Data user
│   ├── classes.json      # Data kelas
│   └── attendance.json   # Data absensi
└── templates/            # Template HTML
    ├── base.html
    ├── login.html
    ├── admin_dashboard.html
    ├── guru_dashboard.html
    ├── manage_class.html
    ├── manage_user.html
    ├── take_attendance.html
    ├── reports.html
    └── report_detail.html
```

## Cara Penggunaan

### Sebagai Admin

1. Login dengan akun admin
2. **Kelola Kelas**: Tambah kelas baru dengan daftar siswa
3. **Kelola User**: Tambah guru atau admin baru
4. **Laporan**: Lihat semua absensi yang telah diinput

### Sebagai Guru

1. Login dengan akun guru
2. Pilih kelas yang akan diabsen
3. Isi status kehadiran untuk setiap siswa:
   - ✅ Hadir
   - 🤒 Sakit
   - 📝 Izin
   - ❌ Alpa
4. Simpan absensi
5. Lihat riwayat absensi di menu Laporan

## Fitur Tambahan

- **Aksi Cepat**: Saat mengisi absensi, tersedia tombol untuk mengisi semua siswa dengan status yang sama
- **Print Laporan**: Laporan dapat di-print langsung dari browser
- **Statistik Real-time**: Dashboard menampilkan statistik terkini
- **Validasi Form**: Semua form memiliki validasi untuk mencegah kesalahan input
- **Responsive Design**: Tampilan menyesuaikan dengan ukuran layar

## Keamanan

- Password di-hash menggunakan SHA-256
- Session-based authentication
- Role-based access control (Admin & Guru)
- Admin utama tidak dapat dihapus

## Teknologi yang Digunakan

- **Backend**: Python Flask
- **Frontend**: HTML, CSS, JavaScript
- **Database**: JSON files (untuk kemudahan deployment)
- **Authentication**: Flask Session

## Catatan

- Data disimpan dalam format JSON di folder `data/`
- Aplikasi ini cocok untuk penggunaan skala kecil-menengah
- Untuk production, disarankan menggunakan database SQL dan HTTPS
