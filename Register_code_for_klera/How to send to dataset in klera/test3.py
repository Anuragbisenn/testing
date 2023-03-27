import pandas as pd
import os
from MessageSender import MessageSender, MessageType 

klera_meta_out = {
    "EMP9": {
        "DSTID": "EMP9_1.0.2",
        "id": {
            "isrowid": True,
            "isvisible": True,
            "datatype": "STRING"
        }
    },
    "EMP10": {
        "DSTID": "EMP10_1.0.2",
        "id": {
            "isrowid": True,
            "isvisible": True,
            "datatype": "STRING"
        }
    },
    "EMP11": {
        "DSTID": "EMP11_1.0.2",
        "id": {
            "isrowid": True,
            "isvisible": True,
            "datatype": "STRING"
        }
    }
}



dir_path = os.path.dirname(os.path.realpath(__file__))
filepath = str(dir_path) + "\\csvout\\"
#filepath = "csvout\\"



data1 = [
{
    "name" : "Ashu1",
    "id" : "1",
},
{
    "name" : "An2",
    "id" : "2",
},
]

data2 = [
{
    "name" : "Ashu3",
    "id" : "1",
},
{
    "name" : "An4",
    "id" : "2",
},
]

data3 = [
{
    "name" : "Ashu5",
    "id" : "1",
},
{
    "name" : "An6",
    "id" : "2",
},
]


df1 = pd.DataFrame(data=data1)
df1.to_csv(filepath + "file_1.csv",index=False)

df2 = pd.DataFrame(data=data2)
df2.to_csv(filepath + "file_2.csv",index=False)

df3 = pd.DataFrame(data=data3)
df3.to_csv(filepath + "file_3.csv",index=False)

K1=pd.read_csv(filepath+"file_1.csv")
l1=pd.read_csv(filepath+"file_2.csv")
m1=pd.read_csv(filepath+"file_3.csv")

out_dict1 = {'EMP9': K1,'EMP10':l1,'EMP11':m1}
klera_dst = [out_dict1]


