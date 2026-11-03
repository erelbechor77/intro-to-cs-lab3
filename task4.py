
num=1
cnt=0

while num!="":#סדרת הקלטים
    num=(input("Enter a number: "))
    if num=="":#יציאה מהלולאה במידה והקלט ריק
        break
    num=int(num)
    if (num%2==1):
        print(":)")
        cnt=cnt+1


print(cnt)