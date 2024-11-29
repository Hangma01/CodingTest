N = int(input())
sizeCount = list(map(int, input().split()))
T, P = map(int, input().split())

# 주문할 티셔츠 묶음
tishirtBundle = 0
for count in sizeCount:
    if count % T == 0:  
        tishirtBundle += count // T
    else:
        tishirtBundle += count // T + 1
    
print(tishirtBundle)

# 주문할 펜 묶음, 자루
penBundle = N // P
penPiece = N % P
print(penBundle, penPiece)

