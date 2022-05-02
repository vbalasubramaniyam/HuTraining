from Main_API_Assignment.Utility import Util


def test_token(getData):
  endpoint="login"

  payload = {
      "email": getData["email"],
      "password": getData["Password"],
  }
  token=Util.post(endpoint,payload,headers=None,expectedstatuscode=200)
  logoutendpoint="logout"
  originalToken=token["token"]
  token1='Bearer '+originalToken
  return token1
