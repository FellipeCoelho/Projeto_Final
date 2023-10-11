from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand:

    def test_flavors_available_success(self):
        icecream = IceCreamStand('Della Nonna', 'Gellateria', ['Chocolate', 'Strawberry', 'Vanilla'])

        response = icecream.flavors_available()

        expected_response = ('\n No momento temos os seguintes sabores de sorvete '
                             'disponíveis:\n\t-Chocolate\n\t-Strawberry\n\t-Vanilla')

        assert expected_response == response

    def test_flavors_available_empty(self):
        icecream = IceCreamStand('Della Nonna', 'Gellateria', [])

        response = icecream.flavors_available()

        expected_response = 'Estamos sem estoque atualmente!'

        assert expected_response == response

    def test_find_flavor_success(self):
        icecream = IceCreamStand('Della Nonna', 'Gellateria', ['Chocolate', 'Strawberry', 'Vanilla'])

        response = icecream.find_flavor('Vanilla')

        expected_response = 'Temos no momento Vanilla!'

        assert expected_response == response

    def test_find_flavor_not_found(self):
        icecream = IceCreamStand('Della Nonna', 'Gellateria', ['Chocolate', 'Strawberry', 'Vanilla'])

        response = icecream.find_flavor('Green Tea')

        expected_response = 'Não temos no momento Green Tea!'

        assert expected_response == response

    def test_find_flavor_not_found_empty_list(self):
        icecream = IceCreamStand('Della Nonna', 'Gellateria', [])

        response = icecream.find_flavor('Espresso')

        expected_response = 'Estamos sem estoque atualmente!'

        assert expected_response == response

    def test_find_flavor_invalid_input_1(self):
        icecream = IceCreamStand('Della Nonna', 'Gellateria', ['Chocolate', 'Strawberry', 'Vanilla'])

        response = icecream.find_flavor(123)

        expected_response = 'Campo inválido'

        assert expected_response == response

    def test_find_flavor_invalid_input_2(self):
        icecream = IceCreamStand('Della Nonna', 'Gellateria', ['Chocolate', 'Strawberry', 'Vanilla'])

        response = icecream.find_flavor(None)

        expected_response = 'Campo inválido'

        assert expected_response == response

    def test_find_flavor_invalid_input_3(self):
        icecream = IceCreamStand('Della Nonna', 'Gellateria', ['Chocolate', 'Strawberry', 'Vanilla'])

        response = icecream.find_flavor(' ')

        expected_response = 'Campo inválido'

        assert expected_response == response

    def test_find_flavor_invalid_input_4(self):
        icecream = IceCreamStand('Della Nonna', 'Gellateria', ['Chocolate', 'Strawberry', 'Vanilla'])

        response = icecream.find_flavor(False)

        expected_response = 'Campo inválido'

        assert expected_response == response

    def test_add_flavor_success(self):
        icecream = IceCreamStand('Della Nonna', 'Gellateria', ['Chocolate', 'Strawberry', 'Vanilla'])

        response = icecream.add_flavor('Espresso')

        expected_response = 'Espresso adicionado ao estoque!'

        assert expected_response == response

    def test_add_flavor_duplicated(self):
        icecream = IceCreamStand('Della Nonna', 'Gellateria', ['Chocolate', 'Strawberry', 'Vanilla'])

        response = icecream.add_flavor('Vanilla')

        expected_response = '\nSabor já disponivel!'

        assert expected_response == response

    def test_add_flavor_in_an_empty_list(self):
        icecream = IceCreamStand('Della Nonna', 'Gellateria', [])

        response = icecream.add_flavor('Green Tea')

        expected_response = 'Green Tea adicionado ao estoque!'

        assert expected_response == response

    def test_add_flavor_invalid_input_1(self):
        icecream = IceCreamStand('Della Nonna', 'Gellateria', [])

        response = icecream.add_flavor(123)

        expected_response = 'Campo inválido'

        assert expected_response == response

    def test_add_flavor_invalid_input_2(self):
        icecream = IceCreamStand('Della Nonna', 'Gellateria', [])

        response = icecream.add_flavor(None)

        expected_response = 'Campo inválido'

        assert expected_response == response

    def test_add_flavor_invalid_input_3(self):
        icecream = IceCreamStand('Della Nonna', 'Gellateria', [])

        response = icecream.add_flavor(False)

        expected_response = 'Campo inválido'

        assert expected_response == response

    def test_add_flavor_invalid_input_4(self):
        icecream = IceCreamStand('Della Nonna', 'Gellateria', [])

        response = icecream.add_flavor(' ')

        expected_response = 'Campo inválido'

        assert expected_response == response
