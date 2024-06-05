import requests

user = input("Enter github id :")

resp = requests.get(f"https://api.github.com/users/{user}")

if resp.status_code != 200:
    print("Sorry! Could not get details!")
    exit()

details = resp.json()  # Covert JSON to dict 

print(f"Name     : {details['name']}")
print(f"Company  : {details['company']}")
print(f"Location : {details['location']}")