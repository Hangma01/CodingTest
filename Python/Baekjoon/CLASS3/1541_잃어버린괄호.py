userInput = input().split("-")

data = []
for temp in userInput:
    c = map(int, temp.split("+"))
    data.append(sum(c))

result = data[0]
for i in data[1:]:
    result -= i
print(result)