#!/bin/bash#!/usr/bin/env python3
print('Bem-vindo à calculadora inteligente')
print('-----------------------------------')

while True:  # Loop principal que continua até o usuário escolher sair
    print('Qual operação você deseja realizar? ')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Sair da calculadora')

    try:
        operacao = int(input('Digite o número da operação desejada: '))
    except ValueError:
        print("Entrada inválida! Por favor, digite um número entre 1 e 5.")
        continue  # Retorna ao início do loop principal para nova tentativa

    if operacao == 5:
        print('Obrigado por usar a calculadora!')
        break  # Sai do loop principal

    elif operacao in [1, 2, 3, 4]:  # Verifica se a operação é válida antes de pedir os números
        num_1 = float(input('Digite o primeiro número: '))
        num_2 = float(input('Digite o segundo número: '))

        if operacao == 1:
            resultado = num_1 + num_2
            print('O resultado da soma é:', resultado)

        elif operacao == 2:
            resultado = num_1 - num_2
            print('O resultado da subtração é:', resultado)

        elif operacao == 3:
            resultado = num_1 * num_2
            print('O resultado da multiplicação é:', resultado)

        elif operacao == 4:
            if num_2 != 0:  # Verifica se o divisor é diferente de zero
                resultado = num_1 / num_2
                print('O resultado da divisão é:', resultado)
            else:
                print('Erro: Divisão por zero não é permitida.')
    else:
        print('Operação inválida. Tente novamente.')

    print('-----------------------------------')  # Separador entre operações

