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

feature_classes = ["agesexrace","econ","education","lingiso","poverty"]
data_path = "/processing/processing.gdb/dissolve_geographies/"

stoptime = 0.5

the_fields = [
"hrbcntpop",
"hrbcnt65o",
"hrbpct65o",
"hrbcntblk",
"hrbpctblk",
"hrbcnthis",
"hrbpcthis"
]

print "add agesexrace_dis fields"

for thefields in the_fields:
	arcpy.AddField_management(fld+data_path+"agesexrace_dis", thefields, "FLOAT")
	time.sleep(stoptime)

field_exps = [
"!SUM_HC01_VC01!",
"!SUM_HC01_VC25!+!SUM_HC01_VC26!",
"(!SUM_HC01_VC25!+!SUM_HC01_VC26!)/!SUM_HC01_VC01!",
"!SUM_HC01_VC30!",
"!SUM_HC01_VC30!/!SUM_HC01_VC01!",
"!SUM_HC01_VC56!",
"!SUM_HC01_VC56!/!SUM_HC01_VC01!",
]

print "calc agesexrace_dis fields"

for thefields, fieldexps in zip(the_fields, field_exps):
	arcpy.CalculateField_management(fld+data_path+"agesexrace_dis", thefields, fieldexps, "PYTHON_9.3")
	time.sleep(stoptime)
#--------------------------
the_fields = [
"hrbcnt16o",
"hrbcntune",
"hrbpctune"
]

print "add econ_dis fields"

for thefields in the_fields:
	arcpy.AddField_management(fld+data_path+"econ_dis", thefields, "FLOAT")
	time.sleep(stoptime)

field_exps = [
"!SUM_HC01_VC02!",
"!SUM_HC01_VC09!",
"!SUM_HC01_VC09!/!SUM_HC01_VC02!"
]

print "calc econ_dis fields"

for thefields, fieldexps in zip(the_fields, field_exps):
	arcpy.CalculateField_management(fld+data_path+"econ_dis", thefields, fieldexps, "PYTHON_9.3")
	time.sleep(stoptime)
#-----------------------
the_fields = [
"hrbcnt25o",
"hrbcntlhs",
"hrbpctlhs"
]

print "add education_dis fields"

for thefields in the_fields:
	arcpy.AddField_management(fld+data_path+"education_dis", thefields, "FLOAT")
	time.sleep(stoptime)

field_exps = [
"!SUM_HC01_VC09!",
"!SUM_HC01_VC10!+!SUM_HC01_VC11!",
"(!SUM_HC01_VC10!+!SUM_HC01_VC11!)/!SUM_HC01_VC09!"
]

print "calc education_dis fields"

for thefields, fieldexps in zip(the_fields, field_exps):
	arcpy.CalculateField_management(fld+data_path+"education_dis", thefields, fieldexps, "PYTHON_9.3")
	time.sleep(stoptime)
#-----------------------
the_fields = [
"hrbcntlan",
"hrbcntlin",
"hrbpctlin"
]

print "add lingiso_dis fields"

for thefields in the_fields:
	arcpy.AddField_management(fld+data_path+"lingiso_dis", thefields, "FLOAT")
	time.sleep(stoptime)

field_exps = [
"!SUM_VD01!",
"!SUM_VD04!+ !SUM_VD07!+ !SUM_VD10!+ !SUM_VD13!",
"(!SUM_VD04!+ !SUM_VD07!+ !SUM_VD10!+ !SUM_VD13!)/!SUM_VD01!"
]

print "calc lingiso_dis fields"

for thefields, fieldexps in zip(the_fields, field_exps):
	arcpy.CalculateField_management(fld+data_path+"lingiso_dis", thefields, fieldexps, "PYTHON_9.3")
	time.sleep(stoptime)
#-----------------------
the_fields = [
"hrbcntppv",
"hrbcntpov",
"hrbpctpov"
]

print "add poverty_dis fields"

for thefields in the_fields:
	arcpy.AddField_management(fld+data_path+"poverty_dis", thefields, "FLOAT")
	time.sleep(stoptime)

field_exps = [
"!SUM_HC02_VC01!",
"!SUM_HC03_VC01!",
"!SUM_HC03_VC01!/!SUM_HC02_VC01!"
]

print "calc poverty_dis fields"

for thefields, fieldexps in zip(the_fields, field_exps):
	arcpy.CalculateField_management(fld+data_path+"poverty_dis", thefields, fieldexps, "PYTHON_9.3")
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