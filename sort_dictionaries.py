# Define a dictionary to store employee information
employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
]

def sort_employees_by_age():
    result = employee_data.copy()
    result.sort(key=lambda x: x['age'])
    return result


def sort_employees_by_dept_then_age():
    result = employee_data.copy()
    result.sort(key=lambda x: (x['department'],x['age']))
    return result


def desc_sort_employees_by_dept_then_age():
    result = employee_data.copy()
    result.sort(key=lambda x: (x['department'],x['age']), reverse=True)
    return result



def sort_employees_by_dept_desc_then_age_asc():
    result = employee_data.copy()
    result.sort(key=lambda x: (x['department'],-x['age']), reverse=True)
    return result




def display_all_records():
    print(("Name" + "\t" +"Age" +"\t" +"Department" +"\t" +"Salary" ).expandtabs(15))
    for item in employee_data:
        print((item["name"] + "\t" + str(item["age"]) + "\t" + item["department"] + "\t" + str(item["salary"])).expandtabs(15))


def display_records(employee_info):
    print(("Name" + "\t" +"Age" +"\t" +"Department" +"\t" +"Salary" ).expandtabs(15))
    for item in employee_info:
        print((item["name"] + "\t" + str(item["age"]) + "\t" + item["department"] + "\t" + str(item["salary"])).expandtabs(15))



def main():
    original = [1,2,3,4,5]
    print(original[::-1])
    display_all_records()
    print("----- Sort by Age -----")
    sortedlist = sort_employees_by_age()
    display_records(sortedlist)
    print("----- Sort by Department, then by Age -----")
    sortedlist = sort_employees_by_dept_then_age()
    display_records(sortedlist)
    print("----- Descending Sort by Department, then by Age -----")
    sortedlist = desc_sort_employees_by_dept_then_age()
    display_records(sortedlist)
    print("----- Sort by Department (desc), then by Age (asc) -----")
    sortedlist = sort_employees_by_dept_desc_then_age_asc()
    display_records(sortedlist)

   


if __name__ == "__main__":
    main()