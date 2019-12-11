import requests
#build URL
path_url = 'http://api.postcodes.io/postcodes/'
arguments = 'e146gt'

post_codes = requests.get(path_url + arguments)
print(post_codes)
print(type(post_codes))
# turn this into a dictionary
dict_response = post_codes.json()
# print(dict_response)
#getting out data
print(dict_response.keys())
print(dict_response['status'])
print(dict_response['result'].keys())
print(dict_response['result']['admin_district'])
