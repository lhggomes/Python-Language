l = [ 30, 50, 10, 35, 70, 80,  100, 22]
sizeL = len(l)

#Bubble Short

for i in range(sizeL):
    for j in range (1,sizeL - i):
        if l[j] < l[j-1]:
            l[j], l[j-1] = l[j-1], l[j]

print(l)

