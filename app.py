import requests
import json
from models.restaurante import Restaurante
from models.cardapio.prato import Prato
from models.cardapio.bebida import Bebida

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)
print(response)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_restaurante = item['Company']
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = []
        
        dados_restaurante[nome_restaurante].append({
            "item": item['Item'],
            "preco": item['price'],
            "descricao": item['description']
        })
else:
    print(f'O erro foi {response.status_code}')

for nome_restaurante, dados in dados_restaurante.items():
    nome_arquivo = f'{nome_restaurante}.json'
    with open(nome_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)


""" restaurante_massa = Restaurante('Massa da Nona', 'Massas e pizzas')
bebida_suco = Bebida('Suco de Melancia', 5.0, 'G')
bebida_suco.aplicar_desconto()
prato_pao = Prato('Pão', 1.0, 'Pãozinho da casa')
prato_pao.aplicar_desconto()
restaurante_massa.adicionar_no_cardapio(bebida_suco)
restaurante_massa.adicionar_no_cardapio(prato_pao)

Restaurante.listar_restaurantes()

def main():
    restaurante_massa.exibir_cardapio

if __name__ == '__main__':
    main() """