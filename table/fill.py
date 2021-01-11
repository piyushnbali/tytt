import xlrd
from django.db import models
from table.models import timetable
loc = (r"E:\Working\timetable\temp.xls")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

for i in range(1,sheet.nrows):
    r = timetable(Subject=sheet.cell_value(i, 0),Day=sheet.cell_value(i, 1),start_time_min=int(sheet.cell_value(i, 2)),end_time_min=int(sheet.cell_value(i, 3)))
    r.save()
    


