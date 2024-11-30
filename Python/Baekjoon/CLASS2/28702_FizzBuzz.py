for i in range(3,0,-1):
    x = input()

    if x not in ["FizzBuzz", "Fizz", "Buzz"]:
        n = int(x) + i

print("Fizz"*(n % 3 == 0) + "Buzz"*(n % 5 ==0) or n)