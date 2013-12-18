import arcpy, time, datetime, csv, sys, traceback
from arcpy import env
env.overwriteOutput = True

#MacBook Pro-Windows 7
drive_path = "V:/"
#dropbox_path = "W:/"

#008
drive_path = "E:/SpiderOak/"
#dropbox_path = "W:/"

fl = drive_path + "projects/hospitals/"
fld = fl + "data"

fields_to_add = ['newarea','pctorgarea']
filesuf = "/processing/processing.gdb/na_albers_equal_area_conic/points_b05mile_intersect_tracts_2000_dis"

print "go"

for fieldsadd in fields_to_add:
	
	arcpy.AddField_management(fld+filesuf, fieldsadd, "FLOAT")

field_exps = ["!shape.area@squaremeters!","!newarea!/!tractareasqmeters!"]	

for fieldsadd, fieldexps in zip(fields_to_add, field_exps):
	filesuf = "/processing/processing.gdb/na_albers_equal_area_conic/points_b05mile_intersect_tracts_2000_dis"
	arcpy.CalculateField_management(fld+filesuf, fieldsadd, fieldexps, "PYTHON_9.3")

	print "1 down"


#RUN IN PYTHON.exe 