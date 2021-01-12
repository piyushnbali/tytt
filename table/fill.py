import xlrd
from django.db import models
from table.models import timetable
loc = (r"E:\Working\timetable\PBTT .xls")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

for i in range(1,sheet.nrows):
    try:
        r = timetable(Subject=sheet.cell_value(i, 0),Day=sheet.cell_value(i, 1),start_time_min=int(sheet.cell_value(i, 2)),end_time_min=int(sheet.cell_value(i, 3)))
        r.save()
    except:
        print(sheet.cell_value(i, 0))
        print(sheet.cell_value(i, 1))
        print(sheet.cell_value(i, 2))
        print(sheet.cell_value(i, 3))
    


