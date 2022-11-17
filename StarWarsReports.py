import requests
import json

def printPeople():
    return ''

response_API = requests.get('https://swapi.dev/api/people/1/')

print(response_API.status_code)

data = response_API.text
parse_json = json.loads(data)

name = parse_json['name']
gender = parse_json['gender']
starships = parse_json['starships']