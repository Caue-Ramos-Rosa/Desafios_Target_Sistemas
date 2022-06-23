def verifica_fibonacci(alvo: int, num1=0, num2=1 ):
    prox = num1 + num2
    if prox == alvo or alvo == 0:
        return print('O número pertence a sequência')
    elif prox > alvo:
        return print('O número não pertence a sequência')
    else:
        return verifica_fibonacci(alvo, num2, prox)

print(verifica_fibonacci((int(input('digite um numero: ')))))
