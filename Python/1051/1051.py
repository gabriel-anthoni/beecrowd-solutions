income = float(input())
if(income <= 2000.00):
    tax = 0
elif(income <= 3000.00):
    income -= 2000
    tax = income*0.08
elif(income <= 4500.00):
    income -= 3000
    tax = income*0.18 + ( 80 )
elif(income > 4500.00):
    income -= 4500
    tax = income*0.28 + ( 80 + 270 )

text = f"R$ {tax:.2f}" if tax != 0 else "Isento"
print(text)