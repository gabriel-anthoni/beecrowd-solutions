characteristics = []
path            = [False,False,False]

for _ in range(3):
    text = input()
    characteristics.append(text)

path[0] = True if  characteristics[0] == "vertebrado"                                                 else False
path[1] = True if  characteristics[1] == "ave"                  or characteristics[1] == "inseto"     else False
path[2] = True if (characteristics[2] == "onivoro" and path[0]) or characteristics[2] == "hematofago" else False

if(path[0]):
    if(path[1]):
        if(path[2]):
            animal = "pomba"
        else:
            animal = "aguia"
    else:
        if(path[2]):
            animal = "homem"
        else:
            animal = "vaca"
else:
    if(path[1]):
        if(path[2]):
            animal = "pulga"
        else:
            animal = "lagarta"
    else:
        if(path[2]):
            animal = "sanguessuga"
        else:
            animal = "minhoca"

print(animal)