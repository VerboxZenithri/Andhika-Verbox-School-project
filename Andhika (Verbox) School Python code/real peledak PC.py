def nuke(n):
    a = []
    for i in range(100):
        if n > 1:
            a.append(nuke(n-1))
        else:
            a.append(i)
    return a

print(nuke(15))