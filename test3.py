import xlwt
import xlrd
import os
###############################################################################
#
#  createExcelWorkbook
#
# ##############################################################################    
def createExcelWorkbook () :    
    workbook = xlwt.Workbook() # create workbook
    return workbook

###############################################################################
#
#  createExcelSheet
#
# ##############################################################################    
def createExcelSheet (workbook, tab_name) :  
    sheet1 = workbook.add_sheet(tab_name)
    sheet1.write(0,0,"Name")
    sheet1.write(0,1,"code")
    sheet1.write(0,2,"money")
    
    
    
    
    
    
    
    
        
    
    return sheet1

################################################################################
#
# saveExcelTable
#
# ##############################################################################    
def saveExcelTable(workbook, file):
    try:
        workbook.save(file)
        
    except PermissionError:
        print("Permission denied!!!!!!!!!!!!!")
        ret = input("Do you want to remove ?")
        if ret == "Y" or ret == "y":
            os.remove(file)
            workbook.save(file)
            
    else:
        pass

################################################################################
#
# excelRead
#
# ##############################################################################    
def excelRead(file):
    wb = xlrd.open_workbook(filename=file) # open file
    sheet1 = wb.sheet_by_index(0)
    nrows = sheet1.nrows
    ncols = sheet1.ncols    
    
    print("Total rows:",nrows)
    print("Total cols:",ncols)

    for i in range (0,nrows):
        for j in range(0, ncols):
            print(sheet1.cell(i,j).value," ", end="")
        print("\n")



studentDict = {
    "朱予墨": 88888888, 
    "李路加": 666666,
    "dad" :123456789,  
    "mom":987654321,
    "duck" :1234567,
    "god":1514664,
}

workbook = createExcelWorkbook()
sheet = createExcelSheet(workbook, "2020-2-27")
row = 1
for student in studentDict.keys():
    sheet.write(row,0,student)
    sheet.write(row,1,studentDict[student])
    row += 1

saveExcelTable(workbook, "test2.xls" )
excelRead("test2.xls")
