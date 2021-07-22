import xlrd
import sys
import os
sys.path.append('../')
from Fduers.settings import MEDIA_ROOT

def decode(path):
    if not (path.endswith(".xls") or path.endswith(".xlsx")): # isn't an excel file, return a blank list
        return []
    
    path = os.path.join(MEDIA_ROOT, path)
    data = xlrd.open_workbook(path)

    sheetName = data.sheet_names()

    print(sheetName)

    # each item of stuList: [name, stuID, department, grade]
    stuList = []

    for year in sheetName:
        table = data.sheet_by_name(year)
        upperbound = table.nrows

        name_idx = 0
        stuID_idx = 0
        department_idx = 0

        grade = 0

        for i in range(0, len(year)):
            if not year[i].isdigit():
                break
            grade = grade * 10 + int(year[i])

        title = table.row(0)

        for i in range(0, len(title)):
            if title[i].value == r'姓名':
                name_idx = i
            elif title[i].value == r'学号':
                stuID_idx = i
            elif title[i].value == r'院系' or title[i] == r'学院':
                department_idx = i

        for i in range(1, upperbound):
            row = table.row(i)
            stuList.append([row[name_idx].value, row[stuID_idx].value, row[department_idx].value, grade])

    return stuList



if __name__ == "__main__":
    path = "../generator/data/example.xls" # absolute path of testing file
    result = decode(path)
    for student in result:
        print(student)
    
