from src.models.restaurant import Restaurant

class TestRestaurant:

    def test_describe_restaurant_success(self):
        restaurant = Restaurant('Cozudo', "Comida Italiana", True)

        restaurant.set_number_served(15)

        expected_response = 'Esse restaturante chama Cozudo and serve Comida Italiana.\n' \
                            'Esse restaturante está servindo 15 consumidores desde que está aberto.'

        response = restaurant.describe_restaurant()

        assert expected_response == response

    def test_open_restaurant(self):
        restaurant = Restaurant('Toca do Gabiru', "Comida de Boteco", False)

        expected_response = 'Toca do Gabiru agora está aberto!'

        response = restaurant.open_restaurant()

        assert expected_response == response

    def test_open_restaurant_already_opened(self):
        restaurant = Restaurant('Toca do Gabiru', "Comida de Boteco", True)

        expected_response = 'Toca do Gabiru já está aberto!'

        response = restaurant.open_restaurant()

        assert expected_response == response

    def test_close_restaurant(self):
        restaurant = Restaurant('Nihonjin', "Comida Japonesa", True)

        expected_response = 'Nihonjin agora está fechado!'

        response = restaurant.close_restaurant()

        assert expected_response == response

    def test_close_restaurant_already_closed(self):
        restaurant = Restaurant('Nihonjin', "Comida Japonesa", False)

        expected_response = 'Nihonjin já está fechado!'

        response = restaurant.close_restaurant()

        assert expected_response == response

    def test_set_number_served_success(self):
        restaurant = Restaurant('Joanne.s Trattoria', "Comida Italiana", True)

        expected_response = 10

        response = restaurant.set_number_served(10)

        assert expected_response == response

    def test_set_number_served_invalid_1(self):
        restaurant = Restaurant('Joanne.s Trattoria', "Comida Italiana", True)

        expected_response = "Entrada inválida"

        response = restaurant.set_number_served('A')

        assert expected_response == response

    def test_set_number_served_invalid_2(self): #nao sei pq esta quebrando...
        restaurant = Restaurant('Joanne.s Trattoria', "Comida Italiana", True)

        expected_response = "Entrada inválida"

        response = restaurant.set_number_served(True)

        assert expected_response == response

    def test_set_number_served_invalid_3(self):
        restaurant = Restaurant('Joanne.s Trattoria', "Comida Italiana", True)

        expected_response = "Entrada inválida"

        response = restaurant.set_number_served(None)

        assert expected_response == response

    def test_set_number_served_invalid_4(self):
        restaurant = Restaurant('Joanne.s Trattoria', "Comida Italiana", True)

        expected_response = "Entrada inválida"

        response = restaurant.set_number_served(' ')

        assert expected_response == response

    def test_set_number_served_invalid_5(self):
        restaurant = Restaurant('Joanne.s Trattoria', "Comida Italiana", True)

        expected_response = "Entrada inválida"

        response = restaurant.set_number_served(-1)

        assert expected_response == response

    def test_set_number_served_invalid_6(self):
        restaurant = Restaurant('Joanne.s Trattoria', "Comida Italiana", True)

        expected_response = "Entrada inválida"

        response = restaurant.set_number_served(0.2)

        assert expected_response == response

    def test_set_number_served_invalid_restaurant_closed(self):
        restaurant = Restaurant('Joanne.s Trattoria', "Comida Italiana", False)

        expected_response = "Joanne.s Trattoria está fechado!"

        response = restaurant.set_number_served('AAA')

        assert expected_response == response

    def test_set_number_served_restaurant_closed(self):

        restaurant = Restaurant('Joanne.s Trattoria', "Comida Italiana", False)

        expected_response = "Joanne.s Trattoria está fechado!"

        response = restaurant.set_number_served(10)

        assert expected_response == response

    def test_increment_number_served_success(self):

        restaurant = Restaurant('Joanne.s Trattoria', "Comida Italiana", True)

        expected_response = 20

        response = restaurant.increment_number_served(20)

        assert expected_response == response

    def test_multiples_increments_number_served_success(self):

        restaurant = Restaurant('Joanne.s Trattoria', "Comida Italiana", True)
        restaurant.increment_number_served(2)

        expected_response = 17

        response = restaurant.increment_number_served(15)

        assert expected_response == response

    def test_increment_number_served_restaurant_closed(self):

        restaurant = Restaurant('Joanne.s Trattoria', "Comida Italiana", False)

        expected_response = 'Joanne.s Trattoria está fechado!'

        response = restaurant.increment_number_served(20)

        assert expected_response == response

    def test_increment_number_served_restaurant_invalid_1(self):

        restaurant = Restaurant('Joanne.s Trattoria', "Comida Italiana", True)

        expected_response = "Entrada inválida"

        response = restaurant.increment_number_served('AA')

        assert expected_response == response

    def test_increment_number_served_restaurant_invalid_2(self):

        restaurant = Restaurant('Joanne.s Trattoria', "Comida Italiana", True)

        expected_response = "Entrada inválida"

        response = restaurant.increment_number_served(-1)

        assert expected_response == response

    def test_increment_number_served_restaurant_invalid_3(self):

        restaurant = Restaurant('Joanne.s Trattoria', "Comida Italiana", True)

        expected_response = "Entrada inválida"

        response = restaurant.increment_number_served(None)

        assert expected_response == response

    def test_increment_number_served_restaurant_invalid_4(self): #quebrando...

        restaurant = Restaurant('Joanne.s Trattoria', "Comida Italiana", True)

        expected_response = "Entrada inválida"

        response = restaurant.increment_number_served(False)

        assert expected_response == response

    def test_increment_number_served_restaurant_invalid_5(self):

        restaurant = Restaurant('Joanne.s Trattoria', "Comida Italiana", True)

        expected_response = "Entrada inválida"

        response = restaurant.increment_number_served(0.1)

        assert expected_response == response

    def test_increment_number_served_restaurant_invalid_6(self):

        restaurant = Restaurant('Joanne.s Trattoria', "Comida Italiana", False)

        expected_response = 'Joanne.s Trattoria está fechado!'

        response = restaurant.increment_number_served('AA')

        assert expected_response == response\
