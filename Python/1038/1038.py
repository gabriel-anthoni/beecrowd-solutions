snacks = [4.00,4.50,5.00,2.00,1.50]
order  = input().split()
print(f"Total: R$ {((snacks[(int(order[0])-1)])*int(order[1])):.2f}")