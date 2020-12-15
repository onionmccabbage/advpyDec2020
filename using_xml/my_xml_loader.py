# pip install lxml
from lxml import etree as et
books_element_tree = et.parse('books.xml')

books_element = books_element_tree.getroot()

list_of_titles = books_element.findall('book/title') # XPATH expression
for title_element in list_of_titles:
    print ("Title: ", title_element.text)

list_of_prices = books_element.findall('book/cost')
for price_element in list_of_prices:
    print("Price: ", price_element.text)

# create a dict of prices
price_dict = dict(zip([e.text for e in list_of_titles],
                      [float(e.text) for e in list_of_prices]))

print('Price dict:', price_dict)

# the prices are text, so:
list_of_prices = [ float(price) for price in [e.text for e in list_of_prices]]
print('Max price:', max(list_of_prices))

