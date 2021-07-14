import xlrd

def decode(path):
    if !(path.endswith(".xls") or path.endswith(".xlsx")): # isn't an excel file, return a blank list
        return []
    
    data = xlrd.open_workbook(filename)
    table = data.sheets()

    print(table)

if __name__ == "__main__":
    path = "../testingfile/example.xls" # absolute path of testing file
    result = decode(path)
    for student in result:
        print(student)
    
