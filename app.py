from model.restaurante_old import Restaurante

restaurante_massa = Restaurante('praça', 'Gourmet')
restaurante_massa.receber_avaliacao('Gui', 9.5)
restaurante_pizza = Restaurante('pizza', 'Massas')
restaurante_sushi = Restaurante('Japa', 'Japones')

Restaurante.listar_restaurantes()

def main():
    pass

if __name__ == '__main__':
    main()