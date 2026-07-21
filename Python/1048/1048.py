salary = float(input())
percentage = 0
if(salary   <= 400.00):
    percentage = 0.15
elif(salary <= 800.00):
    percentage = 0.12
elif(salary <= 1200.00):
    percentage = 0.10
elif(salary <= 2000.00):
    percentage = 0.07
else:
    percentage = 0.04
print(f"Novo salario: {(salary+(salary*percentage)):.2f}\nReajuste ganho: {(salary*percentage):.2f}\nEm percentual: {int(percentage*100)} %")