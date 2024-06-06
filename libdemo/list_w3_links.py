from bs4 import BeautifulSoup
import requests

WEBSITE = "https://www.w3schools.com"

resp = requests.get(WEBSITE)
contents = resp.text 

bs = BeautifulSoup(contents, "html.parser")

links = bs.find_all("a")
urls = []
for link in links:
    href = link['href']
    if href.startswith("javascript:void(0)"):
        continue 

    if not href.startswith("http"):
        href = WEBSITE + href 

    if href not in urls:
        urls.append(href)


for link in urls:
    print(link)    

print(f"Count = {len(urls)}")
