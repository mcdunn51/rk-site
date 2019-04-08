import requests, json, os

token = ''
item = 't14001'

# Testing Mode
if socket.gethostname() == 's1.intranet.svg.local':
    test_mode = False
else:
    test_mode = True

if testing_mode:
    IP = '127.0.0.1:8000'  
    authentication = requests.post(r'http://'+str(IP)+r'/o/token/?grant_type=password&username=M&password=0&client_id=CpV612uZEllAr8vh7bFGVB9Uiq6DagTrhCUu3l4W&client_secret=jJVNuUlYkGSsbbdSQ7DvrAtuiR2T9OO9eY2kVQIJDoNRZ69pHjSkk2KSVJtnXNyGmDAh2PHF0qogfc1GpdXvnqj7ID1rdwVvgjbuNdDkXup3Ewt1mKaDYZR37jTQ6cvr')
else:
    IP = '100.1.253.16:8000'
    authentication = requests.post(r'http://'+str(IP)+r'/o/token/?grant_type=password&username=Mike&password=tas}Ng2uQ7?!rSS9&client_id=3USdTjmnjbcdTeNrdwjeaOlEcVg1n7oFmXHPz2q9&client_secret=QuZg0JK62clUelPFMJs1884zx1g1ZeFPcgPN74W58Z3ZKUrWrUFAaMwoxJ8sdLei5CvTUIvCErNcmIQk4hoRA5w5A3GC1u9Sbe4ctqWrV67SX12mZ8Rxp2hFwVhFXF5M')

# Token endpoint
if not 'error' in authentication.text:
    print('Success Token endpoint')
    token = json.loads(authentication.text)["access_token"]
else:
    print(authentication.text)

# OCustomerID endpoint
authentication = requests.get(r'http://'+str(IP)+r'/OCustomerID/?access_token='+str(token)+'&itemno='+str(item))
if not 'username' in authentication.text:
    print('Failed OCustomerID endpoint')
else:
    print('Success OCustomerID endpoint')

# OProductlist endpoint
authentication = requests.get(r'http://'+str(IP)+r'/OProductlist/?access_token='+str(token)+'&itemno='+str(item))
if not 'itemno' in authentication.text:
    print('Failed OProductlist endpoint')
else:
    print('Success OProductlist endpoint')

# OProdDetailed endpoint
authentication = requests.get(r'http://'+str(IP)+r'/OProdDetailed/?access_token='+str(token)+'&itemno='+str(item))
if not 'itemno' in authentication.text:
    print('Failed OProdDetailed endpoint')
else:
    print('Success OProdDetailed endpoint')

# # OAddressList endpoint
authentication = requests.get(r'http://'+str(IP)+r'/OAddressList/?access_token='+str(token))
if not 'address1' in authentication.text:
    print('Failed OAddressList endpoint')
else:
    print('Success OAddressList endpoint')

# # OOrderHeader endpoint
authentication = requests.get(r'http://'+str(IP)+r'/OOrderHeader/?access_token='+str(token))
if not 'customerID' in authentication.text:
    print('Failed OOrderHeader endpoint')
else:
    print('Success OOrderHeader endpoint')

# # OOrderLines endpoint
authentication = requests.get(r'http://'+str(IP)+r'/OOrderLines/?access_token='+str(token))
if not 'itemID' in authentication.text:
    print('Failed OOrderLines endpoint')
else:
    print('Success OOrderLines endpoint')

# Productlist endpoint
authentication = requests.get(r'http://'+str(IP)+r'/Productlist/?access_token='+'&itemno='+str(item))
if not 'itemno' in authentication.text:
    print('Failed Productlist endpoint')
else:
    print('Success Productlist endpoint')

# ProductDetailed endpoint
authentication = requests.get(r'http://'+str(IP)+r'/ProductDetailed/?access_token='+str(token)+'&itemno='+str(item))
if not 'itemno' in authentication.text:
    print('Failed Productlist endpoint')
else:
    print('Success Productlist endpoint')

# # Manufacturer endpoint
authentication = requests.get(r'http://'+str(IP)+r'/Manufacturer/?access_token=')
if not 'manufacturerCode' in authentication.text:
    print('Failed Manufacturer endpoint')
else:
    print('Success Manufacturer endpoint')