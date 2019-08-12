from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from address.models import Address, State, City


class UnitTestCase(APITestCase):
    def setUp(self):
        self.state_name = 'test_state'
        self.city = 'test_city'
        self.company_name = 'test_comapny'
        self.building_number = '123'
        self.postal_code = '456'
        self.locality = 'test_locality'

    def test_get_address(self):
        address_url = reverse('addresses-list')
        response = self.client.get(address_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_address(self):
        state_url = reverse('state-list')
        state_data = {'name': self.state_name}
        state_response = self.client.post(state_url, state_data, format='json')

        # Check if State creation works
        self.assertEqual(state_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(State.objects.count(), 1)
        self.assertEqual(State.objects.get().name, self.state_name)

        city_url = reverse('city-list')
        city_data = {
            "name": self.city,
            "state": State.objects.get().id
        }
        response = self.client.post(city_url, city_data, format='json')

        # Check if City creation works
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(City.objects.count(), 1)
        self.assertEqual(City.objects.get().name, self.city)

        address_url = reverse('addresses-list')
        address_data = {
            "company_name": self.company_name,
            "building_number": self.building_number,
            "postal_code": self.postal_code,
            "locality": {
                "name": self.locality,
                "city": City.objects.get().id,
                "state": State.objects.get().id
                }
            }
        response = self.client.post(address_url, address_data, format='json')

        # Check if Address creation works
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Address.objects.count(), 1)
        self.assertEqual(Address.objects.get().company_name, self.company_name)