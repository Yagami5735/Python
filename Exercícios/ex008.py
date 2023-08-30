r1 = float(input("Digite o valor de um dos segmentos: "))
r2 = float(input("Digite o valor de outro segmento: "))
r3 = float(input("Digite o valor de outro segmento: "))

if(r1<(r2+r2) and r2<(r1+r3) and r3<(r1+r2)):
    print("Ele forma um triângulo!!!")

else:
    print("Ele não forma um triângulo!!!")