user_input= input("enter items using comma: ")
li= user_input.split(',')
li = [item.strip() for item in li]
print(len(li),':',li)
li_dict={}

for item in li:
    key=len(item)
    if key not in li_dict:
        li_dict[key]=[item]
    else:
        li_dict[key].append(item)
print(li_dict)         
