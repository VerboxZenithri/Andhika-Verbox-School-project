def belanja_tahu(ada_pisang):
    tahu=2
    if ada_pisang:
        tahu=tahu*4 
    return tahu
hasil_belanja=belanja_tahu(ada_pisang=False)
print(f"Jumlah yang dibeli: {hasil_belanja}")