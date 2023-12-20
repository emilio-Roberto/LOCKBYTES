from time import sleep

from random import randrange

print('-'*4, 'LOCKBYTES', '-'*4)

ca = ['!', '@', '#', '$', '*', '&', '%', '(', ')', '-', '_', '=', '+', '/', '.', ':', ';', ',', 
      '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
      'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
      'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
      's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

a00 = str((ca [ randrange ( len ( ca ))]))
a01 = str((ca [ randrange ( len ( ca ))]))
a02 = str((ca [ randrange ( len ( ca ))]))
a03 = str((ca [ randrange ( len ( ca ))]))
a04 = str((ca [ randrange ( len ( ca ))]))
a05 = str((ca [ randrange ( len ( ca ))]))
a06 = str((ca [ randrange ( len ( ca ))]))
a07 = str((ca [ randrange ( len ( ca ))]))
a08 = str((ca [ randrange ( len ( ca ))]))
a09 = str((ca [ randrange ( len ( ca ))]))
a10 = str((ca [ randrange ( len ( ca ))]))
a11 = str((ca [ randrange ( len ( ca ))]))
a12 = str((ca [ randrange ( len ( ca ))]))
a13 = str((ca [ randrange ( len ( ca ))]))
a14 = str((ca [ randrange ( len ( ca ))]))
a15 = str((ca [ randrange ( len ( ca ))]))
a16 = str((ca [ randrange ( len ( ca ))]))
a17 = str((ca [ randrange ( len ( ca ))]))
a18 = str((ca [ randrange ( len ( ca ))]))
a19 = str((ca [ randrange ( len ( ca ))]))
a20 = str((ca [ randrange ( len ( ca ))]))
a21 = str((ca [ randrange ( len ( ca ))]))
a22 = str((ca [ randrange ( len ( ca ))]))
a23 = str((ca [ randrange ( len ( ca ))]))
a24 = str((ca [ randrange ( len ( ca ))]))
a25 = str((ca [ randrange ( len ( ca ))]))
a26 = str((ca [ randrange ( len ( ca ))]))
a27 = str((ca [ randrange ( len ( ca ))]))
a28 = str((ca [ randrange ( len ( ca ))]))
a29 = str((ca [ randrange ( len ( ca ))]))
a30 = str((ca [ randrange ( len ( ca ))]))
a31 = str((ca [ randrange ( len ( ca ))]))
a32 = str((ca [ randrange ( len ( ca ))]))

sleep(2)

qtca = int(input('Quantos caracteres (MIN:8 - MAX:32): '))

if qtca == 8:
    file = open('senhas.txt', 'a')
    s = (a00+a01+a02+a03+a04+a05+a06+a07+a08)
    print(s)
    file.write(s)
    file.close
elif qtca == 9:
    file = open('senhas.txt', 'a')
    s = str((a00+a01+a02+a03+a04+a05+a06+a07+a08+a09))
    print(s)
    file.writelines(s)
    file.close

elif qtca == 10:
    file = open('senhas.txt', 'a')
    s = (a00+a01+a02+a03+a04+a05+a06+a07+a08+a09+a10)
    print(s)
    file.write(s)
    file.close

elif qtca == 11:
    file = open('senhas.txt', 'a')
    s = (a00+a01+a02+a03+a04+a05+a06+a07+a08+a09+a10+a11)
    print(s)
    file.write(s)
    file.close

elif qtca == 12:
    file = open('senhas.txt', 'a')
    s = (a00+a01+a02+a03+a04+a05+a06+a07+a08+a09+a10+a11+a12)
    print(s)
    file.write(s)
    file.close

elif qtca == 13:
    file = open('senhas.txt', 'a')
    s = (a00+a01+a02+a03+a04+a05+a06+a07+a08+a09+a10+a11+a12+a13)
    print(s)
    file.write(s)
    file.close

elif qtca == 14:
    file = open('senhas.txt', 'a')
    s = (a00+a01+a02+a03+a04+a05+a06+a07+a08+a09+a10+a11+a12+a13+a14)
    print(s)
    file.write(s)
    file.close

elif qtca == 15:
    file = open('senhas.txt', 'a')
    s = (a00+a01+a02+a03+a04+a05+a06+a07+a08+a09+a10+a11+a12+a13+a14+a15,)
    print(s)
    file.write(s)
    file.close

elif qtca == 16:
    file = open('senhas.txt', 'a')
    s = (a00+a01+a02+a03+a04+a05+a06+a07+a08+a09+a10+a11+a12+a13+a14+a15+a16)
    print(s)
    file.write(s)
    file.close

elif qtca == 17:
    file = open('senhas.txt', 'a')
    s = (a00+a01+a02+a03+a04+a05+a06+a07+a08+a09+a10+a11+a12+a13+a14+a15+a16+a17)
    print(s)
    file.write(s)
    file.close

elif qtca == 18:
    file = open('senhas.txt', 'a')
    s = (a00+a01+a02+a03+a04+a05+a06+a07+a08+a09+a10+a11+a12+a13+a14+a15+a16+a17+a18)
    print(s)
    file.write(s)
    file.close

elif qtca ==19:
    file = open('senhas.txt', 'a')
    s = (a00+a01+a02+a03+a04+a05+a06+a07+a08+a09+a10+a11+a12+a13+a14+a15+a16+a17+a18+a19)
    print(s)
    file.write(s)
    file.close

elif qtca == 20:
    file = open('senhas.txt', 'a')
    s = (a00+a01+a02+a03+a04+a05+a06+a07+a08+a09+a10+a11+a12+a13+a14+a15+a16+a17+a18+a19+a20)
    print(s)
    file.write(s)
    file.close

elif qtca == 21:
    file = open('senhas.txt', 'a')
    s = (a00+a01+a02+a03+a04+a05+a06+a07+a08+a09+a10+a11+a12+a13+a14+a15+a16+a17+a18+a19+a20+a21)
    print(s)
    file.write(s)
    file.close

elif qtca == 22:
    file = open('senhas.txt', 'a')
    s = (a00+a01+a02+a03+a04+a05+a06+a07+a08+a09+a10+a11+a12+a13+a14+a15+a16+a17+a18+a19+a20+a21+a22)
    print(s)
    file.write(s)
    file.close

elif qtca == 23:
    file = open('senhas.txt', 'a')
    s =(a00+a01+a02+a03+a04+a05+a06+a07+a08+a09+a10+a11+a12+a13+a14+a15+a16+a17+a18+a19+a20+a21+a22+a23)
    print(s)
    file.write(s)
    file.close

elif qtca == 24:
    file = open('senhas.txt', 'a')
    s =(a00+a01+a02+a03+a04+a05+a06+a07+a08+a09+a10+a11+a12+a13+a14+a15+a16+a17+a18+a19+a20+a21+a22+a23+a24)
    print(s)
    file.write(s)
    file.close

elif qtca == 25:
    file = open('senhas.txt', 'a')
    s = (a00+a01+a02+a03+a04+a05+a06+a07+a08+a09+a10+a11+a12+a13+a14+a15+a16+a17+a18+a19+a20+a21+a22+a23+a24+a25)
    print(s)
    file.write(s)
    file.close

elif qtca == 26:
    file = open('senhas.txt', 'a')
    s =(a00+a01+a02+a03+a04+a05+a06+a07+a08+a09+a10+a11+a12+a13+a14+a15+a16+a17+a18+a19+a20+a21+a22+a23+a24+a25+a26)
    print(s)
    file.write(s)
    file.close

elif qtca == 27:
    file = open('senhas.txt', 'a')
    s = (a00+a01+a02+a03+a04+a05+a06+a07+a08+a09+a10+a11+a12+a13+a14+a15+a16+a17+a18+a19+a20+a21+a22+a23+a24+a25+a26+a27)
    print(s)
    file.write(s)
    file.close

elif qtca == 28:
    file = open('senhas.txt', 'a')
    s = (a00+a01+a02+a03+a04+a05+a06+a07+a08+a09+a10+a11+a12+a13+a14+a15+a16+a17+a18+a19+a20+a21+a22+a23+a24+a25+a26+a27+a28)
    print(s)
    file.write(s)
    file.close

elif qtca == 29:
    file = open('senhas.txt', 'a')
    s = (a00+a01+a02+a03+a04+a05+a06+a07+a08+a09+a10+a11+a12+a13+a14+a15+a16+a17+a18+a19+a20+a21+a22+a23+a24+a25+a26+a27+a28+a29)
    print(s)
    file.write(s)
    file.close

elif qtca == 30:
    file = open('senhas.txt', 'a')
    s = (a00+a01+a02+a03+a04+a05+a06+a07+a08+a09+a10+a11+a12+a13+a14+a15+a16+a17+a18+a19+a20+a21+a22+a23+a24+a25+a26+a27+a28+a29+a30)
    print(s)
    file.write(s)
    file.close

elif qtca == 31:
    file = open('senhas.txt', 'a')
    s = (a00+a01+a02+a03+a04+a05+a06+a07+a08+a09+a10+a11+a12+a13+a14+a15+a16+a17+a18+a19+a20+a21+a22+a23+a24+a25+a26+a27+a28+a29+a30+a31)
    print(s)
    file.write(s)
    file.close

elif qtca == 32:
    file = open('senhas.txt', 'a')
    s = (a00+a01+a02+a03+a04+a05+a06+a07+a08+a09+a10+a11+a12+a13+a14+a15+a16+a17+a18+a19+a20+a21+a22+a23+a24+a25+a26+a27+a28+a29+a30+a31+a32)
    print(s)
    file.write(s)
    file.close

else:
    print('Opção inválida!! Desligando')
