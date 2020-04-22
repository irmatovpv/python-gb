n = int(input("Enter n: "))
max = 0
while(n):
    digit = n % 10
    if max < digit:
        max = digit
    n //= 10
print("Max digit is: {}".format(max))
