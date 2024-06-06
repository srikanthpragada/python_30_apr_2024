from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

bs = BeautifulSoup(html_doc, 'html.parser')
print(bs.title.text)
links = bs.find_all('a')  # find all <a> elements 
print(links[0]['href'])
link3 = bs.find(id="link3")  # find element with id link3
print(link3)


