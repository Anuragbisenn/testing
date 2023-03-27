import pandas as pd 
from MessageSender import MessageSender, MessageType   


klera_meta_out = {

    "Practice": {
        "NAME": "Practice_1.0.1",
        "Sequence Number": {
            "isrowid": True,
            "isvisible": True,
            "datatype": "STRING"
        }
    }

}

klera_in_details = {
    "NAME": {
        "datatype": ["STRING"],
        "argtype": "Data",
        "required": True,
        "multiplerows":True
    },
    "SURNAME": {
        "datatype": ["STRING"],
        "argtype": "Data",
        "required": True,
        "multiplerows":True
    }
}

name=NAME[:]
surname=SURNAME[:]

fullName=name+surname

klera_dict={"full_name":fullName}

out_df1 = pd.DataFrame(data=klera_dict)
out_dict1 = {'All Users Data List': out_df1}
klera_dst = [out_dict1]