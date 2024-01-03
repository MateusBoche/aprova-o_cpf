"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
    1  4  6  0  4  4  1  1 6 
    10 36 48 0  24 20 4  3 12
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

import re

while True:
    cpf = input("Digite seu cpf: ").replace(".","")\
        .replace("-","")\
        .replace(" ","")


    #cpf = re.sub(r"[^0-9]","",cpf)
    

    if len(cpf) > 11:
        print("Seu cpf tem muito digitos")
        continue
    elif len(cpf) < 11:
        print(" seu cpf tem poucos digitos")
        continue
    elif cpf == cpf[0] * len(cpf):
        print("Você digitou numeros repetidos")
        continue
    else:
        primeiros_digitos_cpf = cpf[0:9]
        print(primeiros_digitos_cpf)
        i = 0
        n = 10
        tam = len(primeiros_digitos_cpf)
        new_cpf = 0
        while i < tam:
            conta = int(primeiros_digitos_cpf[i]) * n
            i = i +1
            n = n - 1
            new_cpf += conta
        print(new_cpf)
        new_cpf = new_cpf * 10
        new_cpf = new_cpf % 11
        digito = new_cpf
        ver_primeiro_digito = 0 if digito > 9 else digito
    print(cpf[9])
    teste = int(cpf[9])

    print(f"O primeiro digito do seu cpf é {ver_primeiro_digito}")
    new_cpf2 = 0
    if ver_primeiro_digito == teste:
        segundo_digito_cpf = cpf[0:10]
        print(segundo_digito_cpf)
        contagem_regressiva = 11
        for i in segundo_digito_cpf:
            conta2 = int(i) * contagem_regressiva
            new_cpf2 += int(conta2)
            contagem_regressiva -= 1
        print(new_cpf2)
        new_cpf2 = new_cpf2 *10
        new_cpf2 = new_cpf2 % 11
        ver_segundo_digito = 0 if new_cpf2 > 9 else new_cpf2
        print(f"O segundo digito do seu cpf é {ver_segundo_digito}")

    if ver_primeiro_digito == int(cpf[9]) and ver_segundo_digito == int(cpf[10]):
        print("Cpf é valido")
    else:
        print("Cpf invaldio")
