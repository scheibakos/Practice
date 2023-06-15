import requests

url = "https://reqres.in/api/users"
data = {"name": "Ádám", "job": "Being awesome"}
username = "admin"
password = "admin"

session = requests.Session()
session.auth = (username, password)

@allure.id("TC-01")
@allure.title("API Authentication testing")
def test_api_auth():
    respone = session.post(url, json=data)
    assert respone.status_code == 201
    response_data = respone.json()
    print(response_data)
    assert response_data["name"] == data["name"]
    assert response_data["job"] == data["job"]
