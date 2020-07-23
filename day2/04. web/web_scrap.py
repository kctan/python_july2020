#https://www.fortytwo.sg/dining/dining-tables/landon-regular-dining-table-coffee.html

import bs4
import requests

requestObj = requests.get("https://www.fortytwo.sg/dining/dining-tables/landon-regular-dining-table-coffee.html")
requestObj.raise_for_status()
soup = bs4.BeautifulSoup(requestObj.text, 'html.parser')

elements = soup.select("#product-price-46728") # $69.90 
print("Current Price: " + elements[0].text)

elements = soup.select("#old-price-46728")  #  $129.90
print("\nOld Price: " + elements[0].text)

