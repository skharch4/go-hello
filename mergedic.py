def merge(dic1,dic2):
    dic3=dic1.copy()
    dic3.update(dic2)
    return dic3
dic1 = {1:"Orange", 2:"Pineapple"}  
dic2 = { 3:"Cherry", 4:"Melon",5:"Strawberry"}
dic3 = [dic1,dic2]
print (dic3)
