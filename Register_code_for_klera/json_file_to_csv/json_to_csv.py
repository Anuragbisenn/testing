"""This code has written by Anurag Bisen 
   version 1.0.0
   on the  Date 09-06-2022 """

#imported required libraries.

import string
import requests
import json
import pandas as pd



# Output Meta Details
klera_meta_out = {
    "All Users Data": {
        "DSTID": "All Users Data_1.0.0",
        "name": {
            "isrowid": True,
            "isvisible": True,
            "datatype": "STRING"
        }
    }
}

username = "admin"
password = "Ctadmin@123"

url="http://54.215.87.148:8080/rest/api/2/user/search?username="
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

temp=1

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
df=pd.DataFrame({
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

})

df.to_csv('user_data10.csv')

print("Done...")
