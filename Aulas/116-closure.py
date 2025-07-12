'''
Closure e funções que retornam outras funções
'''

def cria_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

retornar_bom_dia = cria_saudacao('Bom dia')
retornar_boa_noite = cria_saudacao('Boa noite')


for nome in ['Maria', 'João', 'Gabriel']:
    print(retornar_bom_dia(nome))
    print(retornar_boa_noite(nome))