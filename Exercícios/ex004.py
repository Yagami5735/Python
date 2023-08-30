a = str(input('Digite algo: '))
print('Seu tipo é: {} \n Ele é numérico? {} \n Ele é alfabético? {} \n Ele é alphanumérico? {} \n Ele está  em letras maiúsculas? {} \n Ele está em letras minúsculas? {} \n ele está capitalizado? {}'
      .format(type(a), a.isnumeric(), a.isalpha(), a.isalnum(), a.isupper(), a.islower(), a.istitle()))
