
num=int(input("Enter a number: "))
while num<0:#בדיקה שהמספר חיובי
    num=int(input("Enter a positive number: "))
if(num**0.5)%1==0:#בדיקה אם המספר ריבוע שלם
    print("yes")
else:
    print("no")