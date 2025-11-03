import json
com_url = "https://api.restful-api.dev/objects"


new_entry_payload = json.dumps({
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