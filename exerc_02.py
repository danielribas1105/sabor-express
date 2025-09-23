
def calcular_idade(ano_nascimento, ano_atual):
    return ano_atual - ano_nascimento

ano_nascimento = input('Digite o ano de nascimento: ')
ano_atual = input('Digite o ano atual: ')

print(f'A idade é {calcular_idade(int(ano_nascimento), int(ano_atual))} anos.')