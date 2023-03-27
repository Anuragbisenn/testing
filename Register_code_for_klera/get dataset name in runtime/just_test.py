import pandas as pd 
from MessageSender import MessageSender, MessageType   



klera_in_details = {
    "FilePath": {
        "datatype": ["STRING"],
        "argtype": "Param",
        "required": True,
        "multiplerows":True
    },
    "DatasetName": {
        "datatype": ["STRING"],
        "argtype": "Param",
        "required": True,
        "multiplerows":True
    }
}

path=FilePath[:]
Name=DatasetName[:]

klera_meta_out = {

    Name : {
        "DSTID": Name+"_1.0.0",
        "id": {
            "isrowid": True,
            "isvisible": True,
            "datatype": "INT"
        }
    }

}

file=pd.read_csv(path)
df=pd.DataFrame(file)
out_dict1 = {Name: df}
klera_dst = [out_dict1]