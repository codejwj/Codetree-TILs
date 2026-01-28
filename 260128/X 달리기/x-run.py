X = int(input())

dist = 0
v = 0
t = 0

while True:
    if dist == X:
        break
    
    if (X - (dist + v + 1)) >= (v * (v + 1) // 2):
        dist += (v + 1)
        v += 1
        t += 1   
    elif (X - (dist + v)) >= (v * (v - 1) // 2):
        dist += v
        t += 1
    else:
        dist += (v - 1)
        v -= 1
        t += 1

print(t)