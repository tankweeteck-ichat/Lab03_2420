import employee_info as EMP
from employee_info import employee_data as EMPDATA
print("Test employee_info")


def test_age_range():
    '''
    expected = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]
    '''
    expected = [EMPDATA[0], EMPDATA[4]]
    result = []
    result = EMP.get_employees_by_age_range(29, 33)
    assert(result==expected)


def test_average_salary():
    expected = 60166.67
    result = EMP.calculate_average_salary()
    result = round(result,2)
    assert(result==expected)


def test_department():
    '''
    expected = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}]
    '''
    expected = [EMPDATA[0], EMPDATA[-1]]
    result=[]
    result = EMP.get_employees_by_dept('Sales')
    assert(result==expected)