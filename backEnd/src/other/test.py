import requests
import json, os
# import pycurl

# authentication = requests.post(r'http://127.0.0.1:5000/getToken')
# print(authentication.text)
# json_data = open('example.json', 'r').read()
# OrderSubmit = requests.post(r'http://127.0.0.1:5000/pushOrder', data=json_data)
# print(OrderSubmit.text)
# authentication = requests.get(r'http://192.168.20.118:8000/o/token/')

IP = '192.168.20.100:8000'
token = 'n9mPEVc0HBCH2Y3S3nxxgDQ8PR2FVQ'

# Productlist
authentication = requests.get(r'http://' + str(IP) + r'/Productlist/?access_token='+str(token))
print(r'Sucess http://' + str(IP) + r'/Productlist/?access_token='+str(token)+r'&format=json')

# Manufacturer endpoint
authentication = requests.get(r'http://' + str(IP) + r'/Manufacturer/?access_token='+str(token))
print(r'Sucess http://' + str(IP) + r'/Manufacturer/?access_token='+str(token)+r'&format=json')

# Address endpoint
authentication = requests.get(r'http://' + str(IP) + r'/Address/?access_token='+str(token))
print(r'Sucess http://' + str(IP) + r'/Address/?access_token='+str(token)+r'&format=json')