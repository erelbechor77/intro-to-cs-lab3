
num=0
while num%2==0:
    num=int(input("Enter an odd number: "))
for i in range(num+1,1):
    for j in range(1, 2*i):
        print("*", end="")
    for j in range(1, num-i+1):
        print(end=' ')


    print()