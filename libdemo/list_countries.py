import requests


resp = requests.get("https://restcountries.com/v3.1/all")
if resp.status_code != 200:
    print("Sorry! Could not get details of countries!")
    exit()


countries = resp.json()

for country in countries:
    name = country['name']['common']
    if 'capital' in country:
        capital = country['capital'][0]
    else:
        capital = 'None'
    region = country['region']
    print(f"{region:15} {name:50} {capital:20}")
