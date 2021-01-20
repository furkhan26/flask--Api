import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "ProcessPayment/",{"CreditCardNumber":1234,"CardHolder":"michale","ExpirationDate":"2020-01-20","Amount": 23444})
print(response.json())

# response = requests.get(BASE + "ProcessPayment/4")
# print(response.json())