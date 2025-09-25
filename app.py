from models.restaurante import Restaurante
from models.cardapio.prato import Prato
from models.cardapio.bebida import Bebida

restaurante_massa = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.0, 'G')
prato_pao = Prato('Pão', 1.0, 'Pãozinho da casa')
restaurante_massa.receber_avaliacao('Gui', 9.5)
restaurante_massa.receber_avaliacao('Lais', 8.0)
restaurante_massa.receber_avaliacao('João', 5.0)
restaurante_pizza = Restaurante('pizza', 'Massas')
restaurante_pizza.receber_avaliacao('Gui', 3.5)
restaurante_pizza.receber_avaliacao('Lais', 4.0)
restaurante_pizza.receber_avaliacao('João', 2.0)
restaurante_sushi = Restaurante('Japa', 'Japones')

Restaurante.listar_restaurantes()

def main():
    pass

if __name__ == '__main__':
    main()