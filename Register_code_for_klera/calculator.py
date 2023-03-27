"""This code has written by Anurag Bisen 
   on the  Date 09-06-2022
   version 1.0.0
    """

#imported required libraries.

import pandas as pd
from MessageSender import MessageSender, MessageType 

Opration=['a','b']

klera_meta_out = {
    "CalculatorAB": {
        "DSTID": "CalculatorAB_1.0.0",
        "Opration": {
            "isrowid": True,
            "isvisible": True,
            "datatype": "STRING"
        }
    }
}

klera_in_details = {
    

    "Number1": {
        "datatype": ["INT"],
        "argtype": "Param",
        "required": True,
        "multiplerows":True
    },
    "Number2": {
        "datatype": ["INT"],
        "argtype": "Param",
        "required": True,
        "multiplerows":True
    },
    "Opration": {
        "datatype": ["STRING"],
        "argtype": "Data",
        "required": True,
        "multiplerows":True
    }
}

input_first=Number1[:]
input_second=Number2[:]

op=Opration[:]

if(op[0]=="Add"):
    result1=input_first[0]+input_second[0]
elif(op[0]=="Sub"):
    result2=input_first[0]+input_second[0]
elif(op[0]=="Multi"):
    result3=input_first[0]*input_second[0]
elif(op[0]=="Div"])
    result4=input_first[0]/input_second[0]


df={'Opration':["Addition","Sub","Multi","Div"],'result':[result1,result2,result3,result4]}

out_df1 = pd.DataFrame(data=df)
out_df1.dropna(axis=1,inplace=True)
out_dict1 = {'All Users Data List': out_df1}
klera_dst = [out_dict1]