import requests


r = requests.get('https://api.kanye.rest')
text = r.text # same as converting to stringify in js 
jsonText = r.json()
print(type(text))
print(jsonText['quote'])
