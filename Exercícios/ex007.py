sal = float(input("Digite o valor do salário: "))

if sal > 1250:
    nsal = sal*1.1
    print("O reajuste salarial foi de 10%, o novo salário é de R${:.2f}".format(nsal))
    
else:
    nsal = sal*1.15
    print("O reajuste salarial foi de 15%, o novo salário é de R${:.2f}".format(nsal))
