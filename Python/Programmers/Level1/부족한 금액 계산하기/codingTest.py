def solution(price, money, count):
    
    result = sum(price*i for i in range(1,count+1))

    return result-money if result > money else 0

price=3
money=20
count=4
print(solution(price,money,count))