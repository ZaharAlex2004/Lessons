import unittest

import requests
from unittest.mock import *
from requests.models import Response


class WebService:
    def get_data(self, url: str) -> dict:
        """
        Применение данных.
        :param url:
        :return:
        """
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err} for url:{url}"}
        except Exception as err:
            return {"error": f"Other error occurred: {err}"}


#ws = WebService()
#print(ws.get_data("https://gortransport.kharkov.ua"))


class TestWebService(unittest.TestCase):
    @patch('requests.get')
    def test_get_data_success(self, mock_get):
        """
        Определение успешного запроса.
        :param mock_get:
        :return:
        """
        mock_response = Response()
        mock_response.status_code = 200
        mock_response._content = b'{"data": "test"}'
        mock_get.return_value = mock_response

        service = WebService()
        result = service.get_data("https://gortransport.kharkov.ua")

        self.assertEqual(result, {"data": "test"})
        mock_get.assert_called_once_with("https://gortransport.kharkov.ua")

    @patch('requests.get')
    def test_get_data_http_error(self, mock_get):
        """
        Выявление ошибок с кодом 404.
        :param mock_get:
        :return:
        """
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response._content = b'{"error": "Not Found"}'
        mock_get.return_value = mock_response
        mock_get.side_effect = requests.exceptions.HTTPError("404 Client Error: Not Found")

        service = WebService()
        result = service.get_data("https://reqres.in/api/users/99999")

        expected = {
            "error": "HTTP error occurred: 404 Client Error: Not Found for url:https://reqres.in/api/users/99999"}
        self.assertEqual(result, expected)

    @patch('requests.get')
    def test_get_data_other_error(self, mock_get):
        """
        Иммитация других проблем.
        :param mock_get:
        :return:
        """
        mock_get.side_effect = Exception("Network error")

        service = WebService()
        result = service.get_data("https://gortransport.kharkov.ua/subway/stations/31/")

        self.assertEqual(result, {"error": "Other error occurred: Network error"})
        mock_get.assert_called_once_with("https://gortransport.kharkov.ua/subway/stations/31/")


if __name__ == '__main__':
    unittest.main()
