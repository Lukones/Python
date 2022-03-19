def notas(*n, sit=False):
    """
    -> Função para analisar notas e siituação de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
    return  r


resp = notas(10, 20, 30, 5, 1, 0, 3, sit=True)
for k, v in resp.items():
        print(f'{k} Foi: {v}')
