nome = str(input('Digite seu nome: '))

# " : " -> faz com que você possa definir quantos caracteres esse print vai ter
# " > " -> faz com que ele fique alinhado na direita
# " < " -> faz com que ele fique alinhado na esquerda
# " ^ " -> faz com que ele fique alinhado no meio
# obs: o ":" vem primeiro, o que vier depois dele será executado, por exemplo, em ":!20" o "!" será preenchido onde não tiver caracteres

'''ex:
print('Olá {:=>20}'.format(nome))
print('Olá {:=<20}'.format(nome))
print('Olá {:=^20}'.format(nome))
# sem o "="
print('Olá {:>20}'.format(nome))
print('Olá {:<20}'.format(nome))
print('Olá {:^20}'.format(nome))
'''
# ex2:
# obs: o "5" delimita a quantidade de caracteres que vai printar, se o nome for maior que 5, ele não irá preencher com o caractere escolhido
print('Olá {:!<5}'.format(nome))
