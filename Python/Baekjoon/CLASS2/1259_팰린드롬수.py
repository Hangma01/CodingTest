while True:
    num = input()
    if int(num[0]) == 0:
        break

    numLen = len(num)//2

    for i in range(numLen):
        if num[i] != num[-i-1]:
            print("no")
            break
    else:
        print("yes")    