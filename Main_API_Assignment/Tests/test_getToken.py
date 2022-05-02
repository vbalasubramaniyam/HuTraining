from Main_API_Assignment.Pages import User


def test_token(getData):
  endpoint="login"

  payload = {
      "email": getData["email"],
      "password": getData["Password"],
  }
  token= User.post(endpoint, payload, headers=None, expectedstatuscode=200)
  logoutendpoint="logout"
  originalToken=token["token"]
  token1='Bearer '+originalToken
  return token1
