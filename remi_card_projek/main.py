import random
import model_dTree

kartu = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 
        4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 
        7, 7, 8, 8, 8, 8 ,9, 9, 9, 9, 10, 10, 10, 
        10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13]

kartuShuffle = random.choices(kartu, k=52) # acak deck

# Bagikan kartu ke pemain
x = 0
while x < 4:
    x += 1

    # ambil 5 kartu pertama dari deck
    kartuP = random.choices(kartuShuffle, k=5)
    kartuQ = random.choices(kartuShuffle, k=5)
    kartuR = random.choices(kartuShuffle, k=5)
    kartuS = random.choices(kartuShuffle, k=5)

    # singkirkan 5 kartu di deck utama yang udah diambil
    kartuShuffle.remove(kartuP[x])
    kartuShuffle.remove(kartuQ[x]) 
    kartuShuffle.remove(kartuR[x])
    kartuShuffle.remove(kartuS[x])

# Mulai permainan
m = 0
while m < 1:
    print("Deck: %s" % kartuShuffle)

    # Player 1
    print("Player 1")
    print("Kartu yang dimiliki: %s" % kartuP)
    decs = input("Masukkan tindakan: ")
    if(decs == "pull"):
        kartuP.append(kartuShuffle[0]) # ambil dari deck
        kartuShuffle.remove(kartuShuffle[0]) # kartu di deck berkurang
        
        # Pilih kartu yang mau dibuang
        buang = int(input("Kartu yang dibuang: "))
        kartuP.remove(kartuP[buang])
        kartuShuffle.append(kartuP[buang])

        print("Kartu yang dimiliki: %s" % kartuP)
        
    elif(decs == "place"):
        print("Permainan berakhir")
        m = 2
        continue
    
    # Player 2
    print("Player 2")
    print("Kartu yang dimiliki: %s" % kartuQ)
    decs = input("Masukkan tindakan: ")
    if(decs == "pull"):
        kartuQ.append(kartuShuffle[0])
        kartuShuffle.remove(kartuShuffle[0])

        
        # Pilih kartu yang mau dibuang
        buang = int(input("Kartu yang dibuang: "))
        kartuQ.remove(kartuQ[buang])
        kartuShuffle.append(kartuQ[buang])

        print("Kartu yang dimiliki: %s" % kartuQ)
        
    elif(decs == "place"):
        print("Permainan berakhir")
        m = 2
        continue
    
    # Player 3
    print("Player 3")
    print("Kartu yang dimiliki: %s" % kartuR)
    decs = input("Masukkan tindakan: ")
    if(decs == "pull"):
        kartuR.append(kartuShuffle[0])
        kartuShuffle.remove(kartuShuffle[0])
        
        # Pilih kartu yang mau dibuang
        buang = int(input("Kartu yang dibuang: "))
        kartuR.remove(kartuR[buang])
        kartuShuffle.append(kartuR[buang])

        print("Kartu yang dimiliki: %s" % kartuR)
        
    elif(decs == "place"):
        print("Permainan berakhir")
        m = 2
        continue
    
    # Player 4
    print("Player 4")
    print("Kartu yang dimiliki: %s" % kartuS)
    
    model_dTree.model(kartuS)
    
    print("Masukkan tindakan: %s" % decs)

    if(decs == "pull"):
        kartuS.append(kartuShuffle[0])
        kartuShuffle.remove(kartuShuffle[0])
        
        # Pilih kartu yang mau dibuang
        buang = min(kartuS)
        kartuS.remove(buang)
        kartuShuffle.append(buang)

        print("Kartu yang dimiliki: %s" % kartuS)
        
    elif(decs == "place"):
        print("Permainan berakhir")
        m = 2

totalP = 0
for p in kartuP:
    totalP += p
print(totalP)

totalQ = 0
for q in kartuQ:
    totalQ += q
print(totalQ)

totalR = 0
for r in kartuR:
    totalR += p
print(totalR)

totalS = 0
for s in kartuS:
    totalS += s
print(totalS)
    