import requests, json, os

IP = '127.0.0.1:8000'
token = 'Xfy5Nef1e6xfM97UYLwqllJUYDnUcD'
item = 't14001'

# # Token endpoint
authentication = requests.post(r'http://127.0.0.1:8000/o/token/?grant_type=password&username=Mike&password=tas}Ng2uQ7?!rSS9&client_id=1VICqpEgPG2D5UB5TSd0UoiMmzuKhvy8ejO9k1hi&client_secret=zFcO5hjIUw44hzNEh1M6lOScNtBmHr3KC6CTeITxqPEd69IZOn5FmwadvVEBKixbeauFgi22geuEvj1uQqAwYWx3buywTs1XW3kuNLMLYPuPFn63AWGtRgIzX3nzlyfM')
if not 'error' in authentication.text:
    print('Success Token endpoint')
else:
    print(authentication.text)

# # Address endpoint
authentication = requests.get(r'http://'+str(IP)+r'/Address/?access_token='+str(token))
if not 'address1' in authentication.text:
    print(authentication.text)
else:
    print('Success Address endpoint')

# # Manufacturer endpoint
authentication = requests.get(r'http://'+str(IP)+r'/Manufacturer/?access_token='+str(token))
if not 'manufacturerCode' in authentication.text:
    print('authentication.text')
else:
    print('Success Manufacturer endpoint')

# Productlist endpoint
authentication = requests.get(r'http://'+str(IP)+r'/Productlist/?access_token='+str(token)+'&itemno='+str(item))
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