

h = 0
for i in range(10):
    h += 2
    print(i, "i", h, "h")
    if h >= 2 and h <= 18:
        continue
print("el valor de h", h)
