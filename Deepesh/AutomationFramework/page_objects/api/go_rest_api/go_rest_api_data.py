import json
url = "https://gorest.co.in"

users_api_url = f"{url}/public/v2/users"
user_payload = json.dumps({
  "name": "Tenali Aajin",
  "gender": "male",
  "email": "tenali1234.ramakrishna@15ce.com",
  "status": "active"
})
user_headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer 69f09b0dab07d7de6a65af964a89b08e088ac9a5aef42a1c3208095d8dab767f'
}
