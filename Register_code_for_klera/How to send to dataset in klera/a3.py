import pandas as pd 
from MessageSender import MessageSender, MessageType 

klera_meta_out = {
    "Emp": {
        "DSTID": "Emp_1.0.0",
        "Id": {
            "isrowid": True,
            "isvisible": True,
            "datatype": "STRING"
        }
    } ,
    "Emp1": {
        "DSTID": "Emp1_1.0.0",
        "Id": {
            "isrowid": True,
            "isvisible": True,
            "datatype": "STRING"
        }
    }
}


dict1={"Id":"xy","Name":"Anurag"}

df=pd.DataFrame(data=dict1,index=[0])

dict2={"Id":"yz","Name":"Ashu"}

df1=pd.DataFrame(data=dict2,index=[0])

out_dict1 = {'Emp': df,'Emp1':df1}
klera_dst = [out_dict1]
