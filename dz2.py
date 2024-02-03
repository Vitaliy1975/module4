def get_cats_info(path):

    try:
        with open(path,"r",encoding="utf-8") as file:
            lines=file.readlines()
    except Exception as e:
        return e
    
    list_of_strings=[]
    for line in lines:
        id,name,age=line.split(",")
        age=age.strip()
        diction={"id":id,"name":name,"age":age}
        list_of_strings.append(diction)

    return list_of_strings
