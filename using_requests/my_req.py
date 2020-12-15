# we need the requests library
# pip install requests
# in my case
# pip install --target=D:\advpy\libs requests --ignore-installed
# (thanks Igor!!)

import requests
url = 'https://jsonplaceholder.typicode.com'
param = 'users' # users, posts, albums, todos, photos
id = 3 # 1-9 to be safe
user_param = ''
user_id = -99
# ask use for param
while user_param not in ('users', 'posts', 'albums', 'todos', 'photos'):
    user_param = input('which parameter? ')
# also we ask for an integer between 1-9 inclusive
while not 1 <= user_id <=9:
    user_id = int(float( input('which id (1-9)? ') ))

new_url = f'{url}/{user_param}/{user_id}'
print(new_url)

# make a request to the end-point API
res = requests.get(new_url) # this may take a moment

# explore the response object
print(res) # this contains EVERYTHING in the resonse
# including status_code, original url, any headers, your fingerprint


# convert the retrieved JSON into a Python structure
j = res.json() # this will convert the json part of the response into Python

print(j['name']) # access the name within the structure
print(j['company']['name'])
print(j['address']['geo']['lat'])

