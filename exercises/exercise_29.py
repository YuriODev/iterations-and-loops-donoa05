# Your solution to Exercise 29
numbers = []
while True:
    num = int(input("numbers:"))
    numbers.append(num)
    if sum(numbers) == 0:
        break

sum_squares = sum(num ** 2 for num in numbers)
print(sum_squares)
