import re

import signal
import os

# Expressão regular para validar o email
regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b'

# Expressão regular para validar o CPF (após integração)
regex_cpf = r'\b\d{9}\b'

def obter_email():
    while True:
        try:
            email = input("Por favor, digite seu Email: ")
            return email
        except ValueError:
            print("Por favor, digite apenas um Email válido.")

def check(email):
    if re.fullmatch(regex_email, email):
        print("Este Email", email, "é Válido")
    else:
        print("O Email", email, "É inválido")

def verificar_data():
    while True:
        try:
            data = int(input("Por favor, digite uma data, ex:(00/00/0000): "))
            tamanho = len(str(data))
            if tamanho != 8:
                print("A data", data, "não se encaixa nos padrões de data, necessário até 8 digitos")
            else:
                print("A data", data, "está correta")
                break
        except ValueError:
            print("Por favor, digite uma data válida.")

def verificar_numero():
    while True:
        try:
            inicio = int(input("Por favor, digite o primeiro número do intervalo:"))
            numero = int(input("Por favor, digite o número a ser verificado: "))
            fim = int(input("Por favor, digite o terceiro e último número do intervalo:"))
            if validar_numero(numero, inicio, fim):
                print("O número", numero, "está dentro do intervalo entre", inicio, "e", fim)
                break
            else:
                print("O número", numero, "está fora do intervalo entre", inicio, "e", fim)
        except ValueError:
            print("Por favor, digite apenas números.")

def validar_numero(numero, inicio, fim):
    return inicio <= numero <= fim

def obter_cpf():
    while True:
        try:
            cpf = str(input("Por favor, digite 9 digitos do seu CPF "))
            return cpf
        except ValueError:
            print("Por favor, digite apenas 9 digitos do seu CPF.")

def calcular_digitos_verificacao(cpf):
    soma = 0
    multiplicador = 10
    for digito in cpf:
        soma += int(digito) * multiplicador
        multiplicador -= 1
    resto = soma % 11
    primeiro_digito = 0 if resto < 2 else 11 - resto

    soma = 0
    multiplicador = 11
    cpf_com_primeiro_digito = cpf + str(primeiro_digito)
    for digito in cpf_com_primeiro_digito:
        soma += int(digito) * multiplicador
        multiplicador -= 1
    resto = soma % 11
    segundo_digito = 0 if resto < 2 else 11 - resto

    return primeiro_digito, segundo_digito

def verificar_cpf():
    cpf = obter_cpf()
    tamanhocpf = len(str(cpf))
    if tamanhocpf != 9:
        print("Por favor, a quantidade de números presentes no cpf", cpf, "não condizente com o necessário")
    else:
        primeiro_digito, segundo_digito = calcular_digitos_verificacao(cpf)
        print("Os dois últimos dígitos de verificação do CPF", cpf, "são:", primeiro_digito, segundo_digito)

def obter_lista():
    while True:
        try:
            numeros = input("Por favor, digite uma lista de números para somarmos (separe os números por espaço): ")
            numeros = [int(num) for num in numeros.split()]
            return numeros
        except ValueError:
            print("Por favor, digite apenas números.")

def somarLista():
    numeros = obter_lista()
    soma_individual = 0
    for numero in numeros:
        soma_individual += numero
    print("Esta é a soma dos números:", soma_individual)

def obter_palavra():
    while True:
        try:
            palavra = str(input("Por favor, digite uma palavra para conferirmos quantas vezes aparece a vogal A"))
            return palavra
        except ValueError:
            print("Por favor, digite apenas palavras.")

def contarCaractere(palavra):
    contagem = palavra.count('A') + palavra.count('a')
    return contagem

def celsius_fahrenheit():
    while True:
        try:
            c = float(input('Digite a temperatura em °c'))
            f = float((9 * c) / 5) + 32
            print('A temperatura em fahrenheit: {0}°F'.format(f))
            return f
        except ValueError:
            print("Digite apenas números")

def obter_maior():
    entrada = []
    while len(entrada) < 2:
        try:
            maior = int(input("Por favor, digite 2 números para descobrirmos qual o maior"))
            entrada.append(maior)
        except ValueError:
            print("Por favor, digite apenas números.")
    return entrada

def encontrarMaior(entrada):
    maior = max(entrada)
    return maior

def obter_frase():
    while True:
        try:
            frase = str(input("Digite uma palavra para inverter"))
            return frase
        except ValueError:
            print("Digite apenas números")

def fator():
    while True:
        try:
            resultado = int(input("Digite um numero para a verificação do fatorial: "))
            return resultado
        except ValueError:
            print("Por favor digite um numero")

def calcular_fatorial(valor):
    if valor == 0:
        return 1
    else:
        return valor * calcular_fatorial(valor -1)

def limpar_linhas(num_lines_to_clear):
    clear_text = "\n" * num_lines_to_clear
    print(clear_text)

def exibir_menu():
    print("Selecione uma opção:")
    print("1. Verificar Email")
    print("2. Verificar Data")
    print("3. Verificar Número")
    print("4. Verificar CPF")
    print("5. Somar Lista de Números")
    print("6. Contar Vogal 'A'")
    print("7. Converter Celsius para Fahrenheit")
    print("8. Encontrar o Maior Número")
    print("9. Inverter Palavra")
    print("10. Calcular Fatorial")
    print("11. Limpar Linhas")
    print("12. Sair")

def menu():
    while True:

        exibir_menu()
        escolha = input("Escolha uma opção: ")
        limpar_linhas(30)
#        system('cls' if name == 'nt' else 'clear')
        if escolha == "1":
            email = obter_email()
            check(email)

        elif escolha == "2":
            verificar_data()

        elif escolha == "3":
            verificar_numero()

        elif escolha == "4":
            verificar_cpf()

        elif escolha == "5":
            somarLista()

        elif escolha == "6":
            palavra = obter_palavra()
            quantidade_A = contarCaractere(palavra)
            print("A vogal A aparece um total de", quantidade_A, "vezes, na palavra" , palavra)

        elif escolha == "7":
            celsius_fahrenheit()

        elif escolha == "8":
            entrada = obter_maior()
            maior_numero = encontrarMaior(entrada)
            print("o maior número é:", maior_numero)

        elif escolha == "9":
            frase = obter_frase()
            invertida = ' '.join(palavra[::-1] for palavra in frase.split())
            print(invertida)

        elif escolha == "10":
            valor = fator()
            resultado = calcular_fatorial(valor)
            print("O fatorial de", valor, "é:", resultado)

        elif escolha == "11":
            num_lines_to_clear = int(input("Digite o número de linhas a serem limpas: "))

        elif escolha == "12":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Inicia o menu
menu()

# import re  # Importa o módulo re para trabalhar com expressões regulares
#
# import os *
#
# numeros = []
#
# # Expressão regular para validar o email
# regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b'
#
# # Expressão regular para validar o CPF (após integração)
# regex_cpf = r'\b\d{9}\b'
#
# def obter_email():  # Define uma função para obter o email do usuário
#     while True:
#         try:
#             email = str(input("Por favor, digite seu Email: "))  # Solicita ao usuário que insira o email
#             return email  # Retorna o email inserido
#         except ValueError:
#             print("Por favor, digite apenas um Email válido.")  # Exibe uma mensagem de erro se o email inserido for inválido
#
# def check(email):  # Define uma função para verificar se o email é válido
#     if re.fullmatch(regex_email, email):  # Usa a expressão regular para verificar se o email é válido
#         print("Este Email", email, "é Válido")  # Exibe uma mensagem se o email for válido
#     else:
#         print("o Email", email, "É inválido")  # Exibe uma mensagem se o email for inválido
#
# def verificar_data():  # Define uma função para verificar a data
#     while True:
#         try:
#             data = int(input("Por favor, digite uma data, ex:(00/00/0000): "))
#             tamanho = len(str(data))
#             if tamanho != 8:
#                 print("A data", data, "não se encaixa nos padrões de data, necessário até 8 digitos")
#             else:
#                 print("A data", data, "está correta")
#                 break
#         except ValueError:
#             print("Por favor, digite uma data válida.")  # Exibe uma mensagem de erro se a data inserida for inválida
#
# def verificar_numero():  # Define uma função para verificar um número dentro de um intervalo
#     while True:
#         try:
#             inicio = int(input("Por favor, digite o primeiro número do intervalo:"))
#             numero = int(input("Por favor, digite o número a ser verificado: "))
#             fim = int(input("Por favor, digite o terceiro e último número do intervalo:"))
#             if validar_numero(numero, inicio, fim):
#                 print("O número", numero, "está dentro do intervalo entre", inicio, "e", fim)
#                 break
#             else:
#                 print("O número", numero, "está fora do intervalo entre", inicio, "e", fim)
#         except ValueError:
#             print("Por favor, digite apenas números.")  # Exibe uma mensagem de erro se o valor inserido não for um número
#
# def validar_numero(numero, inicio, fim):  # Define uma função para validar se um número está dentro de um intervalo
#     return inicio <= numero <= fim
#
# def obter_cpf():  # Define uma função para obter o CPF do usuário
#     while True:
#         try:
#             cpf = str(input("Por favor, digite 9 digitos do seu CPF "))
#             return cpf
#         except ValueError:
#             print("Por favor, digite apenas 9 digitos do seu CPF.")  # Exibe uma mensagem de erro se o CPF inserido for inválido
#
# def calcular_digitos_verificacao(cpf):  # Define uma função para calcular os dois últimos dígitos de verificação do CPF
#     soma = 0
#     multiplicador = 10
#     for digito in cpf:
#         soma += int(digito) * multiplicador
#         multiplicador -= 1
#     resto = soma % 11
#     primeiro_digito = 0 if resto < 2 else 11 - resto
#
#     # Reinicializa as variáveis para o cálculo do segundo dígito
#     soma = 0
#     multiplicador = 11
#     cpf_com_primeiro_digito = cpf + str(primeiro_digito)
#     for digito in cpf_com_primeiro_digito:
#         soma += int(digito) * multiplicador
#         multiplicador -= 1
#     resto = soma % 11
#     segundo_digito = 0 if resto < 2 else 11 - resto
#
#     return primeiro_digito, segundo_digito  # Retorna os dois últimos dígitos de verificação do CPF
#
# def verificar_cpf():  # Define uma função para verificar o CPF
#     cpf = obter_cpf()  # Obtém o CPF do usuário
#     tamanhocpf = len(str(cpf))
#     if tamanhocpf != 9:  # Verifica se o CPF inserido tem 9 dígitos
#         print("Por favor, a quantidade de números presentes no cpf", cpf, "não condizente com o necessário")
#     else:
#         primeiro_digito, segundo_digito = calcular_digitos_verificacao(cpf)  # Calcula os dois últimos dígitos de verificação do CPF
#         print("Os dois últimos dígitos de verificação do CPF", cpf, "são:", primeiro_digito, segundo_digito)
#
# def obter_lista():
#     while True:
#         try:
#             numeros = input("Por favor, digite uma lista de números para somarmos (separe os números por espaço): ")
#             numeros = [int(num) for num in numeros.split()]
#             return numeros
#         except ValueError:
#             print("Por favor, digite apenas números.")
#
# def somarLista():
#     numeros = obter_lista()  # Chama a função para obter a lista de números
#     soma_individual = 0
#     for numero in numeros:
#         soma_individual += numero
#     print("Esta é a soma dos números:", soma_individual)
#
# def obter_palavra():
#     while True:
#         try:
#             palavra = str(input("Por favor, digite uma palavra para conferirmos quantas vezes aparece a vogal A"))
#             return palavra
#         except ValueError:
#             print("Por favor, digite apenas palavras.")
#
# def contarCaractere(palavra):
#         contagem = palavra.count('A') + palavra.count('a')
#         return contagem
#
# def celsius_fahrenheit():
#     while True:
#         try:
#             c = float(input('Digite a temperatura em °c'))
#             f = float((9 * c) / 5) + 32
#             print('A temperatura em fahrenheit: {0}°F'.format(f))
#             return f
#         except ValueError:
#             print("Digite apenas números")
#
# def obter_maior():
#     entrada = []
#     while len(entrada) < 2:
#         try:
#             maior = int(input("Por favor, digite 2 números para descobrirmos qual o maior"))
#             entrada.append(maior)
#         except ValueError:
#             print("Por favor, digite apenas números.")
#     return entrada
#
# def encontrarMaior(entrada):
#     maior = max(entrada)
#     return maior
#
# def obter_frase():
#     while True:
#         try:
#             frase = str(input("Digite uma palavra para inverter"))
#             return frase
#         except ValueError:
#             print("Digite apenas números")
#
# def fator():
#     while True:
#         try:
#             resultado = int(input("Digite um numero para a verificação do fatorial: "))
#             return resultado
#         except ValueError:
#             print("Por favor digite um numero")
#
# def calcular_fatorial(valor):
#     if valor == 0:
#         return 1
#     else:
#         return valor * calcular_fatorial(valor -1)
#
# def limpar_linhas(num_lines_to_clear):
#     clear_text = "\n" * num_lines_to_clear
#     print(clear_text)
#
# # Solicitar e verificar o email
# email = obter_email()  # Chama a função para obter o email
# check(email)  # Chama a função para verificar o email
# limpar_linhas(1)
# # print("\n" * os.get_terminal_size().lines)
#
#
# # Verificar a data
# verificar_data()  # Chama a função para verificar a data
# limpar_linhas(1)
# # Verificar o número
# verificar_numero()  # Chama a função para verificar o número
# limpar_linhas(1)
# # Verificar o CPF
# verificar_cpf()  # Chama a função para verificar o CPF
# limpar_linhas(1)
#
# somarLista()
# limpar_linhas(1)
#
# palavra = obter_palavra()
# quantidade_A = contarCaractere(palavra)
# print("A vogal A aparece um total de", quantidade_A, "vezes, na palavra" , palavra)
# limpar_linhas(1)
#
# celsius_fahrenheit()
# limpar_linhas(1)
#
# entrada = obter_maior()
# maior_numero = encontrarMaior(entrada)
# print("o maior número é:", maior_numero)
# limpar_linhas(1)
#
# frase = obter_frase()
# invertida = ' '.join(palavra[::-1] for palavra in frase.split())
# print(invertida)
# limpar_linhas(1)
#
# valor = fator()
# resultado = calcular_fatorial(valor)
# print("O fatorial de", valor, "é:", resultado)
# limpar_linhas(1)
