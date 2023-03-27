

import pandas as pd 
from MessageSender import MessageSender, MessageType   


klera_meta_out = {

    "Practice": {
        "NAME": "Practice_1.0.9",
        "Number": {
            "isrowid": True,
            "isvisible": True,
            "datatype": "INT"
        }
    }

}

klera_in_details = {
    
    "Date_column": { 
        "description":"Date",
        "datatype":["DATE","DATETIME","TIME"],
        "argtype":"Data",
        "multivalued":False,
        "multicolumn":False },
 "ForecastColumn": { 
        "description":"Forecast Column",
        "datatype":["INT","LONG","NUMERIC","STRING"],
        "argtype":"Data",
        "multivalued":False,
        "multicolumn":True },
"Steps": {
            "description":"Steps Count", 
            "datatype":["INT","LONG"],
            "argtype":"Param",
            "multivalued":False,
            "multicolumn":False,
            "min":3, "max":100,
            "default":4 }
    }

A=[1,2,3,4,6,7]
B=["a","b","c","d","e","f","g"]

dict={"First":A,"Second":B}

out_df1 = pd.DataFrame(data=dict)
out_dict1 = {Name: out_df1}
klera_dst = [out_dict1]