loops = int(input())
for loop in range(loops):
    cryptograph = list(input())
    for _ in range(len(cryptograph)):
        if cryptograph[_].isalpha():
            cryptograph[_] = (chr(ord(cryptograph[_])+(3)))
    cryptograph = cryptograph[::-1]
    for _ in range( 1 ,((len(cryptograph)//2)+1) if (len(cryptograph)/2)%1 == 0 else ((len(cryptograph)//2)+2)):
        cryptograph[-_] = (chr(ord(cryptograph[-_])-1))