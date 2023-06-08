#NUMBERS DIVISIBLE BY 7 NOT BY 5

numGen = (
            num
            for num in range(2, 101)
            if num % 7 == 0
            if num % 5 != 0
            )

sumNumGen = 0
for num in numGen:
    print(num)
    sumNumGen += num
print(sumNumGen)

numList = [
            num
            for num in range(2, 101)
            if num % 7 == 0
            if num % 5 != 0
            ]

print(numList)
print(sum(numList))
