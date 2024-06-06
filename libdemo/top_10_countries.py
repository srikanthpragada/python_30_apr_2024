import requests 

try:
    resp = requests.get("https://restcountries.com/v3.1/all")
    if resp.status_code != 200:
        print("Sorry! Could not get details of countries!")
        exit()
except:
     print("Sorry! Could not get details of countries!")
     exit()

countries = resp.json() 

sorted_coutries = sorted(countries,
                      key = lambda c: c['population'], reverse=True)
for country in sorted_coutries[:10]:
    name = country['name']['common']
    population = country['population']
    if 'capital' in country:
        capital = country['capital'][0]
    else:
        capital = 'None'
    region = country['region']
    print(f"{region:15} {name:30} {capital:15}  {population:15}")
