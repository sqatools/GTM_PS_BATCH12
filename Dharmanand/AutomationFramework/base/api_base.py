import logging
import requests


class APIBase:
    def __init__(self):
        self.log = logging.getLogger(__name__)

    def get_method(self, url, headers=None, payload=None):
        headers = headers if headers else {}
        payload = payload if payload else {}
        response = requests.request("GET", url, headers=headers, data=payload)
        logging.info(f"url: {url}")
        logging.info(f"headers: {headers}")
        logging.info(f"payload: {payload}")
        logging.info(f"status code: {response.status_code}")
        logging.info(f"response data: {response.json()}")
        return response.json(), response.status_code

    def post_method(self, url, headers=None, payload=None):
        headers = headers if headers else {}
        payload = payload if payload else {}
        response = requests.request("POST", url, headers=headers, data=payload)
        logging.info(f"url: {url}")
        logging.info(f"headers: {headers}")
        logging.info(f"payload: {payload}")
        logging.info(f"status code: {response.status_code}")
        logging.info(f"response data: {response.json()}")
        return response.json(), response.status_code

    def put_method(self, url, headers=None, payload=None):
        headers = headers if headers else {}
        payload = payload if payload else {}
        response = requests.request("PUT", url, headers=headers, data=payload)
        logging.info(f"url: {url}")
        logging.info(f"headers: {headers}")
        logging.info(f"payload: {payload}")
        logging.info(f"status code: {response.status_code}")
        logging.info(f"response data: {response.json()}")
        return response.json(), response.status_code

    def patch_method(self, url, headers=None, payload=None):
        headers = headers if headers else {}
        payload = payload if payload else {}
        response = requests.request("PATCH", url, headers=headers, data=payload)
        logging.info(f"url: {url}")
        logging.info(f"headers: {headers}")
        logging.info(f"payload: {payload}")
        logging.info(f"status code: {response.status_code}")
        logging.info(f"response data: {response.json()}")
        return response.json(), response.status_code

    def delete_method(self, url, headers=None, payload=None):
        headers = headers if headers else {}
        payload = payload if payload else {}
        response = requests.request("GET", url, headers=headers, data=payload)
        logging.info(f"url: {url}")
        logging.info(f"headers: {headers}")
        logging.info(f"payload: {payload}")
        logging.info(f"status code: {response.status_code}")
        logging.info(f"response data: {response.json()}")
        return response.json(), response.status_code
