import pandas as pd 
from MessageSender import MessageSender, MessageType 

klera_meta_out = {
    "Data": {
        "DSTID": "Data_1.0.0",
        "Name": {
            "isrowid": True,
            "isvisible": True,
            "datatype": "STRING"
        }
    }
}


dict1={"Name":"Anurag","surname":"Bisen"}

df=pd.DataFrame(data=dict1,index=[0])

out_dict1 = {'Data': df}
klera_dst = [out_dict1]
