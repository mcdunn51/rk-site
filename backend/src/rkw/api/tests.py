import requests, json, os

token = ''
item = 't14001'

testing_mode = False

if testing_mode:
    IP = '127.0.0.1:8000'  
    authentication = requests.post(r'http://'+str(IP)+r'/o/token/?grant_type=password&username=Mike&password=tas}Ng2uQ7?!rSS9&client_id=1VICqpEgPG2D5UB5TSd0UoiMmzuKhvy8ejO9k1hi&client_secret=zFcO5hjIUw44hzNEh1M6lOScNtBmHr3KC6CTeITxqPEd69IZOn5FmwadvVEBKixbeauFgi22geuEvj1uQqAwYWx3buywTs1XW3kuNLMLYPuPFn63AWGtRgIzX3nzlyfM')
else:
    IP = '100.1.253.16:8000'
    authentication = requests.post(r'http://'+str(IP)+r'/o/token/?grant_type=password&username=Mike&password=tas}Ng2uQ7?!rSS9&client_id=3USdTjmnjbcdTeNrdwjeaOlEcVg1n7oFmXHPz2q9&client_secret=QuZg0JK62clUelPFMJs1884zx1g1ZeFPcgPN74W58Z3ZKUrWrUFAaMwoxJ8sdLei5CvTUIvCErNcmIQk4hoRA5w5A3GC1u9Sbe4ctqWrV67SX12mZ8Rxp2hFwVhFXF5M')

# Token endpoint
if not 'error' in authentication.text:
    print('Success Token endpoint')
    token = json.loads(authentication.text)["access_token"]
else:
    print(authentication.text)

# OProductlist endpoint
authentication = requests.get(r'http://'+str(IP)+r'/OProductlist/?access_token='+str(token)+'&itemno='+str(item))
if not 'itemno' in authentication.text:
    print(authentication.text)
else:
    print('Success OProductlist endpoint')

# OProdDetailed endpoint
authentication = requests.get(r'http://'+str(IP)+r'/OProdDetailed/?access_token='+str(token)+'&itemno='+str(item))
if not 'itemno' in authentication.text:
    print(authentication.text)
else:
    print('Success OProdDetailed endpoint')

# # OAddressList endpoint
authentication = requests.get(r'http://'+str(IP)+r'/OAddressList/?access_token='+str(token))
if not 'address1' in authentication.text:
    print(authentication.text)
else:
    print('Success OAddressList endpoint')

# # OOrderHeader endpoint
authentication = requests.get(r'http://'+str(IP)+r'/OOrderHeader/?access_token='+str(token))
if not 'id' in authentication.text:
    print(authentication.text)
else:
    print('Success OOrderHeader endpoint')

# # OOrderLines endpoint
authentication = requests.get(r'http://'+str(IP)+r'/OOrderLines/?access_token='+str(token))
if not 'id' in authentication.text:
    print(authentication.text)
else:
    print('Success OOrderLines endpoint')

# Productlist endpoint
authentication = requests.get(r'http://'+str(IP)+r'/Productlist/?access_token='+'&itemno='+str(item))
if not 'itemno' in authentication.text:
    print(authentication.text)
else:
    print('Success Productlist endpoint')

# ProductDetailed endpoint
authentication = requests.get(r'http://'+str(IP)+r'/ProductDetailed/?access_token='+str(token)+'&itemno='+str(item))
if not 'itemno' in authentication.text:
    print(authentication.text)
else:
    print('Success Productlist endpoint')

# # Manufacturer endpoint
authentication = requests.get(r'http://'+str(IP)+r'/Manufacturer/?access_token=')
if not 'manufacturerCode' in authentication.text:
    print('authentication.text')
else:
    print('Success Manufacturer endpoint')