"""This code has written by Anurag Bisen 
   version 1.0.0
   on the  Date 09-06-2022 """

#imported required libraries.

import pandas as pd
from MessageSender import MessageSender, MessageType 

# Output Meta Details
klera_meta_out = {
    "AB Calculator": {
        "DSTID": "AB Calculator_1.0.0",
        "id": {
            "isrowid": True,
            "isvisible": True,
            "datatype": "STRING"
        }
    }
}

# Required Input Details
klera_in_details = {
    "Client_ID": {
        "datatype": ["STRING"],
        "argtype": "Data",
        "required": True,
        "multiplerows":True
    },
    "Client_Secret": {
        "datatype": ["STRING"],
        "argtype": "Data",
        "required": True,
        "multiplerows":True
    },
    "AWS_Region": {
        "datatype": ["STRING"],
        "argtype": "Data",
        "required": True,
        "multiplerows":True
    },
    "Build_Ids": {
        "datatype": ["STRING"],
        "argtype": "Data",
        "required": True,
        "multiplerows":True
    }
}







out_df1 = pd.DataFrame(data=kleraDict)
out_dict1 = {'Calculator': out_df1}
klera_dst = [out_dict1]
