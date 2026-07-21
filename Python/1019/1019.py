totalSeconds = int(input())
hours        = totalSeconds//3600
minutes      = (totalSeconds//60)%60
seconds      = totalSeconds%60
print(f"{hours}:{minutes}:{seconds}")