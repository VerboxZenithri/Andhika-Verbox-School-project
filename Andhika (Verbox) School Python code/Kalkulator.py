import os
import math
import re
from decimal import Decimal, getcontext

#Set Precision Tinggi Untuk Perhitungan
getcontext().prec = 50

#ANSI Color Codes
R="\033[0m"
B="\033[34m"
G="\033[32m"
Y="\033[33m"
C="\033[36m"
M="\033[35m"
RD="\033[31m"
BG="\033[1;32m"
BB="\033[1;34m"
BY="\033[1;33m"

def clear():
    os.system("cls" if os.name=="nt" else "clear")

def header():
    print(f"{BG}╔════════════════════════════════════════════════════════════╗{R}")
    print(f"{BG}║{BY}            KALKULATOR ADVANCED - TERMINAL MODE             {BG}║{R}")
    print(f"{BG}╚════════════════════════════════════════════════════════════╝{R}")

def menu():
    clear()
    header()
    print(f"\n{C}[1]{R} Operasi Dasar        {C}[7]{R}  Konversi Suhu")
    print(f"{C}[2]{R} Pangkat & Akar       {C}[8]{R}  Konversi Panjang")
    print(f"{C}[3]{R} Trigonometri         {C}[9]{R}  Konversi Berat")
    print(f"{C}[4]{R} Logaritma            {C}[10]{R} Sistem Bilangan")
    print(f"{C}[5]{R} Faktorial & Kombinasi{C}[11]{R} Statistik")
    print(f"{C}[6]{R} Persamaan Kuadrat    {C}[12]{R} Matrix 2x2")
    print(f"{C}[0]{R} {RD}Keluar{R}\n")
    return input(f"{G}Pilih menu [{C}0-12{G}]:{R} ")

def operasi_dasar():
    clear()
    print(f"{BB}═══ OPERASI DASAR ═══{R}\n")
    print(f"{Y}1.{R} Tambah (+)   {Y}2.{R} Kurang (-)   {Y}3.{R} Kali (×)")
    print(f"{Y}4.{R} Bagi (÷)     {Y}5.{R} Modulus (%)  {Y}6.{R} Pangkat (^)")
    pilih=input(f"\n{G}Pilih:{R} ")
    if pilih in ['1','2','3','4','5','6']:
        try:
            a=float(input(f"{C}Angka 1:{R} "))
            b=float(input(f"{C}Angka 2:{R} "))
            if pilih=='1': hasil=a+b; op="+"
            elif pilih=='2': hasil=a-b; op="-"
            elif pilih=='3': hasil=a*b; op="×"
            elif pilih=='4':
                if b==0: print(f"\n{RD}[ERROR] Tidak bisa bagi dengan 0!{R}"); return
                hasil=a/b; op="÷"
            elif pilih=='5': hasil=a%b; op="%"
            elif pilih=='6': hasil=a**b; op="^"
            print(f"\n{BG}Hasil:{R} {a} {op} {b} = {BY}{hasil}{R}")
        except: print(f"\n{RD}[ERROR] Input tidak valid!{R}")
    else: print(f"\n{RD}[ERROR] Pilihan tidak valid!{R}")
    input(f"\n{Y}Tekan Enter untuk kembali...{R}")

def pangkat_akar():
    clear()
    print(f"{BB}═══ PANGKAT & AKAR ═══{R}\n")
    print(f"{Y}1.{R} Kuadrat (x²)      {Y}4.{R} Akar Pangkat N")
    print(f"{Y}2.{R} Kubik (x³)        {Y}5.{R} Pangkat N")
    print(f"{Y}3.{R} Akar Kuadrat (√)")
    pilih=input(f"\n{G}Pilih:{R} ")
    try:
        if pilih in ['1','2','3']:
            x=float(input(f"{C}Angka:{R} "))
            if pilih=='1': hasil=x**2; print(f"\n{BG}{x}² = {BY}{hasil}{R}")
            elif pilih=='2': hasil=x**3; print(f"\n{BG}{x}³ = {BY}{hasil}{R}")
            elif pilih=='3':
                if x<0: print(f"\n{RD}[ERROR] Tidak bisa akar bilangan negatif!{R}"); return
                hasil=math.sqrt(x); print(f"\n{BG}√{x} = {BY}{hasil}{R}")
        elif pilih=='4':
            x=float(input(f"{C}Angka:{R} "))
            n=int(input(f"{C}Akar pangkat:{R} "))
            if n==0: print(f"\n{RD}[ERROR] Pangkat tidak boleh 0!{R}"); return
            hasil=x**(1/n); print(f"\n{BG}ⁿ√{x} (n={n}) = {BY}{hasil}{R}")
        elif pilih=='5':
            x=float(input(f"{C}Base:{R} "))
            n=float(input(f"{C}Pangkat:{R} "))
            hasil=x**n; print(f"\n{BG}{x}^{n} = {BY}{hasil}{R}")
        else: print(f"\n{RD}[ERROR] Pilihan tidak valid!{R}")
    except: print(f"\n{RD}[ERROR] Input tidak valid!{R}")
    input(f"\n{Y}Tekan Enter untuk kembali...{R}")

def trigonometri():
    clear()
    print(f"{BB}═══ TRIGONOMETRI ═══{R}\n")
    print(f"{Y}1.{R} Sin    {Y}4.{R} Sec")
    print(f"{Y}2.{R} Cos    {Y}5.{R} Csc")
    print(f"{Y}3.{R} Tan    {Y}6.{R} Cot")
    pilih=input(f"\n{G}Pilih:{R} ")
    if pilih in ['1','2','3','4','5','6']:
        try:
            deg=float(input(f"{C}Sudut (derajat):{R} "))
            rad=math.radians(deg)
            if pilih=='1': hasil=math.sin(rad); func="sin"
            elif pilih=='2': hasil=math.cos(rad); func="cos"
            elif pilih=='3': hasil=math.tan(rad); func="tan"
            elif pilih=='4':
                cos_val=math.cos(rad)
                if abs(cos_val)<1e-10: print(f"\n{RD}[ERROR] Sec tidak terdefinisi (cos=0)!{R}"); return
                hasil=1/cos_val; func="sec"
            elif pilih=='5':
                sin_val=math.sin(rad)
                if abs(sin_val)<1e-10: print(f"\n{RD}[ERROR] Csc tidak terdefinisi (sin=0)!{R}"); return
                hasil=1/sin_val; func="csc"
            elif pilih=='6':
                tan_val=math.tan(rad)
                if abs(tan_val)<1e-10: print(f"\n{RD}[ERROR] Cot tidak terdefinisi (tan=0)!{R}"); return
                hasil=1/tan_val; func="cot"
            print(f"\n{BG}{func}({deg}°) = {BY}{hasil}{R}")
        except: print(f"\n{RD}[ERROR] Input tidak valid!{R}")
    else: print(f"\n{RD}[ERROR] Pilihan tidak valid!{R}")
    input(f"\n{Y}Tekan Enter untuk kembali...{R}")

def logaritma():
    clear()
    print(f"{BB}═══ LOGARITMA ═══{R}\n")
    print(f"{Y}1.{R} Log₁₀ (Log basis 10)")
    print(f"{Y}2.{R} Ln (Log natural)")
    print(f"{Y}3.{R} Log basis N")
    pilih=input(f"\n{G}Pilih:{R} ")
    try:
        x=float(input(f"{C}Angka:{R} "))
        if x<=0: print(f"\n{RD}[ERROR] Log hanya untuk bilangan positif!{R}"); return
        if pilih=='1': hasil=math.log10(x); print(f"\n{BG}log₁₀({x}) = {BY}{hasil}{R}")
        elif pilih=='2': hasil=math.log(x); print(f"\n{BG}ln({x}) = {BY}{hasil}{R}")
        elif pilih=='3':
            base=float(input(f"{C}Base:{R} "))
            if base<=0 or base==1: print(f"\n{RD}[ERROR] Base harus > 0 dan ≠ 1!{R}"); return
            hasil=math.log(x,base); print(f"\n{BG}log_{base}({x}) = {BY}{hasil}{R}")
        else: print(f"\n{RD}[ERROR] Pilihan tidak valid!{R}")
    except: print(f"\n{RD}[ERROR] Input tidak valid!{R}")
    input(f"\n{Y}Tekan Enter untuk kembali...{R}")

def faktorial_kombinasi():
    clear()
    print(f"{BB}═══ FAKTORIAL & KOMBINASI ═══{R}\n")
    print(f"{Y}1.{R} Faktorial (n!)")
    print(f"{Y}2.{R} Permutasi (nPr)")
    print(f"{Y}3.{R} Kombinasi (nCr)")
    pilih=input(f"\n{G}Pilih:{R} ")
    try:
        if pilih=='1':
            n=int(input(f"{C}n:{R} "))
            if n<0: print(f"\n{RD}[ERROR] n harus ≥ 0!{R}"); return
            hasil=math.factorial(n); print(f"\n{BG}{n}! = {BY}{hasil}{R}")
        elif pilih in ['2','3']:
            n=int(input(f"{C}n:{R} "))
            r=int(input(f"{C}r:{R} "))
            if n<0 or r<0: print(f"\n{RD}[ERROR] n dan r harus ≥ 0!{R}"); return
            if r>n: print(f"\n{RD}[ERROR] r tidak boleh > n!{R}"); return
            if pilih=='2': hasil=math.perm(n,r); print(f"\n{BG}P({n},{r}) = {BY}{hasil}{R}")
            else: hasil=math.comb(n,r); print(f"\n{BG}C({n},{r}) = {BY}{hasil}{R}")
        else: print(f"\n{RD}[ERROR] Pilihan tidak valid!{R}")
    except: print(f"\n{RD}[ERROR] Input tidak valid!{R}")
    input(f"\n{Y}Tekan Enter untuk kembali...{R}")

def persamaan_kuadrat():
    clear()
    print(f"{BB}═══ PERSAMAAN KUADRAT ═══{R}")
    print(f"{C}Format: ax² + bx + c = 0{R}\n")
    try:
        a=float(input(f"{C}Koefisien a:{R} "))
        b=float(input(f"{C}Koefisien b:{R} "))
        c=float(input(f"{C}Koefisien c:{R} "))
        if a==0: print(f"\n{RD}[ERROR] Bukan persamaan kuadrat (a=0)!{R}"); return
        D=b**2-4*a*c
        print(f"\n{BG}Diskriminan (D) = {BY}{D}{R}")
        if D>0:
            x1=(-b+math.sqrt(D))/(2*a)
            x2=(-b-math.sqrt(D))/(2*a)
            print(f"{G}Dua akar real berbeda:{R}")
            print(f"  x₁ = {BY}{x1}{R}")
            print(f"  x₂ = {BY}{x2}{R}")
        elif D==0:
            x=-b/(2*a)
            print(f"{G}Dua akar real sama:{R}")
            print(f"  x₁ = x₂ = {BY}{x}{R}")
        else:
            real=-b/(2*a)
            imag=math.sqrt(abs(D))/(2*a)
            print(f"{G}Dua akar kompleks:{R}")
            print(f"  x₁ = {BY}{real} + {imag}i{R}")
            print(f"  x₂ = {BY}{real} - {imag}i{R}")
    except: print(f"\n{RD}[ERROR] Input tidak valid!{R}")
    input(f"\n{Y}Tekan Enter untuk kembali...{R}")

def konversi_suhu():
    clear()
    print(f"{BB}═══ KONVERSI SUHU ═══{R}\n")
    print(f"{Y}1.{R} Celsius → Fahrenheit  {Y}4.{R} Fahrenheit → Celsius")
    print(f"{Y}2.{R} Celsius → Kelvin      {Y}5.{R} Fahrenheit → Kelvin")
    print(f"{Y}3.{R} Celsius → Reamur      {Y}6.{R} Kelvin → Celsius")
    pilih=input(f"\n{G}Pilih:{R} ")
    try:
        if pilih=='1':
            c=float(input(f"{C}Celsius:{R} "))
            f=(c*9/5)+32; print(f"\n{BG}{c}°C = {BY}{f}°F{R}")
        elif pilih=='2':
            c=float(input(f"{C}Celsius:{R} "))
            k=c+273.15; print(f"\n{BG}{c}°C = {BY}{k}K{R}")
        elif pilih=='3':
            c=float(input(f"{C}Celsius:{R} "))
            re=c*4/5; print(f"\n{BG}{c}°C = {BY}{re}°R{R}")
        elif pilih=='4':
            f=float(input(f"{C}Fahrenheit:{R} "))
            c=(f-32)*5/9; print(f"\n{BG}{f}°F = {BY}{c}°C{R}")
        elif pilih=='5':
            f=float(input(f"{C}Fahrenheit:{R} "))
            k=(f-32)*5/9+273.15; print(f"\n{BG}{f}°F = {BY}{k}K{R}")
        elif pilih=='6':
            k=float(input(f"{C}Kelvin:{R} "))
            c=k-273.15; print(f"\n{BG}{k}K = {BY}{c}°C{R}")
        else: print(f"\n{RD}[ERROR] Pilihan tidak valid!{R}")
    except: print(f"\n{RD}[ERROR] Input tidak valid!{R}")
    input(f"\n{Y}Tekan Enter untuk kembali...{R}")

def konversi_panjang():
    clear()
    print(f"{BB}═══ KONVERSI PANJANG ═══{R}\n")
    print(f"{Y}1.{R} Meter → Kilometer   {Y}5.{R} Meter → Inch")
    print(f"{Y}2.{R} Meter → Centimeter  {Y}6.{R} Kilometer → Mil")
    print(f"{Y}3.{R} Meter → Milimeter   {Y}7.{R} Mil → Kilometer")
    print(f"{Y}4.{R} Meter → Feet")
    pilih=input(f"\n{G}Pilih:{R} ")
    try:
        if pilih=='1': m=float(input(f"{C}Meter:{R} ")); km=m/1000; print(f"\n{BG}{m}m = {BY}{km}km{R}")
        elif pilih=='2': m=float(input(f"{C}Meter:{R} ")); cm=m*100; print(f"\n{BG}{m}m = {BY}{cm}cm{R}")
        elif pilih=='3': m=float(input(f"{C}Meter:{R} ")); mm=m*1000; print(f"\n{BG}{m}m = {BY}{mm}mm{R}")
        elif pilih=='4': m=float(input(f"{C}Meter:{R} ")); ft=m*3.28084; print(f"\n{BG}{m}m = {BY}{ft}ft{R}")
        elif pilih=='5': m=float(input(f"{C}Meter:{R} ")); inch=m*39.3701; print(f"\n{BG}{m}m = {BY}{inch}inch{R}")
        elif pilih=='6': km=float(input(f"{C}Kilometer:{R} ")); mil=km*0.621371; print(f"\n{BG}{km}km = {BY}{mil}mil{R}")
        elif pilih=='7': mil=float(input(f"{C}Mil:{R} ")); km=mil*1.60934; print(f"\n{BG}{mil}mil = {BY}{km}km{R}")
        else: print(f"\n{RD}[ERROR] Pilihan tidak valid!{R}")
    except: print(f"\n{RD}[ERROR] Input tidak valid!{R}")
    input(f"\n{Y}Tekan Enter untuk kembali...{R}")

def konversi_berat():
    clear()
    print(f"{BB}═══ KONVERSI BERAT ═══{R}\n")
    print(f"{Y}1.{R} Kilogram → Gram     {Y}4.{R} Kilogram → Ons")
    print(f"{Y}2.{R} Kilogram → Pound    {Y}5.{R} Pound → Kilogram")
    print(f"{Y}3.{R} Kilogram → Ton")
    pilih=input(f"\n{G}Pilih:{R} ")
    try:
        if pilih=='1': kg=float(input(f"{C}Kilogram:{R} ")); g=kg*1000; print(f"\n{BG}{kg}kg = {BY}{g}g{R}")
        elif pilih=='2': kg=float(input(f"{C}Kilogram:{R} ")); lb=kg*2.20462; print(f"\n{BG}{kg}kg = {BY}{lb}lb{R}")
        elif pilih=='3': kg=float(input(f"{C}Kilogram:{R} ")); ton=kg/1000; print(f"\n{BG}{kg}kg = {BY}{ton}ton{R}")
        elif pilih=='4': kg=float(input(f"{C}Kilogram:{R} ")); ons=kg*10; print(f"\n{BG}{kg}kg = {BY}{ons}ons{R}")
        elif pilih=='5': lb=float(input(f"{C}Pound:{R} ")); kg=lb/2.20462; print(f"\n{BG}{lb}lb = {BY}{kg}kg{R}")
        else: print(f"\n{RD}[ERROR] Pilihan tidak valid!{R}")
    except: print(f"\n{RD}[ERROR] Input tidak valid!{R}")
    input(f"\n{Y}Tekan Enter untuk kembali...{R}")

def sistem_bilangan():
    clear()
    print(f"{BB}═══ SISTEM BILANGAN ═══{R}\n")
    print(f"{Y}1.{R} Desimal → Biner     {Y}4.{R} Biner → Desimal")
    print(f"{Y}2.{R} Desimal → Oktal     {Y}5.{R} Oktal → Desimal")
    print(f"{Y}3.{R} Desimal → Hexa      {Y}6.{R} Hexa → Desimal")
    pilih=input(f"\n{G}Pilih:{R} ")
    try:
        if pilih=='1':
            des=int(input(f"{C}Desimal:{R} "))
            bin_val=bin(des)[2:]; print(f"\n{BG}{des}₁₀ = {BY}{bin_val}₂{R}")
        elif pilih=='2':
            des=int(input(f"{C}Desimal:{R} "))
            oct_val=oct(des)[2:]; print(f"\n{BG}{des}₁₀ = {BY}{oct_val}₈{R}")
        elif pilih=='3':
            des=int(input(f"{C}Desimal:{R} "))
            hex_val=hex(des)[2:].upper(); print(f"\n{BG}{des}₁₀ = {BY}{hex_val}₁₆{R}")
        elif pilih=='4':
            bin_val=input(f"{C}Biner:{R} ")
            des=int(bin_val,2); print(f"\n{BG}{bin_val}₂ = {BY}{des}₁₀{R}")
        elif pilih=='5':
            oct_val=input(f"{C}Oktal:{R} ")
            des=int(oct_val,8); print(f"\n{BG}{oct_val}₈ = {BY}{des}₁₀{R}")
        elif pilih=='6':
            hex_val=input(f"{C}Hexa:{R} ")
            des=int(hex_val,16); print(f"\n{BG}{hex_val}₁₆ = {BY}{des}₁₀{R}")
        else: print(f"\n{RD}[ERROR] Pilihan tidak valid!{R}")
    except: print(f"\n{RD}[ERROR] Input tidak valid!{R}")
    input(f"\n{Y}Tekan Enter untuk kembali...{R}")

def statistik():
    clear()
    print(f"{BB}═══ STATISTIK ═══{R}\n")
    print(f"{C}Masukkan data (pisahkan dengan spasi):{R}")
    try:
        data=list(map(float,input(f"{G}Data:{R} ").split()))
        if len(data)==0: print(f"\n{RD}[ERROR] Data kosong!{R}"); return
        n=len(data)
        mean=sum(data)/n
        data_sorted=sorted(data)
        if n%2==0: median=(data_sorted[n//2-1]+data_sorted[n//2])/2
        else: median=data_sorted[n//2]
        variance=sum((x-mean)**2 for x in data)/n
        std_dev=math.sqrt(variance)
        print(f"\n{BG}Jumlah data:{R} {BY}{n}{R}")
        print(f"{BG}Mean (rata-rata):{R} {BY}{mean}{R}")
        print(f"{BG}Median:{R} {BY}{median}{R}")
        print(f"{BG}Variance:{R} {BY}{variance}{R}")
        print(f"{BG}Standar Deviasi:{R} {BY}{std_dev}{R}")
        print(f"{BG}Min:{R} {BY}{min(data)}{R}")
        print(f"{BG}Max:{R} {BY}{max(data)}{R}")
    except: print(f"\n{RD}[ERROR] Input tidak valid!{R}")
    input(f"\n{Y}Tekan Enter untuk kembali...{R}")

def matrix_2x2():
    clear()
    print(f"{BB}═══ OPERASI MATRIX 2x2 ═══{R}\n")
    print(f"{Y}1.{R} Penjumlahan Matrix")
    print(f"{Y}2.{R} Perkalian Matrix")
    print(f"{Y}3.{R} Determinan Matrix")
    pilih=input(f"\n{G}Pilih:{R} ")
    try:
        if pilih in ['1','2']:
            print(f"\n{C}Matrix A:{R}")
            a11=float(input("a11: ")); a12=float(input("a12: "))
            a21=float(input("a21: ")); a22=float(input("a22: "))
            print(f"\n{C}Matrix B:{R}")
            b11=float(input("b11: ")); b12=float(input("b12: "))
            b21=float(input("b21: ")); b22=float(input("b22: "))
            if pilih=='1':
                c11=a11+b11; c12=a12+b12
                c21=a21+b21; c22=a22+b22
                print(f"\n{BG}Hasil A + B:{R}")
                print(f"  [{BY}{c11}{R}  {BY}{c12}{R}]")
                print(f"  [{BY}{c21}{R}  {BY}{c22}{R}]")
            else:
                c11=a11*b11+a12*b21; c12=a11*b12+a12*b22
                c21=a21*b11+a22*b21; c22=a21*b12+a22*b22
                print(f"\n{BG}Hasil A × B:{R}")
                print(f"  [{BY}{c11}{R}  {BY}{c12}{R}]")
                print(f"  [{BY}{c21}{R}  {BY}{c22}{R}]")
        elif pilih=='3':
            print(f"\n{C}Matrix:{R}")
            a11=float(input("a11: ")); a12=float(input("a12: "))
            a21=float(input("a21: ")); a22=float(input("a22: "))
            det=a11*a22-a12*a21
            print(f"\n{BG}Determinan:{R} {BY}{det}{R}")
        else: print(f"\n{RD}[ERROR] Pilihan tidak valid!{R}")
    except: print(f"\n{RD}[ERROR] Input tidak valid!{R}")
    input(f"\n{Y}Tekan Enter untuk kembali...{R}")

def main():
    while True:
        pilih=menu()
        if pilih=='1': operasi_dasar()
        elif pilih=='2': pangkat_akar()
        elif pilih=='3': trigonometri()
        elif pilih=='4': logaritma()
        elif pilih=='5': faktorial_kombinasi()
        elif pilih=='6': persamaan_kuadrat()
        elif pilih=='7': konversi_suhu()
        elif pilih=='8': konversi_panjang()
        elif pilih=='9': konversi_berat()
        elif pilih=='10': sistem_bilangan()
        elif pilih=='11': statistik()
        elif pilih=='12': matrix_2x2()
        elif pilih=='0':
            clear()
            print(f"{BG}Terima kasih telah menggunakan kalkulator!{R}")
            break
        else: input(f"{RD}[ERROR] Pilihan tidak valid! Tekan Enter...{R}")

if __name__=="__main__":
    main()