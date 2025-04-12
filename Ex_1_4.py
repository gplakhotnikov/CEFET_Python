nome = 'João da Silva'
cidade = 'São Paulo'
cpf = '123.456.789-00'

print(f'Em maiúsculo: \n {nome.upper()} \n {cidade.upper()} \n {cpf.upper()}')
print(f'Em minúsculo: \n {nome.lower()} \n {cidade.lower()} \n {cpf.lower()}')
print('Posição do caractere "ã" (se não tiver imprime "-1"):', nome.find("ã"), cidade.find("ã"), cpf.find("ã"))
print('Número de caracteres de cada variável:', len(nome), len(cidade), len(cpf))
print('Número de CPF sem os pontos e o hífen:', cpf.translate({ord(i): None for i in "-."}))
