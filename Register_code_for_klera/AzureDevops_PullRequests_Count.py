import requests
from requests.auth import HTTPBasicAuth
import json
import pandas as pd

url = "https://dev.azure.com/ashutoshagrawal0460/415af66e-4759-46ac-9c12-04dbce37f324/_apis/git/pullrequests?api-version=5.0"

top = 1
skip=0
kleradict = {}
flag = True

while flag:
    tosendurl = url + "&$top=" + str(top) + "&$skip=" + str(skip)
    req = requests.get(tosendurl,auth = HTTPBasicAuth('ashutosh.agrawal@clear-trail.com','kf3zqaxa3eevlvgt46exjv5jadhj7mwgm5p7ujmagvb3b5k2tjua'))
    #result = json.loads(req.content, indent=4, sort_keys=True, default=str)
    #print(req.content)
    result = json.loads(req.content)
    #r = json.loads(result, indent=4, sort_keys=True, default=str)

    for record in result['value']:
        kleradict.setdefault('Pull Request Id',[]).append(record['pullRequestId'])
        kleradict.setdefault('API URL', []).append(tosendurl)

    skip = skip + top

    if result['value']:
        flag = True
    else:
        flag = False

df = pd.DataFrame(data=kleradict)
df.to_csv("dump.csv")
#print(df)