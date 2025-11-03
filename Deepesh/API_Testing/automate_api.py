# pip install requests
import requests
import json
from pprint import pprint


def get_all_entries():
    url = "https://api.restful-api.dev/objects"
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.status_code)
    print(response.json())

#get_all_entries()


def get_specific_entries():
    url = "https://api.restful-api.dev/objects?id=3&id=5&id=10"
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.status_code)
    pprint(response.json())

#get_specific_entries()


def get_one_specific_entry():
    url = "https://api.restful-api.dev/objects/7"
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.status_code)
    pprint(response.json())

#get_one_specific_entry()

def create_new_entry():
    url = "https://api.restful-api.dev/objects"

    payload = json.dumps({
        "name": "Apple MacBook Pro 25",
        "data": {
            "year": 2025,
            "price": 2000.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "4 TB"
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print("status code :", response.status_code)
    pprint(response.json())

create_new_entry()