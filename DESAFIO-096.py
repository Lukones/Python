def vota(n=0):
    from datetime import date
    s = date.today().year - n
    if s < 16:
        return f'A sua idade é de {s} seu voto: NEGADO'
    elif 16 <= s < 18 or s > 65:
        return f'A sua idade é de {s} seu voto: OPCIONAL'
    else:
        return f'A sua idade é de {s} seu voto: OBRIGATÓRIO'


resp = int(input('Digite ano de nascimento: '))
print(vota(resp))