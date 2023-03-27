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
    "Test Data": {
        "DSTID": "Test Data_1.0.2",
        "Key": {
            "isrowid": True,
            "isvisible": True,
            "datatype": "STRING"
        }
    }
}

#start1=0
username = "admin"
password = "Ctadmin@123"
letters=[]
url="http://54.215.87.148:8080/rest/api/2/user/search?username="


for letter in string.ascii_lowercase:
   letters.append(letter)


for letter in letters:
    # start1 has declared for pagination stuff.
    
    start1=0

    response_API = requests.get(url+letter+"&maxResults=20"+"&startAt="+str(start1),auth=(username,password))
    data1=response_API.text
    parse_json = json.loads(data1)
    a=len(parse_json)
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
    

        
        
        
        
        
        # increment each time for next 100 records.
    #start1=start1+10
    for i in range(a):
           
        b=parse_json[i]['name']
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

          
        

# converting into Dataframe obj of lists.
        df={
        'Name':name_list,
        'Email':email_list,
        'Key':key_list,
        'Display Name':Displayname_list,
        'Active':Active_list,
        'Deleted':del_list,
       

        }

# Creating Pandas Dataframe and assiging the dict created from the response.
        out_df1 = pd.DataFrame(data=df)
        out_dict1 = {'Test Data': out_df1}
        klera_dst = [out_dict1]
        data_block = {}
        data_block['klera_dst'] = klera_dst
        data_block['klera_meta_out'] = klera_meta_out
        # Prepare a message block.
        message_block = {}
        # Message Type
        message_block ['message_type'] = MessageType.DATA
        message_block ['data_block'] = data_block
        # Push the data to Klera
        klera_message_sender.push_data_to_queue(message_block)