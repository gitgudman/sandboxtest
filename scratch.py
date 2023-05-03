def main():
    import requests
    from termcolor import cprint, colored
    import colorama
    colorama.init()
#    import os
#    cmd = 'color 0B'
#    os.system(cmd)

    import json
    from pprint import pprint
    import urllib.request
    import base64

    # api_token = 'your_api_token'
    res2 = requests.get('https://join.t-mobile.com/api/access_token')
    # headers = {'Content-Type': 'application/json',
    #           'Authorization': 'Bearer {0}'.format(api_token)}
    data2 = res2.json()

    apitoken = data2['access_token']
    print('Authenticated = {}' .format(colored(apitoken, 'white', attrs=['bold'])))
    print()
    while True:
        imei_input = input('Enter IMEI(s):\n')
        res = requests.get('https://join.t-mobile.com/api/get_byod_check?imeiNumber={}'.format(imei_input),
                           headers={'Authorization': (apitoken)})
        if imei_input == 'r' or imei_input == 'restart':
            main()
        data = res.json()
        print()
        # api token check
        #    try:
        #        apicheck1 = data['error']['expiredAt']
        #        apicheck2 = data['error']['name']
        #        print('API Status: {} \nTime: {}'.format(apicheck2, apicheck1))
        #    except KeyError:
        #        pass
        dict.get


        try:
            marketdata = data[0]['MarketingName']
            print('Model: {} '.format(colored(marketdata, 'cyan', attrs=['bold'])))
        except KeyError:
            pass

        try:
            imeidata = data[0]['IMEI']
            print('IMEI: {} '.format(colored(imeidata, 'white', attrs=['bold', 'dark'])))
        except KeyError:
            pass

        try:
            carrierdata = data[0]['CarrierName']
            print('Carrier: {} '.format(colored(carrierdata, 'cyan', attrs=['bold', 'dark'])))
        except KeyError:
            pass

        try:
            manufdata = data[0]['Manufacturer']
            print('Manufacturer: {} '.format(colored(manufdata, 'white', attrs=['bold'])))
        except KeyError:
            pass

        try:
            unlockdata = data[0]['Unlocked']
            if data[0]['Unlocked'] == 1:
                cprint("Unlocked", 'green', attrs=['bold', 'dark'])
            else:
                cprint("Network Locked", 'red', attrs=['bold', 'dark'])
        except KeyError:
            pass

        try:
            balancedata = data[0]['FullyPaidOff']
            if data[0]['FullyPaidOff'] == 0: # 0 is false paid off
                cprint("Outstanding Balances", 'yellow', attrs=['bold', 'dark'])
            else:
                cprint("Paid Off", 'green', attrs=['bold'])
        except KeyError:
            pass

        try:
            blockdata = data[0]['Blocked']
            if data[0]['Blocked'] == 1:
                cprint("Blacklisted", 'red', attrs=['bold', 'dark'])
            else:
                cprint("Clean", 'green', attrs=['bold'])
        except KeyError:
            pass

        print()
main()
