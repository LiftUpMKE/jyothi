import requests
import json


api_iss_now = 'http://api.open-notify.org/iss-now.json'
api_iss_pass = 'http://api.open-notify.org/iss-pass.json?lat=43.0388889&lon=-87.9063889'
api_iss_astros = 'http://api.open-notify.org/astros.json'

def print_response(request_url):
    response = requests.get(request_url)
    print(response.json())

def parse_response(request_url):
    response = requests.get(request_url)
    response_json = response.json()
    for x in response_json:
        print(x + ': ' + str(response_json.get(x) ))

x = input('''1. ISS Current Location
2. ISS Pass Time for Milwaukee
3. People in Space
              
Select an Option (1/2/3):  ''')

if x == '1':
    print_response(api_iss_now)
elif x == '2':
    print_response(api_iss_pass)
elif x == '3':
    print_response(api_iss_astros)
else:
    print('Please Select a Valid Option')    

        
