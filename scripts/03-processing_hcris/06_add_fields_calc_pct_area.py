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

feature_classes = ["agesexrace_dis","econ_dis","education_dis","lingiso_dis","poverty_dis"]
data_path = "/processing/processing.gdb/intersect_dissolves_by_topic/"
#E:/SpiderOak/projects/hospitals/data/processing/processing.gdb/dissolve_geographies/agesexrace
stoptime = 0.5

the_fields = [
"HC01_VC01",
"HC01_VC03",
"HC01_VC04",
"HC01_VC18",
"HC01_VC25",
"HC01_VC26",
"HC01_VC28",
"HC01_VC29",
"HC01_VC30",
"HC01_VC31",
"HC01_VC32",
"HC01_VC55",
"HC01_VC56"
]

print "add agesexrace fields"

for thefields in the_fields:
	arcpy.AddField_management(fld+data_path+"agesexrace", thefields, "FLOAT")
	time.sleep(stoptime)

field_exps = [
"!agesexrace_HC01_VC01!*!pctorgarea!",
"!agesexrace_HC01_VC03!*!pctorgarea!",
"!agesexrace_HC01_VC04!*!pctorgarea!",
"!agesexrace_HC01_VC18!*!pctorgarea!",
"!agesexrace_HC01_VC25!*!pctorgarea!",
"!agesexrace_HC01_VC26!*!pctorgarea!",
"!agesexrace_HC01_VC28!*!pctorgarea!",
"!agesexrace_HC01_VC29!*!pctorgarea!",
"!agesexrace_HC01_VC30!*!pctorgarea!",
"!agesexrace_HC01_VC31!*!pctorgarea!",
"!agesexrace_HC01_VC32!*!pctorgarea!",
"!agesexrace_HC01_VC55!*!pctorgarea!",
"!agesexrace_HC01_VC56!*!pctorgarea!"
]

print "calc agesexrace fields"

for thefields, fieldexps in zip(the_fields, field_exps):
	arcpy.CalculateField_management(fld+data_path+"agesexrace", thefields, fieldexps, "PYTHON_9.3")
	time.sleep(stoptime)

the_fields = [
"HC01_VC02",
"HC01_VC03",
"HC01_VC08",
"HC01_VC09",
"HC01_VC25",
]

print "add econ fields"

for thefields in the_fields:
	arcpy.AddField_management(fld+data_path+"econ", thefields, "FLOAT")
	time.sleep(stoptime)

field_exps = [
"!econ_HC01_VC02!*!pctorgarea!",
"!econ_HC01_VC03!*!pctorgarea!",
"!econ_HC01_VC08!*!pctorgarea!",
"!econ_HC01_VC09!*!pctorgarea!",
"!econ_HC01_VC25!*!pctorgarea!"
]

print "calc agesexrace fields"

for thefields, fieldexps in zip(the_fields, field_exps):
	arcpy.CalculateField_management(fld+data_path+"econ", thefields, fieldexps, "PYTHON_9.3")
	time.sleep(stoptime)

the_fields = [
"HC01_VC09",
"HC01_VC10",
"HC01_VC11",
"HC01_VC12",
"HC01_VC13",
"HC01_VC14",
"HC01_VC15",
"HC01_VC16",
"HC01_VC17",
"HC01_VC18",
]

print "add edu fields"

for thefields in the_fields:
	arcpy.AddField_management(fld+data_path+"education", thefields, "FLOAT")
	time.sleep(stoptime)

field_exps = [
"!education_HC01_VC09!*!pctorgarea!",
"!education_HC01_VC10!*!pctorgarea!",
"!education_HC01_VC11!*!pctorgarea!",
"!education_HC01_VC12!*!pctorgarea!",
"!education_HC01_VC13!*!pctorgarea!",
"!education_HC01_VC14!*!pctorgarea!",
"!education_HC01_VC15!*!pctorgarea!",
"!education_HC01_VC16!*!pctorgarea!",
"!education_HC01_VC17!*!pctorgarea!",
"!education_HC01_VC18!*!pctorgarea!",
]

print "calc edu fields"

for thefields, fieldexps in zip(the_fields, field_exps):
	arcpy.CalculateField_management(fld+data_path+"education", thefields, fieldexps, "PYTHON_9.3")
	time.sleep(stoptime)

the_fields = [
"VD01",
"VD02",
"VD03",
"VD04",
"VD05",
"VD06",
"VD07",
"VD08",
"VD09",
"VD10",
"VD11",
"VD12",
"VD13",
"VD14",
]

print "add lingiso fields"

for thefields in the_fields:
	arcpy.AddField_management(fld+data_path+"lingiso", thefields, "FLOAT")
	time.sleep(stoptime)

field_exps = [
"!lingiso_VD01!*!pctorgarea!",
"!lingiso_VD02!*!pctorgarea!",
"!lingiso_VD03!*!pctorgarea!",
"!lingiso_VD04!*!pctorgarea!",
"!lingiso_VD05!*!pctorgarea!",
"!lingiso_VD06!*!pctorgarea!",
"!lingiso_VD07!*!pctorgarea!",
"!lingiso_VD08!*!pctorgarea!",
"!lingiso_VD09!*!pctorgarea!",
"!lingiso_VD10!*!pctorgarea!",
"!lingiso_VD11!*!pctorgarea!",
"!lingiso_VD12!*!pctorgarea!",
"!lingiso_VD13!*!pctorgarea!",
"!lingiso_VD14!*!pctorgarea!",
]

print "calc lingiso fields"

for thefields, fieldexps in zip(the_fields, field_exps):
	arcpy.CalculateField_management(fld+data_path+"lingiso", thefields, fieldexps, "PYTHON_9.3")
	time.sleep(stoptime)


the_fields = [
"HC02_VC01",
"HC03_VC01"
]

print "add poverty fields"

for thefields in the_fields:
	arcpy.AddField_management(fld+data_path+"poverty", thefields, "FLOAT")
	time.sleep(stoptime)

field_exps = [
"!poverty_HC02_VC01!*!pctorgarea!",
"!poverty_HC03_VC01!*!pctorgarea!"
]

print "calc poverty fields"

for thefields, fieldexps in zip(the_fields, field_exps):
	arcpy.CalculateField_management(fld+data_path+"poverty", thefields, fieldexps, "PYTHON_9.3")
	time.sleep(stoptime)


raw_input("Congrats! Processing has been completed effectively. Press any key to exit") 

