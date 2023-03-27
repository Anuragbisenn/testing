klera_dict={}
list1=["Anurag","Ram","Abhay"]

for i in range(len(list1)):

    klera_dict.setdefault("Name",[]).append(list1[i])


print(klera_dict)