from unittest import TestCase
import requests

baseURL = "https://api.exchangeratesapi.io"


class ExchangeRate(TestCase):

    # Verify that the response body of valid GET request is not empty and has a correct structure
    def test_valid_get(self):
        response = requests.get(baseURL + '/2010-01-12')
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.json())
        self.assertEqual("EUR", response.json()["base"])
        self.assertIsNotNone(response.json()["rates"])
        self.assertEqual("2010-01-12", response.json()["date"])

    # Verify that the corresponding response body with error is returned with invalid GET request
    def test_invalid_get(self):
        response = requests.get(baseURL + '/notExpected')
        self.assertEqual(400, response.status_code)
        self.assertDictEqual({"error": "time data 'notExpected' does not match format '%Y-%m-%d'"}, response.json())

    # Verify that corresponding error message is returned when invalid date is given (leap years also can be verified)
    def test_get_invalid_date(self):
        response = requests.get(baseURL + '/2010-02-30')
        self.assertEqual(400, response.status_code)
        self.assertDictEqual({"error": "day is out of range for month"}, response.json())

    # Verify that response has Content-Type and it is application/json
    def test_get_content_type(self):
        response = requests.get(baseURL + '/2010-01-12')
        self.assertIn('Content-Type', response.headers)
        self.assertEqual("application/json", response.headers["Content-Type"])
