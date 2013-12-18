import arcpy, time, datetime, csv, sys, traceback
import shutil
from arcpy import env
env.overwriteOutput = True

arcpy.ImportToolbox('C:\Program Files (x86)\DataEast\XTools Pro\Toolbox\XTOOLS PRO.tbx')

#add state and zip so order of output csv is correct
arcpy.AddField_management("E:/SpiderOak/projects/hospitals/data/_original/nis/nis_hospitals_2004_2008.dbf","ST","TEXT","#","#","#","#","NULLABLE","NON_REQUIRED","#")
arcpy.AddField_management("E:/SpiderOak/projects/hospitals/data/_original/nis/nis_hospitals_2004_2008.dbf","ZIPcode","TEXT","#","#","#","#","NULLABLE","NON_REQUIRED","#")
#calc those fields
arcpy.CalculateField_management("E:/SpiderOak/projects/hospitals/data/_original/nis/nis_hospitals_2004_2008.dbf","ST","!STATE!","PYTHON_9.3","#")
arcpy.CalculateField_management("E:/SpiderOak/projects/hospitals/data/_original/nis/nis_hospitals_2004_2008.dbf","ZIPcode","!ZIP!","PYTHON_9.3","#")

arcpy.XToolsPro_Table2Text("E:/SpiderOak/projects/hospitals/data/_original/nis/nis_hospitals_2004_2008.dbf","ADDRESS;CITY;ST;ZIPcode","E:/SpiderOak/projects/hospitals/data/_original/nis/nis_hospitals_2004_2008.csv")

shutil.copy2("E:/SpiderOak/projects/hospitals/data/_original/nis/nis_hospitals_2004_2008.csv", "E:/SpiderOak/projects/hospitals/scripts/processing_nis/03_geocode/addr_raw.csv")

fin = csv.reader(open("E:/SpiderOak/projects/hospitals/scripts/processing_nis/03_geocode/addr_raw.csv", 'rb'), delimiter=',')
fout = open("E:/SpiderOak/projects/hospitals/scripts/processing_nis/03_geocode/addr.csv", 'w')

print 'Replace commas started at this time: ' + time.strftime('%c') 

for row in fin:
	for item in row:
		str_row = item     
		fout.write(str_row.replace(',',' '))
		fout.write(" ")
	fout.write("\n")

fout.close()