# curl 'http://192.168.86.42/driver/ajax/update' \
#   -H 'Accept: application/json, text/javascript, */*; q=0.01' \
#   -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
#   -H 'Accept-Language: en-US,en;q=0.9' \
#   --data 'id=910&version=6&source=%2F%0A+*++QAQAAAAQQQonnected+Switch%0A+*%0A+*++Copyright+2017+konnected.io%0A+*%0A+*++Licensed+under+the+Apache+License%2C+Version+2.0+(the+%22License%22)%3B+you+may+not+use+this+file+except%0A+*++in+compliance+with+the+License.+You+may+obtain+a+copy+of+the+License+at%3A%0A+*%0A+*++++++http%3A%2F%2Fwww.apache.org%2Flicenses%2FLICENSE-2.0%0A+*%0A+*++Unless+required+by+applicable+law+or+agreed+to+in+writing%2C+software+distributed+under+the+License+is+distributed%0A+*++on+an+%22AS+IS%22+BASIS%2C+WITHOUT+WARRANTIES+OR+CONDITIONS+OF+ANY+KIND%2C+either+express+or+implied.+See+the+License%0A+*++for+the+specific+language+governing+permissions+and+limitations+under+the+License.%0A+*%0A+*%2F%0Ametadata+%7B%0A++definition+(name%3A+%22blah%22%2C+namespace%3A+%22loghound%22%2C+author%3A+%22john%22%2C+mnmn%3A+%22SmartThings%22%2C+vid%3A+%22generic-switch%22)+%7B%0A++++capability+%22Switch%22%0A++++capability+%22Actuator%22%0A++%7D%0A%0A%0A%0A%7D%0A' \
#   --compressed 


#python upload
from __future__ import print_function
import requests
import json 
import re
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
print (sys.argv[1])

if (len(sys.argv)<2) :
  eprint("Error -- not enough arguments")
  exit()

idNumber=re.search(".*-([0-9].*).groovy",sys.argv[1]).group(1)
response = requests.get('http://192.168.86.42/driver/ajax/code?id='+idNumber)
version=json.loads(str(response.content.decode('utf-8')))['version'] # could be 'id' or 'source' or 'status'

with open(sys.argv[1], 'r') as myfile:
  driver = myfile.read()

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Language': 'en-US,en;q=0.9',
}

data = {
  'id': idNumber,
  'version': version,
  'source': driver
}

response = requests.post('http://192.168.86.42/driver/ajax/update', headers=headers, data=data)

resp_json=response.json()


if (resp_json['status']!='success'):
    str=resp_json['errorMessage']
    lineNumber=re.search("line ([-+]?\d+)",str).group(1)
    columnNumber=re.search("column ([-+]?\d+)",str).group(1)
    eprint("line" , lineNumber , 'col' , columnNumber , ":" , resp_json['errorMessage'])

print(response.json())




# #curl 'http://192.168.86.42/driver/ajax/code?id=910' 
#  #python download


# response = requests.get('http://192.168.86.42/driver/ajax/code?id=910')
# print(json.loads(str(response.content.decode('utf-8')))['version']) # could be 'id' or 'source' or 'status'


