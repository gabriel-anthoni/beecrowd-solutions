money  = int(round(float(input())*100))
bills  = [10000, 5000, 2000, 1000, 500, 200]
coints = [100, 50, 25, 10, 5, 1]
print("NOTAS:")
for bill in bills:
    print(f"{int(money//bill)} nota(s) de R$ {(bill/100):.2f}")
    money %= bill
print("MOEDAS:")
for coint in coints:
    print(f"{int(money//coint)} moeda(s) de R$ {(coint/100):.2f}")
    money %= coint