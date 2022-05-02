import requests
import json

url = "https://api-nodejs-todolist.herokuapp.com/user/register"

payload = json.dumps({
  "name": "Muhammad Nur Ali",
  "email": "muh.nurali4345@gmail.com",
  "password": "12345678",
  "age": 20
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.post(url, data=payload, headers=headers)

print(response.text)