import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    groups = employee.groupby(['departmentId', 'salary']).count().sort_values('salary', ascending=False).groupby(['departmentId']).head(3).reset_index()
    
    df = pd.merge(employee, groups[['departmentId', 'salary', 'id']], on=['departmentId', 'salary'], how='left', suffixes=('', '_merge'))
    df = df.dropna()
    df = pd.merge(df, department, left_on='departmentId', right_on='id', suffixes=('', '_department'))

    df = df.rename(
        columns={
            'name_department': 'Department',
            'name': 'Employee',
            'salary': 'Salary'
        })

    return df.sort_values('id')[['Department', 'Employee', 'Salary']]

employees = pd.DataFrame(
    [[1, "Joe", 85000, 1],
    [2, "Henry", 80000, 2],
    [3, "Sam", 60000, 2],
    [4, "Max", 90000, 1],
    [5, "Janet", 69000, 1],
    [6, "Randy", 85000, 1],
    [7, "Will", 70000, 1]]
    )
employees.columns = ["id", "name", "salary", "departmentId"]

department = pd.DataFrame(
    [[1, "IT"],
     [2, "Sales"]],
     columns=['id', 'name']
)

print(top_three_salaries(employees, department))