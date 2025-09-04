#1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

# informacoes = {'nome':'Eduardo', 'idade':20, 'cidade':'São Paulo'}

 #2 - Utilizando o dicionário criado no item 1:

# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
# Adicione um campo de profissão para essa pessoa;
# Remova um item do dicionário.

# informacoes['idade'] = 21
# informacoes



# print(informacoes)

#3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.

# quadrados = {}

# for i in range(1,6):
#     quadrados[i] = i**2


# print(quadrados)

#4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

# informacoes = {'nome':'Eduardo', 'idade':20, 'cidade':'São Paulo'}

# for i in informacoes:
#     if 'nome' in i:
#         print('essa chave existe no dicionáro')

#5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

#frase = 'banana maça laranja abrobinha banana'

# Transformar a frase em lista de palavras
#palavras = frase.split()

# Dicionário vazio para contar
#contador_palavras = {}

# Loop para contar cada palavra
# for palavra in palavras:
#     if palavra in contador_palavras:
#         contador_palavras[palavra] += 1  # incrementa se já existe
#     else:
#         contador_palavras[palavra] = 1   # adiciona se não existe

# print(contador_palavras)
