
import pandas as pd 
from MessageSender import MessageSender, MessageType   


klera_meta_out = {

    "Practice1": {
        "DSTID": "Practice1_1.2.3",
        "Number": {
            "isrowid": True,
            "isvisible": True,
            "datatype": "STRING"
        }
    }

}

klera_in=["Options"]

klera_in_details ={
 "Options":{ 
        "description":"Options Column",
        "datatype":["STRING","INT","LONG","NUMERIC","DATE","DATETIME","TIME","BOOL"],
        "argtype":"Data",
        "multivalued":False,
        "multicolumn":True 
         }
    
}
    
df = pd.DataFrame(Options)
num_cols = df.shape[1]
new_cols = []
for col in range(0,num_cols):
    new_cols.append(klera_meta_in["Options"][col]["name"])
df.columns = new_cols[:num_cols]

out_dict1 = {"Practice1": df}
klera_dst = [out_dict1]