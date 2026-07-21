grades      = input().split()
n1,n2,n3,n4 = float(grades[0])*2,float(grades[1])*3,float(grades[2])*4,float(grades[3])
average     = (n1+n2+n3+n4)/10
print(f"Media: {(average):.1f}")
if(average >= 7):
    print("Aluno aprovado.")
elif(average < 5):
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exam = float(input())
    print(f"Nota do exame: {exam:.1f}")
    average = (average+exam)/2
    if(average >= 5):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {average:.1f}")