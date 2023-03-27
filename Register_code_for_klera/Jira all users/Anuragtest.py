# This code sample uses the 'requests' library:
# http://docs.python-requests.org
from tkinter.tix import COLUMN
import requests
from requests.auth import HTTPBasicAuth
import json
import string
import pandas as pd
url = "https://your-domain.atlassian.net/rest/api/3/serverInfo"

auth = HTTPBasicAuth("kushagra.behere5@gmail.com", "FiswSuvI1y8aVaxz8IzC9300")

headers = {
   "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)
"""
Parse=json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
print(Parse)

"""
List1=[]
List2=[]

Data=json.loads(response.text)
List1.append(Data['baseUrl'])
List2.append(Data['version'])

df={'COLUMN1':List1,'COLUMN2':List2}

out_df1 = pd.DataFrame(data=df)
out_dict1 = {'TestData': out_df1}
klera_dst = [out_dict1]
