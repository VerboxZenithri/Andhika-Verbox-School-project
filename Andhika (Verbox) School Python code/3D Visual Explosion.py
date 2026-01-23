import time
import sys

def nuke(n):  #Nah Ini Bomb Nya
    a = []
    for i in range(255):
        if n > 1:
            a.append(nuke(n-1))
        else:
            a.append(i)
    return a

#Effect Arming Nuclear+Loading Bar
spinner=["|","/","-","\\"]
bar_len=90
total_steps=105

print("⚠ ARMING NUCLEAR PAYLOAD... ⚠\n")

for i in range(total_steps+1):
    filled=int(i/total_steps*bar_len)
    bar="█"*filled+"-"*(bar_len-filled)
    spin=spinner[i%len(spinner)]

    sys.stdout.write(f"\r[{bar}]{i:3d}% {spin}")
    sys.stdout.flush()
    time.sleep(0.06)

print("\n\n☢︎ ⚠ LAUNCH SEQUENCE INITIATED ⚠ ☢︎")
time.sleep(1)

for t in range(15, 0, -1):
    sys.stdout.write(f"\r💣 T-{t}...")
    sys.stdout.flush()
    time.sleep(1)

print("\n\nYES RICKO, KABOOM!\n")
time.sleep(1)
print(nuke(64))

'''
#Loading Systemnya
total = 5  #total untuk si detik countdown

for t in range(total,0,-1):
    bar_len=80
    filled=int((total-t+1)/total*bar_len)
    bar="█"*filled+"-"*(bar_len-filled)

    sys.stdout.write(f"\r[{bar}]{t}detik lagi...")
    sys.stdout.flush()
    time.sleep(1)

print("\nAwas ada sule!!!")
time.sleep(1.4)
print("\nprikitiw...!")
time.sleep(0.3)
print(nuke(64))
''' #model awal