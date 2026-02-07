numbers = list(map(int, input("Enter the numbers:").split()))
max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
print("The maximum number is: ", max_num)
