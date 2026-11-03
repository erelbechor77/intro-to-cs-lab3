
num=0
sum=1
while num<1:
    num=int(input("Enter a positive number: "))
for i in range(1, num + 1):
    sum=sum*i

print(f"The factorial of {num} is {sum}")
