vel = float(input("Qual a velocidade do carro? "))

if (vel <= 80):
    print("Bom dia, dirija em segurança e tenha uma Boa Viagem!!!")

else:
    multa = (vel - 80)*7
    print("Você foi multado! O valor da multa é de R${:.2f}".format(multa))
