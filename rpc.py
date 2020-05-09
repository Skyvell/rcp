import requests
import pprint as pp
import json

# Not sure if the header is strictly needed. Included it anyway.
# The URL is basically a way to represent the RPC server's ipaddress and which portnumber to use, alphabetically.
# I think you can enter your own node's RPC endpoint here if you want.
HEADERS = {'content-type': 'application/json'}
URL = "https://ctz.solidwallet.io/api/v3" 


# A funtion for getting blockdata from a specified block.
def get_block(blocknr):
    # Convert blocknr to hexadecimal.
    blocknr = hex(blocknr)
    
    # Data to be sent to the API.
    payload = {
                "jsonrpc": '2.0',
                "id": '12',
                "method": "icx_getBlockByHeight",
                "params": {"height": blocknr}
              }

    # Send the data request to the API and returns the response. (json.dumps(payload) converts the python dictionary to json format)
    response = requests.post(URL, data=json.dumps(payload), headers=HEADERS)

    # Converts the jsondata recived to a python dictionary.
    response = response.json()
    return response


# A function for getting prep information about specified prep.
def get_prep(address):
    payload = {
                  "jsonrpc": "2.0",
                  "id": 13,
                  "method": "icx_call",
                  "params": 
                  {
                      "to": "cx0000000000000000000000000000000000000000",
                      "dataType": "call",
                      "data": 
                      {
                          "method": "getPRep",
                          "params": {"address": address}
                      }
                  }
              }
    response = requests.post(URL, data=json.dumps(payload), headers=HEADERS)
    response = response.json()
    return response
  
# Call and print results of get_block.
print("get_block:")
pp.pprint(get_block(500))

# Print whitespaces.
print("\n" * 2)

# Call and print results of get_prep.
print("get_prep:")
pp.pprint(get_prep("hx2f3fb9a9ff98df2145936d2bfcaa3837a289496b"))

