import pandas as pd 
from MessageSender import MessageSender, MessageType   


klera_meta_out = {

    "Testx": {
        "DSTID": "TestX_1.0.0",
        "Charactor": {
            "isrowid": True,
            "isvisible": True,
            "datatype": "STRING"
        }
    }

}

Charactor=["a","b","c","d"]
Name=["Apple","Bat","Cat","Dog"]

dict1={"Charactor":Charactor,"Name":Name}

df=pd.DataFrame(dict1)

out_dict={"Testx":df}

klera_dst = [out_dict]