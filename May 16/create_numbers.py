f = open("numbers.txt", "w")
for i in range(1, 201):
    f.write(str(i) + "\n")
f.close()