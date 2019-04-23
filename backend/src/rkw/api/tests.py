import requests, json, os, socket

token = ''
item = 't14001'

# Testing Mode
if socket.gethostname() == 's1.intranet.svg.local':
    test_mode = False
else:
    test_mode = True

if test_mode:
    IP = '127.0.0.1:8000'  
    authentication = requests.post(r'http://'+str(IP)+r'/o/token/?grant_type=password&username=M&password=0&client_id=CpV612uZEllAr8vh7bFGVB9Uiq6DagTrhCUu3l4W&client_secret=jJVNuUlYkGSsbbdSQ7DvrAtuiR2T9OO9eY2kVQIJDoNRZ69pHjSkk2KSVJtnXNyGmDAh2PHF0qogfc1GpdXvnqj7ID1rdwVvgjbuNdDkXup3Ewt1mKaDYZR37jTQ6cvr')
else:
    IP = '100.1.253.16:8000'
    authentication = requests.post(r'http://'+str(IP)+r'/o/token/?grant_type=password&username=Mike&password=tas}Ng2uQ7?!rSS9&client_id=3USdTjmnjbcdTeNrdwjeaOlEcVg1n7oFmXHPz2q9&client_secret=QuZg0JK62clUelPFMJs1884zx1g1ZeFPcgPN74W58Z3ZKUrWrUFAaMwoxJ8sdLei5CvTUIvCErNcmIQk4hoRA5w5A3GC1u9Sbe4ctqWrV67SX12mZ8Rxp2hFwVhFXF5M')

# Token endpoint
def Token():
    if not 'error' in authentication.text:
        print('Success Token endpoint')
        token = json.loads(authentication.text)["access_token"]
        return token
    else:
        print(authentication.text)

# OCustomer endpoint
def OCustomer(IP, token, item):
    authentication = requests.get(r'http://'+str(IP)+r'/OCustomer/?access_token='+str(token)+'&itemno='+str(item))
    if not 'username' in authentication.text:
        print('Failed OCustomer endpoint')
    else:
        print('Success OCustomer endpoint')

# OProductlist endpoint
def OProductlist(IP, token, item):
    authentication = requests.get(r'http://'+str(IP)+r'/OProductlist/?access_token='+str(token)+'&itemno='+str(item))
    if not 'itemno' in authentication.text:
        print('Failed OProductlist endpoint')
    else:
        print('Success OProductlist endpoint')

# OProdDetailed endpoint
def OProdDetailed(IP, token, item):
    authentication = requests.get(r'http://'+str(IP)+r'/OProdDetailed/?access_token='+str(token)+'&itemno='+str(item))
    if not 'itemno' in authentication.text:
        print('Failed OProdDetailed endpoint')
    else:
        print('Success OProdDetailed endpoint')

# OAddressList endpoint
def OAddressList(IP, token, item):
    authentication = requests.get(r'http://'+str(IP)+r'/OAddressList/?access_token='+str(token))
    if not 'address1' in authentication.text:
        print('Failed OAddressList endpoint')
    else:
        print('Success OAddressList endpoint')

# OOrderHeader endpoint
def OOrderHeader(IP, token, item):
    authentication = requests.get(r'http://'+str(IP)+r'/OOrderHeader/?access_token='+str(token))
    if not 'customerCode' in authentication.text:
        print('Failed OOrderHeader endpoint')
    else:
        print('Success OOrderHeader endpoint')

# OOrderLines endpoint
def OOrderLines(IP, token, item):
    authentication = requests.get(r'http://'+str(IP)+r'/OOrderLines/?access_token='+str(token))
    if not 'itemno' in authentication.text:
        print('Failed OOrderLines endpoint')
    else:
        print('Success OOrderLines endpoint')

# OSearch endpoint
def OSearch(IP, token, item):
    authentication = requests.get(r'http://'+str(IP)+r'/OSearch/?access_token='+str(token)+r'&search='+str(item))
    if not 'itemno' in authentication.text:
        print('Failed OSearch endpoint')
    else:
        print('Success OSearch endpoint')

# Productlist endpoint
def Productlist(IP, item):
    authentication = requests.get(r'http://'+str(IP)+r'/Productlist/?access_token='+'&itemno='+str(item))
    if not 'itemno' in authentication.text:
        print('Failed Productlist endpoint')
    else:
        print('Success Productlist endpoint')

# ProductDetailed endpoint
def ProductDetailed(IP, item):
    authentication = requests.get(r'http://'+str(IP)+r'/ProductDetailed/?access_token='+str(token)+'&itemno='+str(item))
    if not 'itemno' in authentication.text:
        print('Failed ProductDetailed endpoint')
    else:
        print('Success ProductDetailed endpoint')

# Manufacturer endpoint
def manufacturerCode(IP, item):
    authentication = requests.get(r'http://'+str(IP)+r'/Manufacturer/')
    if not 'manufacturerCode' in authentication.text:
        print('Failed Manufacturer endpoint')
    else:
        print('Success Manufacturer endpoint')

# Manufacturer endpoint
def IPG(IP, item):
    authentication = requests.get(r'http://'+str(IP)+r'/IPG/')
    if not 'IPG' in authentication.text:
        print('Failed IPG endpoint')
    else:
        print('Success IPG endpoint')

# Search endpoint
def Search(IP, item):
    authentication = requests.get(r'http://'+str(IP)+r'/Search/?search='+str(item))
    if not 'itemno' in authentication.text:
        print('Failed Search endpoint')
    else:
        print('Success Search endpoint')

token = Token()
OCustomer(IP, token, item)
OProductlist(IP, token, item)
OProdDetailed(IP, token, item)
OAddressList(IP, token, item)
OOrderHeader(IP, token, item)
OOrderLines(IP, token, item)
OSearch(IP, token, item)
Productlist(IP, item)
ProductDetailed(IP, item)
manufacturerCode(IP, item)
IPG(IP, item)
Search(IP, item)