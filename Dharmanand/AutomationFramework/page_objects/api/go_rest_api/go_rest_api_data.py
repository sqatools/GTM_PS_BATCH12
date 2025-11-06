import json
url = "https://gorest.co.in"

users_api_url = f"{url}/public/v2/users/172964"
user_payload = json.dumps({
  "name": "rakesh jain",
  "gender": "male",
  "email": "rakesh.jain@15ce.com",
  "status": "active"
})
user_headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer 448dac141381bfeb9dd874eb05609057dc07dab5effabe9716fa48423a3cdeae'
}
