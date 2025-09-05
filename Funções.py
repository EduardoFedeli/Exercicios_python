# #Exercicio 5
# lista = [3, 7, 10, 11, 2, 9]
# soma = 0

# for i in lista:
#     if i % 2 == 1 and i > 5:
#         soma = soma + i

# print(soma)

#-----------------------------------------------------------|

#Exercício 6
# fruta = 'banana'
# contador = 0

# for a in fruta:
#      contador = fruta.count(a)

# print(contador)


#|---------------------------------------------------------------------------------------------------------------------------------|

# # 1 - Crie uma lista para cada informação a seguir:

# # Lista de números de 1 a 10;
# # Lista com quatro nomes;
# # Lista com o ano que você nasceu e o ano atual.

# lista_numero = [1,2,3,4,5,6,7,8,9,10]
# lista_nomes = ['Eduardo', 'Gabriel', 'Otavio', 'Murilo']
# lista_anos = [2005, 2025]

#|---------------------------------------------------------------------------------------------------------------------------------|

# # 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

# lista_numero = [1,2,3,4,5,6,7,8,9,10]

# soma = 0
# for i in lista_numero:
#     if i % 2 != 0:
#         soma += i
#     else:
#         pass

# print(f'A soma dos números ímpares é {soma}')

#|---------------------------------------------------------------------------------------------------------------------------------|


# # 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

# lista_numero = [1,2,3,4,5,6,7,8,9,10]

# for numero in reversed(lista_numero):
#     if numero % 2 == 0:
#         print(numero)
#     else:
#         pass

#|---------------------------------------------------------------------------------------------------------------------------------|

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

# numero = int(input("Digite um número: "))

# for i in range(1,11):
#     resultado = numero * i
#     print(f'{numero} x {i} = {resultado}')

#|---------------------------------------------------------------------------------------------------------------------------------|

# # 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

# lista_numero = [1,2,3,4,5,6,7,8,9,10]

# soma = 0 

# try:
#     for i in lista_numero:
#         soma += i
# except TypeError:
#     print('Erro: todos os elementos da lista devem ser números.')
# else:
#     print(f'a soma de todos os elementos ad lista é: {soma}')

# # 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

# lista = [1,2,3,4,5,6,7,8,9,10]
# soma = 0

# for i in lista:
#         soma = soma + i

# try:
#     media = soma / len(lista)
# except ZeroDivisionError:
#     print('A lista precisa estar preenchida com número inteiros!')
# else:
#     print(f'A media da lista é: {media}')


#1) Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.

# num1 = int(input('Digite um número '))
# num2 = int(input('Digite o segundo numero: '))

# lista = range(num1, num2)

# for i in lista:
#     if i > num1 and i < num2:
#         print(i)


# print(lista)

#2) Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B,
#  com base nas taxas de crescimento de 3% e 1,5% respectivamente. 
# Considere que a colônia A inicia com 4 elementos e a B com 10.

# colonia_A = 4
# colonia_B = 10

# dias = 0

# while colonia_A < colonia_B:
#     colonia_A *= 1.03
#     colonia_B *= 1.015

#     dias += 1

# print(dias)

#3) Para tratar uma quantidade de 15 dados de avaliações de pessoas usuárias de um serviço da empresa, precisamos verificar se as notas são válidas. 
# Então, escreva um programa que vai receber a nota de 0 a 5 de todos os dados e verificar se é um valor válido. 
# Caso seja inserido uma nota acima de 5 ou abaixo de 0, repita até que a pessoa usuária insira um valor válido.

# lista = []

# while len(lista) < 15:
#     avaliacao = int(input('Digite um número de 0 a 5: '))
#     if avaliacao >= 0 and avaliacao <= 5:
#         lista.append(avaliacao)
#     else:
#         print('Você precisa digitar um valor entre 0 e 5')

# print(lista)


#5) Escreva um programa que calcule o fatorial de um número inteiro fornecido pela pessoa usuária. 
# Lembrando que o fatorial de um número inteiro é a multiplicação desse número por todos os seus antecessores até o número 1. 
# Por exemplo, o fatorial de 5 é 5 x 4 x 3 x 2 x 1 = 120.

# numero = int(input('Digite um número:'))

# resultado = 1

# contador = numero

# while contador >= 1:
#     resultado = resultado * contador
#     contador = contador - 1

# print(resultado)

#7) Os números primos possuem várias aplicações dentro da Ciência de Dados em criptografia e segurança, por exemplo. 
# Um número primo é aquele que é divisível apenas por um e por ele mesmo. 
# Assim, faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

# n = int(input("Digite um número inteiro: "))

# if n <= 1:
#     print("Não é primo")
# else:
#     primo = True
#     for i in range(2, n):
#         if n % i == 0:
#             primo = False
#             break
#     if primo:
#         print("É primo")
#     else:
#         print("Não é primo")

#8) Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência. 
# Escreva um programa que leia as idades de uma quantidade não informada de clientes e mostre a distribuição em intervalos de [0-25], [26-50], [51-75] e [76-100]. 
# Encerre a entrada de dados com um número negativo.

# Criando um dicionário com os intervalos e suas contagens
# intervalos = {
#     '0-25': 0,
#     '26-50': 0,
#     '51-75': 0,
#     '76-100': 0
# }

# idade = int(input('Digite uma idade: '))

# while idade >= 0:
#     if 0 <= idade <= 25:
#         intervalos['0-25'] += 1
#     elif 26 <= idade <= 50:
#         intervalos['26-50'] += 1
#     elif 51 <= idade <= 75:
#         intervalos['51-75'] += 1
#     elif 76 <= idade <= 100:
#         intervalos['76-100'] += 1
    
#     idade = int(input('Digite uma idade: '))

# print('Encerrando aplicação...')
# for intervalo, count in intervalos.items():
#     print(f'[{intervalo}] = {count}')

# 9) Em uma eleição para gerência em uma empresa com 20 pessoas colaboradoras, existem quatro candidatos(as). 
# Escreva um programa que calcule o(a) vencedor(a) da eleição. A votação ocorreu da seguinte maneira:

# Cada colaborador(a) votou em uma das quatro pessoas candidatas (que representamos pelos números 1, 2, 3 e 4).
# Também foram contabilizados os votos nulos (representados pelo número 5) e os votos em branco (representados pelo número 6).
# Ao final da votação, o programa deve exibir o número total de votos para cada candidato(a), os nulos e os votos em branco. 
# Além disso, deve calcular e exibir a porcentagem de votos nulos em relação ao total de votos e a porcentagem de votos em branco em relação ao total de votos.

# contador = 0


# candidatos = {
#     'candidato1': 0,
#     'candidato2': 0,
#     'candidato3': 0,
#     'candidato4': 0
# }


# invalidos = {
#     'voto_nulo': 0,
#     'voto_branco': 0
# }

# while contador < 20:
#     print('--- Votação ---')
#     print('1 - Candidato 1')
#     print('2 - Candidato 2')
#     print('3 - Candidato 3')
#     print('4 - Candidato 4')
#     print('5 - Voto nulo')
#     print('6 - Voto em branco')

#     try:
#         voto = int(input('Digite o número de seu voto: '))
#     except ValueError:
#         print('Entrada inválida. Digite um número entre 1 e 6.')
#         continue

#     if voto == 1:
#         candidatos['candidato1'] += 1
#     elif voto == 2:
#         candidatos['candidato2'] += 1
#     elif voto == 3:
#         candidatos['candidato3'] += 1
#     elif voto == 4:
#         candidatos['candidato4'] += 1
#     elif voto == 5:
#         invalidos['voto_nulo'] += 1
#     elif voto == 6:
#         invalidos['voto_branco'] += 1
#     else:
#         print('Digite um número válido (1 a 6).')
#         continue 

#     contador += 1

# print('\nEncerrando a votação...\n')


# print('--- Votos por candidato ---')
# for nome, qtd in candidatos.items():
#     print(f'{nome}: {qtd} votos')


# print('\n--- Votos inválidos ---')
# print(f"Votos nulos: {invalidos['voto_nulo']}")
# print(f"Votos em branco: {invalidos['voto_branco']}")


# total_votos = sum(candidatos.values()) + sum(invalidos.values())  
# pct_nulo = (invalidos['voto_nulo'] / total_votos) * 100 if total_votos else 0
# pct_branco = (invalidos['voto_branco'] / total_votos) * 100 if total_votos else 0

# print(f'\nPercentual de votos nulos: {pct_nulo:.2f}%')
# print(f'Percentual de votos em branco: {pct_branco:.2f}%')


# max_votos = max(candidatos.values())
# vencedores = [k for k, v in candidatos.items() if v == max_votos]

# if len(vencedores) == 1:
#     print(f'\n🏆 Vencedor: {vencedores[0]} com {max_votos} votos')
# else:
#     print('\n⚠ Empate entre candidatos:')
#     for w in vencedores:
#         print(f' - {w}: {candidatos[w]} votos')


# 1) Faça um programa que tenha a seguinte lista contendo os valores de gastos de uma empresa de papel 
# [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]. 
# Com esses valores, faça um programa que calcule a média de gastos. Dica: use as funções built-in sum() e len().

# lista = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

# media = (sum(lista)/len(lista))

# print(f"Média = {media:.2f}")

#2) Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem quanto ao total de compras.

# acima = []

# for i in lista:
#     if i > 3000:
#         acima.append(i)

# qtd_acima = len(acima)            
# total = len(lista)                  
# percentual = (qtd_acima / total) * 100  

# print(f"Compras acima de 3000: {qtd_acima}")
# print(f"Percentual: {percentual:.2f}%")

#3) Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista. Exemplo: [1,4,7,2,4].

# numeros = []

# for i in range(5):
#     n = int(input("Digite um número inteiro: "))
#     numeros.append(n)

# print("Lista final:", numeros)

#4) Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.

# numeros = []

# for i in range(5):
#     n = int(input("Digite um número inteiro: "))
#     numeros.append(n)

# # imprimir lista invertida
# print("Lista invertida:", numeros[::-1])

# 5) Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos os números primos entre 1 e o número digitado.
# lista = []
# numero = int(input("Digite um número: "))

# for n in range(2, numero + 1):
#     primo = True
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             primo = False
#             break 
#     if primo:
#         lista.append(n)

# print("Números primos até", numero, ":", lista)