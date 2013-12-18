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

#for health insurance
print "make table view of points intersected w/ counties"
arcpy.MakeTableView_management(fld+"/processing/processing.gdb/na_albers_equal_area_conic/points_intersect_county","points_intersect_county_view")
print "join points/county w/ healthinsurance table"
arcpy.AddJoin_management("points_intersect_county_view","CNTYIDFP",fld+"/input/census/variables.gdb/healthinsurance","geoid","KEEP_ALL")

print "export health insurance table to tables.gdb"
arcpy.TableToTable_conversion("points_intersect_county_view",fld+"/processing/tables.gdb","health_insurance")

field_name_list = [
	"cnycntypop",
	"cnywithins",
	"cnywoutins",
	"cnypcwiins",
	"cnypcwoins"
]

for field_name in field_name_list:
	arcpy.AddField_management(fld+"/processing/tables.gdb/health_insurance", field_name, "FLOAT")

calc_expr_list = [
	"!healthinsurance_totpop!",
	"!healthinsurance_num_ins!",
	"!healthinsurance_num_uninsu!",
	"!cnywithins!/!cnycntypop!",
	"!cnywoutins!/!cnycntypop!"
]

for calc_field_name, calc_expr in zip(field_name_list, calc_expr_list):
	arcpy.CalculateField_management(fld+"/processing/tables.gdb/health_insurance", calc_field_name, calc_expr,"PYTHON_9.3","#")

#sample for ref
#arcpy.CalculateField_management("V:/projects/hospitals/data/processing/tables.gdb/health_insurance","inscntypop","!healthinsurance_totpop!","PYTHON_9.3","#")
