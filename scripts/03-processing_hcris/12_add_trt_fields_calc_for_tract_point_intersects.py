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

feature_classes = ["agesexrace_county_cny","econ_county_cny","education_county_cny","lingiso_county_cny","poverty_county_cny"]
data_path = "/processing/processing.gdb/county_int_geographies/"

stoptime = 0.5

the_fields = [
"cnycntpop",
"cnycnt65o",
"cnypct65o",
"cnycntblk",
"cnypctblk",
"cnycnthis",
"cnypcthis"
]

print "add agesexrace_cny fields"

for thefields in the_fields:
	arcpy.AddField_management(fld+data_path+"agesexrace_county_cny", thefields, "FLOAT")
	time.sleep(stoptime)

field_exps = [
"!agesexrace_county_HC01_VC01!",
"!agesexrace_county_HC01_VC25!+!agesexrace_county_HC01_VC26!",
"!cnycnt65o!/!cnycntpop!",
"!agesexrace_county_HC01_VC30!",
"!cnycntblk!/!cnycntpop!",
"!agesexrace_county_HC01_VC56!",
"!cnycnthis!/!cnycntpop!"
]

print "calc agesexrace_cny fields"

for thefields, fieldexps in zip(the_fields, field_exps):
	arcpy.CalculateField_management(fld+data_path+"agesexrace_county_cny", thefields, fieldexps, "PYTHON_9.3")
	time.sleep(stoptime)
#--------------------------
the_fields = [
"cnycnt16o",
"cnycntune",
"cnypctune"
]

print "add econ_cny fields"

for thefields in the_fields:
	arcpy.AddField_management(fld+data_path+"econ_county_cny", thefields, "FLOAT")
	time.sleep(stoptime)

field_exps = [
"!econ_county_HC01_VC02!",
"!econ_county_HC01_VC09!",
"!cnycntune!/!cnycnt16o!"
]

print "calc econ_cny fields"

for thefields, fieldexps in zip(the_fields, field_exps):
	arcpy.CalculateField_management(fld+data_path+"econ_county_cny", thefields, fieldexps, "PYTHON_9.3")
	time.sleep(stoptime)
#-----------------------
the_fields = [
"cnycnt25o",
"cnycntlhs",
"cnypctlhs"
]

print "add education_cny fields"

for thefields in the_fields:
	arcpy.AddField_management(fld+data_path+"education_county_cny", thefields, "FLOAT")
	time.sleep(stoptime)

field_exps = [
"!education_county_HC01_VC09!",
"!education_county_HC01_VC10!+!education_county_HC01_VC11!",
"!cnycntlhs!/!cnycnt25o!"
]

print "calc education_cny fields"

for thefields, fieldexps in zip(the_fields, field_exps):
	arcpy.CalculateField_management(fld+data_path+"education_county_cny", thefields, fieldexps, "PYTHON_9.3")
	time.sleep(stoptime)
#-----------------------
the_fields = [
"cnycntlan",
"cnycntlin",
"cnypctlin"
]

print "add lingiso_cny fields"

for thefields in the_fields:
	arcpy.AddField_management(fld+data_path+"lingiso_county_cny", thefields, "FLOAT")
	time.sleep(stoptime)

field_exps = [
"!lingiso_county_VD01!",
"!lingiso_county_VD04!+ !lingiso_county_VD07!+ !lingiso_county_VD10!+ !lingiso_county_VD13!",
"!cnycntlin!/!cnycntlan!"
]

print "calc lingiso_cny fields"

for thefields, fieldexps in zip(the_fields, field_exps):
	arcpy.CalculateField_management(fld+data_path+"lingiso_county_cny", thefields, fieldexps, "PYTHON_9.3")
	time.sleep(stoptime)
#-----------------------
the_fields = [
"cnycntppv",
"cnycntpov",
"cnypctpov"
]

print "add poverty_cny fields"

for thefields in the_fields:
	arcpy.AddField_management(fld+data_path+"poverty_county_cny", thefields, "FLOAT")
	time.sleep(stoptime)

field_exps = [
"!poverty_county_HC02_VC01!",
"!poverty_county_HC03_VC01!",
"!cnycntpov!/!cnycntppv!"
]
#"!cnycntpov! / !cnycntppv!","PYTHON_9.3","#")
#"!poverty_HC03_VC01!/!poverty_HC02_VC01!","PYTHON_9.3","#")


print "calc poverty_cny fields"

for thefields, fieldexps in zip(the_fields, field_exps):
	arcpy.CalculateField_management(fld+data_path+"poverty_county_cny", thefields, fieldexps, "PYTHON_9.3")
	time.sleep(stoptime)



raw_input("Congrats! Processing has been completed effectively. Press any key to exit") 


# the_fields = [
# ]

# print "add ______ fields"

# for thefields in the_fields:
# 	arcpy.AddField_management(fld+data_path+"_______", thefields, "FLOAT")
# 	time.sleep(stoptime)

# field_exps = [
# ]

# print "calc _______ fields"

# for thefields, fieldexps in zip(the_fields, field_exps):
# 	arcpy.CalculateField_management(fld+data_path+"_______", thefields, fieldexps, "PYTHON_9.3")
# 	time.sleep(stoptime)