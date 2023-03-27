
import pandas as pd 
from MessageSender import MessageSender, MessageType   

klera_meta_out = {
    "Name" : {
        "DSTID": "Name_1.0.0",
        "x": {
            "isrowid": True,
            "isvisible": True,
            "datatype": "STRING"
        }
    }

}

x=["1","2"]
z=["a","b"]
dict={"First":x,"second":z}

out_df1 = pd.DataFrame(data=dict)
out_dict1 = {"Name": out_df1}
klera_dst = [out_dict1]