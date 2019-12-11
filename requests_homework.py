import requests
#build URL
path_url = 'http://api.postcodes.io/postcodes/'
arguments = 'e146gt'

post_codes = requests.get(path_url + arguments)
# turn this into a dictionary
dict_response = post_codes.json()
# print(dict_response)
#getting out data
print(dict_response.keys())
print(dict_response['status'])
print(dict_response['result'])
print(dict_response['result'].keys())
print(dict_response['result']['admin_district'])
print(dict_response['result']['longitude'])
print(dict_response['result']['latitude'])
print(dict_response['result']['nuts'])
print(dict_response['result']['admin_ward'])
def lat_return(self,path_url,arguments):
    p_cs = requests.get(path_url + arguments)
    dict_response = p_cs.json()
    return dict_response['result']['longitude']
def long_return(self,path_url,arguments):
    p_cs = requests.get(path_url + arguments)
    dict_response = p_cs.json()
    return dict_response['result']['latitude']
def search_post(path_url,arguments):
    search_pcs = requests.get(path_url + arguments)
    dict_response = search_pcs.json()
    file_create = open('postcode_text.txt','w+')
    file_create.write( f"{dict_response['result']['longitude']}"+' '+f"{dict_response['result']['latitude']}"+' '+
    f"{dict_response['result']['nuts']}"+' '+f"{dict_response['result']['admin_ward']}")
    file_create.close()
search_post('http://api.postcodes.io/postcodes/','e146gt')


# 5 - allows me to search a postcode and get the
# following data exported to a .txt file:
# - postcode
# - lat
# - long
# - nuts
# - admin_ward
