import requests
import json


api_iss_now = 'http://api.open-notify.org/iss-now.json'
api_iss_pass = 'http://api.open-notify.org/iss-pass.json?lat=43.0388889&lon=-87.9063889'
api_iss_astros = 'http://api.open-notify.org/astros.json'
# response = requests.get(api_iss_now )  
# # response = requests.get(api_iss_pass)
# # response = requests.get(api_iss_astros)
# print(response.json())

def print_response(request_url):
    response = requests.get(request_url)
    print(response.json())

def parse_response(request_url):
    response = requests.get(request_url)
    response_json = response.json()
    for x in response_json:
        print(x + ': ' + str(response_json.get(x) ))

print_response(api_iss_now) 
parse_response(api_iss_now)





