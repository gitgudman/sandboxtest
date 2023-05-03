import requests
from pprint import pprint
import json
import string
import sys
times_to_repeat = 3


# imei_input = input('enter imei : ').split()
# imei_input2 = input('enter imei : ')
url = "https://join.t-mobile.com/api/get_byod_check"
url2 = "https://join.t-mobile.com/api/access_token"
# no_of_lines = 5


imei_input1 = input("enter 3 numbers :\n").split(' ')
res = requests.get(url2)
data = res.json()

# querystring = {"imeiNumber":(imei_input)}
querystring = {"imeiNumber1":(imei_input1)}

#unlockinfo = data[0]['Unlocked']
#carrierinfo = data[0]['CarrierName']
manuinfo = data[0]['Manufacturer']
#modelinfo = data[0]['MarketingName']
#blockinfo = data[0]['Blocked']


headers = {
    'Authorization': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvYXV0aCI6ImNmZTUxM2RjLTcyMmQtNGJlNC04ZjRkLTRlMjMyOGRjODcyOSIsImlhdCI6MTU2NTkxMDc5NSwiZXhwIjoxNTY1OTExMzk5fQ.PFqcZx6vVQPkb0xNOgGTsM3F11CgwhzKXS3t_ugR-EY",
    'User-Agent': "PostmanRuntime/7.15.2",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "a6df9036-9454-4956-b54c-424d71348bad,b50544ae-3a40-4894-ad56-fb08db2c0e1c",
    'Host': "join.t-mobile.com",
    'Cookie': "visid_incap_1846188=JCROQ/zUQ7CSpIn4cCEoRnRKMF0AAAAAQUIPAAAAAACzW2KZ4a/jFUL2hhE6Tfzu; nlbi_1846188=B1CoTH8WPBnp94xm26+O3gAAAACnCWJvnJYeNE4ZaHJFfhVb; incap_ses_1227_1846188=bA/eIkdOEE91tMP0QC4HEfytSl0AAAAAR3aaMIXYL1BXPtGEs95KbQ==; ___utmvmvOBulDPzB=oXFOfuUIHHH; ___utmvbvOBulDPzB=ZZc    XeZOealN: NtN",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }




response = requests.request("GET", url, headers=headers, params=querystring)

pprint(response.text)

pprint(data)
print('IMEI : {}'.format(manuinfo))
#input('Press ENTER to exit')

