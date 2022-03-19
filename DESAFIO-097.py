def fatorial(a, show=False):
    """ Fatorial (n, show=False)
        --> Calcula o Fatorial de um número.
        : param n: O número a ser calculado.
        : param show: (Opcional) Mostrar ou não a conta.
        : return: O valor do Fatoriial de um número n."""
    f = 1
    if show == True:
        print('*' * 30)
        for c in range(a, 0, -1):
            if show:
                print(c, end='')
                if c > 1:
                    print(' x ', end='')
                else:
                    print(' = ', end='')
            f *= c
        return f'{f}'
    else:
        print('*' * 30)
        for c in range(a, 0, -1):
            f *= c
        print(f'O fatorial de {a} ', end='')
        return f'é {f}'




print(fatorial(5, show=True))
