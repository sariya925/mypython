num = int(input("Enter an integer: "))
n = abs(num)
count = 0
while n > 0:
    n = n // 10 
    count += 1
if num == 0:
    count = 1
print("Number of digits:", count)
