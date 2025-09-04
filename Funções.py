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
intervalos = {
    '0-25': 0,
    '26-50': 0,
    '51-75': 0,
    '76-100': 0
}

idade = int(input('Digite uma idade: '))

while idade >= 0:
    if 0 <= idade <= 25:
        intervalos['0-25'] += 1
    elif 26 <= idade <= 50:
        intervalos['26-50'] += 1
    elif 51 <= idade <= 75:
        intervalos['51-75'] += 1
    elif 76 <= idade <= 100:
        intervalos['76-100'] += 1
    
    idade = int(input('Digite uma idade: '))

print('Encerrando aplicação...')
for intervalo, count in intervalos.items():
    print(f'[{intervalo}] = {count}')
