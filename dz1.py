
def total_salary(path):
    
    try:
        with open(path,"r",encoding="utf-8") as file:
            lines=file.readlines()
    except Exception as e:
        return e
    
    salaries_list=[]
    for line in lines:
        _,salary=line.split(",")
        salary=salary.strip()
        salary=int(salary)
        salaries_list.append(salary)
    total=sum(salaries_list)
    average=total/len(salaries_list)
    return (total,average)
