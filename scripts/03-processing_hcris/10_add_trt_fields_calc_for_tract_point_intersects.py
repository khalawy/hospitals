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

feature_classes = ["agesexrace_trt","econ_trt","education_trt","lingiso_trt","poverty_trt"]
data_path = "/processing/processing.gdb/tract_int_geographies/"

stoptime = 0.5

the_fields = [
"trtcntpop",
"trtcnt65o",
"trtpct65o",
"trtcntblk",
"trtpctblk",
"trtcnthis",
"trtpcthis"
]

print "add agesexrace_trt fields"

for thefields in the_fields:
	arcpy.AddField_management(fld+data_path+"agesexrace_trt", thefields, "FLOAT")
	time.sleep(stoptime)

field_exps = [
"!agesexrace_HC01_VC01!",
"!agesexrace_HC01_VC25!+!agesexrace_HC01_VC26!",
"!trtcnt65o!/!trtcntpop!",
"!agesexrace_HC01_VC30!",
"!trtcntblk!/!trtcntpop!",
"!agesexrace_HC01_VC56!",
"!trtcnthis!/!trtcntpop!"
]

print "calc agesexrace_trt fields"

for thefields, fieldexps in zip(the_fields, field_exps):
	arcpy.CalculateField_management(fld+data_path+"agesexrace_trt", thefields, fieldexps, "PYTHON_9.3")
	time.sleep(stoptime)
#--------------------------
the_fields = [
"trtcnt16o",
"trtcntune",
"trtpctune"
]

print "add econ_trt fields"

for thefields in the_fields:
	arcpy.AddField_management(fld+data_path+"econ_trt", thefields, "FLOAT")
	time.sleep(stoptime)

field_exps = [
"!econ_HC01_VC02!",
"!econ_HC01_VC09!",
"!trtcntune!/!trtcnt16o!"
]

print "calc econ_trt fields"

for thefields, fieldexps in zip(the_fields, field_exps):
	arcpy.CalculateField_management(fld+data_path+"econ_trt", thefields, fieldexps, "PYTHON_9.3")
	time.sleep(stoptime)
#-----------------------
the_fields = [
"trtcnt25o",
"trtcntlhs",
"trtpctlhs"
]

print "add education_trt fields"

for thefields in the_fields:
	arcpy.AddField_management(fld+data_path+"education_trt", thefields, "FLOAT")
	time.sleep(stoptime)

field_exps = [
"!education_HC01_VC09!",
"!education_HC01_VC10!+!education_HC01_VC11!",
"!trtcntlhs!/!trtcnt25o!"
]

print "calc education_trt fields"

for thefields, fieldexps in zip(the_fields, field_exps):
	arcpy.CalculateField_management(fld+data_path+"education_trt", thefields, fieldexps, "PYTHON_9.3")
	time.sleep(stoptime)
#-----------------------
the_fields = [
"trtcntlan",
"trtcntlin",
"trtpctlin"
]

print "add lingiso_trt fields"

for thefields in the_fields:
	arcpy.AddField_management(fld+data_path+"lingiso_trt", thefields, "FLOAT")
	time.sleep(stoptime)

field_exps = [
"!lingiso_VD01!",
"!lingiso_VD04!+ !lingiso_VD07!+ !lingiso_VD10!+ !lingiso_VD13!",
"!trtcntlin!/!trtcntlan!"
]

print "calc lingiso_trt fields"

for thefields, fieldexps in zip(the_fields, field_exps):
	arcpy.CalculateField_management(fld+data_path+"lingiso_trt", thefields, fieldexps, "PYTHON_9.3")
	time.sleep(stoptime)
#-----------------------
the_fields = [
"trtcntppv",
"trtcntpov",
"trtpctpov"
]

print "add poverty_trt fields"

for thefields in the_fields:
	arcpy.AddField_management(fld+data_path+"poverty_trt", thefields, "FLOAT")
	time.sleep(stoptime)

field_exps = [
"!poverty_HC02_VC01!",
"!poverty_HC03_VC01!",
"!trtcntpov!/!trtcntppv!"
]
#"!trtcntpov! / !trtcntppv!","PYTHON_9.3","#")
#"!poverty_HC03_VC01!/!poverty_HC02_VC01!","PYTHON_9.3","#")


print "calc poverty_trt fields"

for thefields, fieldexps in zip(the_fields, field_exps):
	arcpy.CalculateField_management(fld+data_path+"poverty_trt", thefields, fieldexps, "PYTHON_9.3")
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