import pandas as pd 
#from MessageSender import MessageSender, MessageType   



Dataset = "abc"
Name=Dataset

klera_meta_out = {

    Name : {
        "DSTID": Name+"_1.0.0",
        "x": {
            "isrowid": True,
            "isvisible": True,
            "datatype": "STRING"
        }
    }

}

klera_in_details = {
    "Dataset": {
        "datatype": ["STRING"],
        "argtype": "Param",
        "required": True,
        "multiplerows":True
    }
}

print(klera_meta_out)

x=["1","2","3"]
y=["d","e","f"]

dict={"first":x,"Second":y}

out_df1 = pd.DataFrame(data=dict)
out_dict1 = {Name: out_df1}
klera_dst = [out_dict1]