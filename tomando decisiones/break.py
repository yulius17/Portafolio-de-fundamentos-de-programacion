contador = 0

for i in range(3):
    for j in range(3):
        contador += 1
        print("i", i, "J", j)
        if contador >= 10:
            break

print("contador: ", contador)
