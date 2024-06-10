import math


def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[2:]  # Começamos a partir de n=2


def soma_serie(fib_sequence, num_terms):
    soma_total = 0
    for n in fib_sequence[:num_terms]:
        if n > 1:
            termo = 1 / (n * (math.log(n)**2))
            soma_total += termo
    return soma_total


def verificar_convergencia(fib_sequence, num_terms, tolerancia=1e-6):
    soma_anterior = 0
    for i in range(2, num_terms):
        soma_atual = soma_serie(fib_sequence, i)
        if abs(soma_atual - soma_anterior) < tolerancia:
            return True
        soma_anterior = soma_atual
    return False


num_fib_termos = 1000
fib_sequence = fibonacci(num_fib_termos)


converge = verificar_convergencia(fib_sequence, num_fib_termos)

if converge:
    print("A série converge.")
else:
    print("A série não converge.")
