from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    # Primeiro vamos alterar todos os metodos com os prints e substituir por return

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.


        """
        super().__init__(restaurant_name, cuisine_type, is_open=True)
        self.flavors = flavors_list

    # metodo auxiliar para verificar se um input flavor é valido ou nao

    def is_flavor_input_valid(self, flavor_input):
        if flavor_input is not None:
            if isinstance(flavor_input, str):
                if flavor_input.isspace() is False:
                    return True

                else:
                    return False
            else:
                return False
        else:
            return False


    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""

        # Melhorar a estrutura da mensagem desse return

        if self.flavors:

            text = "\n No momento temos os seguintes sabores de sorvete disponíveis:"
            for flavor in self.flavors:
                text += f"\n\t-{flavor}"
            return text
        else:
            return "Estamos sem estoque atualmente!"

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""

        # Está retornando todos os sabores, vamos alterar para retornar apenas se existe ou nao o sabor informado

        if self.is_flavor_input_valid(flavor):
            if self.flavors:
                if flavor in self.flavors:
                    return f"Temos no momento {flavor}!"
                else:
                    return f"Não temos no momento {flavor}!"
            else:
                return "Estamos sem estoque atualmente!"
        else:
            return "Campo inválido"

    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque."""

        # Alterar o retorno desabor sem estoque, pq se estamos adicionando entao nao faz sentido a mensagem de erro para
        # estoque vazio
        if self.is_flavor_input_valid(flavor):
            if flavor in self.flavors:
                return "\nSabor já disponivel!"
            else:
                self.flavors.append(flavor)
                return f"{flavor} adicionado ao estoque!"
        else:
            return "Campo inválido"
