import requests
from bs4 import BeautifulSoup
# ex :1 
"""
response = requests.get("https://quotes.toscrape.com")
soup = BeautifulSoup(response.text, "html.parser")
name = soup.find("h2").text
price = soup.find("p").text

import pandas as pd

df = pd.DataFrame({
    "Product": [name],
    "Price": [price]
})
df.to_csv("products.csv", index=False)"""

#ex:2 

"""url = "https://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

title = soup.find("title").text
print(title)
quotes = soup.find_all("span", class_="text")

for quote in quotes:
    print(quote.text)
"""    

#ex:3 
'''
html = """
<div class="product">
    <h2>Laptop</h2>
    <span class="price">50000</span>
</div>
"""

soup = BeautifulSoup(html, "html.parser")

product = soup.find("h2").text
price = soup.find("span", class_="price").text

print("Product:", product)
print("Price:", price)
'''
import requests
from bs4 import BeautifulSoup

"""url = "https://quotes.toscrape.com"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all("div", class_="quote")

for quote in quotes:

    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text

    print(text)
    print(author)
    print("-" * 40)
    """
    
"""import requests

response = requests.get("https://quotes.toscrape.com")
print(response.status_code)
"""

import  requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"

respose = requests.get(url)
soup = BeautifulSoup(respose.text, "html.parser")

qutoes = soup.find_all("span",class_="text")

for i in qutoes:
    print(i.text)