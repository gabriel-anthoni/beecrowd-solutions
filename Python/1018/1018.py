money = int(input())
bills = [100,50,20,10,5,2,1] 
print(money)
for bill in bills:
    print(f"{money//bill} nota(s) de R$ {bill},00")
    money %= bill