'''
Dennis Smith

Vacation Rental API ("test_index")

This File houses the unit tests used on the Vacation Rental API Program.
'''
import unittest
import json
import requests

class TestRentalAPI(unittest.TestCase):
	'''
	Test class for The Rental API
	'''

	BASE_URL = 'http://localhost:5000/'

	def test_get_rentals(self):
		'''
		Method -- test_get_rentals
			Tests the API's ability to return all existing rentals
		'''
		response = requests.get(f'{self.BASE_URL}/rentals')
		self.assertEqual(response.status_code, 200)
		self.assertTrue(isinstance(response.json(), list))
		# Always start with 5 homes
		self.assertEqual(len(response.json()), 5)


	def test_rent_existing_home(self):
		'''
		Method -- test_rent_existing_home
			Tests a request to rent an existing vacation home that has availability.
		'''
		rental_request = {
			'home_id': 1,
	        'start_date': '2024-07-01',
	        'end_date': '2024-07-06'
		}
		response = requests.post(f'{self.BASE_URL}/rent', json=rental_request)
		self.assertEqual(response.status_code, 200)
		self.assertIn('Reservation success!', response.json()['message'])

	def test_rent_invalid_home(self):
		'''
		Method -- test_rent_invalid_home
			Tests a request to rent a vacation home that does not exist in the API.
		'''
		fake_request = {
			'home_id': 25,
	        'start_date': '2024-07-01',
	        'end_date': '2024-07-06'
		}
		response = requests.post(f'{self.BASE_URL}/rent', json=fake_request)
		self.assertEqual(response.status_code, 404)
		self.assertIn('Rental home not found, please try another ID', response.json()['error'])


	def test_rent_home_overlap(self):
		'''
		Method -- test_rent_home_overlap
			Tests a request to rent an existing vacation home that has already been rented out. The
			dates between both requests will overlap.
		'''
		# making initial request
		rental_request = {
			'home_id': 1,
	        'start_date': '2024-08-01',
	        'end_date': '2024-08-10'
		}
		response = requests.post(f'{self.BASE_URL}/rent', json=rental_request)

		# making request with overlapping dates
		overlapping = {
			'home_id': 1,
	        'start_date': '2024-08-03',
	        'end_date': '2024-08-12'
		}

		response = requests.post(f'{self.BASE_URL}/rent', json=overlapping)
		self.assertEqual(response.status_code, 400)
		self.assertIn('Rental is already booked for this time period, please try again', response.json()['error'])

	def test_one_day_rental(self):
		'''
		Method -- test_one_day_rental
			Tests a request to rent an existing vacation home with an identical start and end date.
		'''
		rental_request = {
			'home_id': 1,
	        'start_date': '2024-07-01',
	        'end_date': '2024-07-01'
		}
		response = requests.post(f'{self.BASE_URL}/rent', json=rental_request)
		self.assertEqual(response.status_code, 400)
		self.assertIn('Invalid Date Selection. Please make your end date at least one day after your start date.', response.json()['error'])

	def test_res_start_after_end(self):
		'''
		Method -- test_res_start_after_end
			Tests a request to rent an existing vacation home with a reservation start date that is after the end date.
		'''
		rental_request = {
			'home_id': 1,
	        'start_date': '2024-07-10',
	        'end_date': '2024-07-06'
		}
		response = requests.post(f'{self.BASE_URL}/rent', json=rental_request)
		self.assertEqual(response.status_code, 400)
		self.assertIn('Invalid Date Selection. Please ensure that the start date of your reservation occurs before the end date.', response.json()['error'])

	def test_bad_date_input(self):
		'''
		Method -- test_bad_date_input
			Tests a request where the input format for the date is incorrect.
		'''
		bad_date = {
			'home_id': 1,
	        'start_date': '2024/07/01',
	        'end_date': '2024-07-06'
		}
		response = requests.post(f'{self.BASE_URL}/rent', json=bad_date)
		self.assertEqual(response.status_code, 400)
		self.assertIn('Invalid Date Format. Please use YY-MM-DD', response.json()['error'])

if __name__ == "__main__":
	unittest.main()