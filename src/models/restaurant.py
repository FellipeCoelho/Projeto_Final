class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type, is_open):
        # Precisamos incluir number_served e open nos parametros de entrada

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = is_open

    # Primeiramente vamos alterar todos os print nos metodos para um return

    # method auxiliar que valida se uma entrada de numeros de clientes é válida ou nao :)
    def input_number_clients_valid(self, number):
        if number is not None:
            if isinstance(number, int) and number >= 0:
                return True
            else:
                return False
        else:
            return False


    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""

        # O nome do restaurante estava retornando o tipo de culinaria
        # O number_serverd sempre estava retornando 0

        description = f'Esse restaturante chama {self.restaurant_name} and serve {self.cuisine_type}.\n' \
                      f'Esse restaturante está servindo {self.number_served} consumidores desde que está aberto.'

        return description

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""

        # number_served estava setado com um numero negativo

        if not self.open:
            self.open = True
            self.number_served = 0
            return f"{self.restaurant_name} agora está aberto!"
        else:
            return f"{self.restaurant_name} já está aberto!"

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""

        if self.open:
            self.open = False
            self.number_served = 0
            return f"{self.restaurant_name} agora está fechado!"
        else:
            return f"{self.restaurant_name} já está fechado!"

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""

        if self.open:
            if self.input_number_clients_valid(total_customers):
                self.number_served = total_customers
                return self.number_served
            else:
                return "Entrada inválida"
        else:
            return f"{self.restaurant_name} está fechado!"

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""

        # corrigindo a inclusao da soma de mais clientes (acredito que deveria incrementar o numero de clientes ao total)

        if self.open:
            if self.input_number_clients_valid(more_customers):
                self.number_served += more_customers
                return self.number_served
            else:
                return "Entrada inválida"
        else:
            return f"{self.restaurant_name} está fechado!"
