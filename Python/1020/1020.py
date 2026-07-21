totalDays = int(input())
years     = totalDays//365
months    = (totalDays%365)//30
days      = (totalDays%365)%30
print(f"{years} ano(s)\n{months} mes(es)\n{days} dia(s)")