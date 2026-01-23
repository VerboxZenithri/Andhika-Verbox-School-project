import time
import sys
import winsound

def nuke(n):  #nah ini bomb nya
    a = []
    for i in range(255):
        if n > 1:
            a.append(nuke(n-1))
        else:
            a.append(i)
    return a

# efek arming nuclear
spinner = ["|", "/", "-", "\\"]
bar_len = 80
total_steps = 100

print("☢︎ ARMING NUCLEAR PAYLOAD... ⚠\n")

for i in range(total_steps + 1):
    filled = int(i / total_steps * bar_len)
    bar = "█" * filled + "-" * (bar_len - filled)
    spin = spinner[i % len(spinner)]

    sys.stdout.write(f"\r[{bar}] {i:3d}% {spin}")
    sys.stdout.flush()
    time.sleep(0.05)

print("\n\n☢︎ ⚠ LAUNCH SEQUENCE INITIATED ⚠ ☢︎")
time.sleep(1)

for t in range(5, 0, -1):
    sys.stdout.write(f"\r💣 T-{t}...")
    sys.stdout.flush()
    time.sleep(1)

print("\n\nYES RICKO, KABOOM!\n")
time.sleep(1)
print(nuke(1))