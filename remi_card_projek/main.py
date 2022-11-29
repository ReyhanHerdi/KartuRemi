import random
import model_dTree

kartu = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 
        4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 
        7, 7, 8, 8, 8, 8 ,9, 9, 9, 9, 10, 10, 10, 
        10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13]

kartuShuffle = random.choices(kartu, k=52) # acak deck

kartuP = []
kartuQ = []
kartuR = []
kartuS = []

print("Deck: %s" % kartuShuffle)

# Bagikan kartu ke pemain
x = -1
while x < 4:
    x += 1

    kartuP.append(kartuShuffle[x]) # ambil 5 kartu pertama dari deck
    kartuShuffle.remove(kartuP[x]) # singkirkan 5 kartu di deck utama yang udah diambil
    kartuQ.append(kartuShuffle[x])
    kartuShuffle.remove(kartuQ[x]) 
    kartuR.append(kartuShuffle[x])
    kartuShuffle.remove(kartuR[x])
    kartuS.append(kartuShuffle[x])
    kartuShuffle.remove(kartuS[x])

# Mulai permainan
m = 0
while m < 1:
    print("Deck: %s" % kartuShuffle)

    # Player 1
    print("Player 1")
    print("Kartu yang dimiliki: %s" % kartuP)
    decs = input("Tindakan: ")
    if(decs == "pull"):
        kartuP.append(kartuShuffle[0]) # ambil dari deck
        kartuShuffle.remove(kartuShuffle[0]) # kartu di deck berkurang
        
        # Pilih kartu yang mau dibuang
        buang = int(input("Kartu yang dibuang: "))
        kartuP.remove(buang)
        kartuShuffle.append(buang)

        print("Kartu yang dimiliki: %s" % kartuP)
        
    elif(decs == "place"):
        print("Permainan berakhir")
        m = 2
        continue
    
    # Player 2
    print("Player 2")
    print("Kartu yang dimiliki: %s" % kartuQ)
    decs = input("Tindakan: ")
    if(decs == "pull"):
        kartuQ.append(kartuShuffle[0])
        kartuShuffle.remove(kartuShuffle[0])

        
        # Pilih kartu yang mau dibuang
        buang = int(input("Kartu yang dibuang: "))
        kartuQ.remove(buang)
        kartuShuffle.append(buang)

        print("Kartu yang dimiliki: %s" % kartuQ)
        
    elif(decs == "place"):
        print("Permainan berakhir")
        m = 2
        continue
    
    # Player 3
    print("Player 3")
    print("Kartu yang dimiliki: %s" % kartuR)
    decs = input("Tindakan: ")
    if(decs == "pull"):
        kartuR.append(kartuShuffle[0])
        kartuShuffle.remove(kartuShuffle[0])
        
        # Pilih kartu yang mau dibuang
        buang = int(input("Kartu yang dibuang: "))
        kartuR.remove(buang)
        kartuShuffle.append(buang)

        print("Kartu yang dimiliki: %s" % kartuR)
        
    elif(decs == "place"):
        print("Permainan berakhir")
        m = 2
        continue
    
    # Player 4
    print("Player 4")
    print("Kartu yang dimiliki: %s" % kartuS)

    decsAuto = model_dTree.model(kartuS)
    print("Tindakan: %s" % decsAuto)
    if(decsAuto == "pull"):
        kartuS.append(kartuShuffle[0])
        kartuShuffle.remove(kartuShuffle[0])
        
        # Pilih kartu yang mau dibuang
        buang = min(kartuS)
        kartuS.remove(buang)
        kartuShuffle.append(buang)

        print("Kartu yang dimiliki: %s" % kartuS)
        
    elif(decsAuto == "place"):
        print("Permainan berakhir")
        m = 2

# Total Jumlah Kartu masing-masing pemain
totalP = 0
for p in kartuP:
    totalP += p
print("Player 1: %s" % totalP)

totalQ = 0
for q in kartuQ:
    totalQ += q
print("Player 2: %s" % totalQ)

totalR = 0
for r in kartuR:
    totalR += p
print("Player 3: %s" % totalR)

totalS = 0
for s in kartuS:
    totalS += s
print("Player 4: %s" % totalS)
    