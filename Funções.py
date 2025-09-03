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