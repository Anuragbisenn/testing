"""This code has written by Anurag Bisen 
   on the  Date 09-06-2022
   version 1.0.0
    """

#imported required libraries.

import string
import requests
import json
import pandas as pd
from MessageSender import MessageSender, MessageType 


# Output Meta Details
klera_meta_out = {
    "All Users Details": {
        "DSTID": "All Users Details_1.0.0",
        "Key": {
            "isrowid": True,
            "isvisible": True,
            "datatype": "STRING"
        }
    }
}

# Required Input Details
klera_in_details = {
    "Instance_Url": {
        "datatype": ["STRING"],
        "argtype": "Param",
        "required": True,
        "multiplerows":True
    },
    "User_Name": {
        "datatype": ["STRING"],
        "argtype": "Param",
        "required": True,
        "multiplerows":True
    },
    "Password": {
        "datatype": ["STRING"],
        "argtype": "Param",
        "required": True,
        "masked":True,
        "multiplerows":True
    }
}

#outhentication accessed by user 
username = User_Name[:]
password = Password[:]

#instance url accessed by user 
instance_url=Instance_Url[:]

url=instance_url+"/rest/api/2/user/search?username="
letters=[]
name_list=[]
self_list=[]
key_list=[]
email_list=[]
Displayname_list=[]
Active_list=[]
del_list=[]
Timezone_list=[]
locel_list=[]
list48=[]
list24=[]
list16=[]
list32=[]

for letter in string.ascii_lowercase:
   letters.append(letter)


for letter in letters:
    # start1 has declared for pagination stuff.
    start1=0
    
    while(1):
        
        response_API = requests.get(url+letter+"&maxResults=100"+"&startAt="+str(start1),auth=(username,password))
        data1=response_API.text
        parse_json = json.loads(data1)
        a=len(parse_json)

        if (a==0):
            break
        
        # increment each time for next 100 records.
        start1=start1+100
        for i in range(a):
           
            b=parse_json[i]['name']
            if  b not in name_list:
                name_list.append(b)

                c=parse_json[i]['emailAddress']
                email_list.append(c)

                d=parse_json[i]['key']
                key_list.append(d)
                
                e=parse_json[i]['displayName']
                Displayname_list.append(e)

                f=parse_json[i]['active']
                Active_list.append(f)

                g=parse_json[i]['deleted']
                del_list.append(g)

                h=parse_json[i]['timeZone']
                Timezone_list.append(h)

                j=parse_json[i]['locale']
                locel_list.append(j)

                k=parse_json[i]['avatarUrls']['16x16']
                list16.append(k)

                l=parse_json[i]['avatarUrls']['24x24']
                list24.append(l)

                m=parse_json[i]['avatarUrls']['32x32']
                list32.append(m)

                n=parse_json[i]['avatarUrls']['48x48']
                list48.append(n)

                o=parse_json[i]['self']
                self_list.append(o)

        

# converting into Dataframe obj of lists.
df={
  'Name':name_list,
  'Email':email_list,
  'Key':key_list,
  'Display Name':Displayname_list,
  'Active':Active_list,
  'Deleted':del_list,
  'TimeZone':Timezone_list,
  'Locale':locel_list,
  'Self':self_list,
  'AvtarUrl 16x16':list16,
  'AvtarUrl 24x24':list24,
  'AvtarUrl 32x32':list32,
  'AvtarUrl 48x48':list48

}

# Creating Pandas Dataframe and assiging the dict created from the response.
out_df1 = pd.DataFrame(data=df)
out_dict1 = {'All Users Data List': out_df1}
klera_dst = [out_dict1]
