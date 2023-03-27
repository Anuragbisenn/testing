import pandas as pd 
from MessageSender import MessageSender, MessageType   

klera_meta_out = {
    "Abx3" : {
        "DSTID": "Abx3_1.0.0",
        "y": {
            "isrowid": True,
            "isvisible": True,
            "datatype": "STRING"
        }
    }
}

klera_in = ["Rank","steps"]

klera_in_details = {
    "Rank": { 
        "description":"Rank column",
        "datatype":["STRING"],
        "argtype":"Data",
        "multivalued":False,
        "multicolumn":True },

     "Steps": {
        "description":"Steps Count",
        "datatype":["INT","LONG"],
        "argtype":"Param",
        "multivalued":False,
        "multicolumn":False,
        "min":3,
        "max":100,
        "default":4 
     }

}

x=Rank[:]
y=["Anurag","Ram","Arvind"]

dict={"First":x,"Second":y}

out_df1 = pd.DataFrame(data=dict)
out_dict1 = {'Abx3': out_df1}
klera_dst = [out_dict1]