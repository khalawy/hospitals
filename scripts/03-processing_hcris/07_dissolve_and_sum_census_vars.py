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
data_path = "/processing/processing.gdb/intersect_dissolves_by_topic/"

print "dissolve interesected tracks to Provider number and uidpreint"
arcpy.Dissolve_management(fld+"/processing/processing.gdb/intersect_dissolves_by_topic/agesexrace",fld+"/processing/processing.gdb/dissolve_geographies/agesexrace_dis","prvdr_num;uidpreint","HC01_VC01 SUM;HC01_VC03 SUM;HC01_VC04 SUM;HC01_VC18 SUM;HC01_VC25 SUM;HC01_VC26 SUM;HC01_VC28 SUM;HC01_VC29 SUM;HC01_VC30 SUM;HC01_VC31 SUM;HC01_VC32 SUM;HC01_VC55 SUM;HC01_VC56 SUM","MULTI_PART","DISSOLVE_LINES")
arcpy.Dissolve_management(fld+"/processing/processing.gdb/intersect_dissolves_by_topic/econ",fld+"/processing/processing.gdb/dissolve_geographies/econ_dis","prvdr_num;uidpreint","HC01_VC02 SUM;HC01_VC03 SUM;HC01_VC08 SUM;HC01_VC09 SUM;HC01_VC25 SUM","MULTI_PART","DISSOLVE_LINES")
arcpy.Dissolve_management(fld+"/processing/processing.gdb/intersect_dissolves_by_topic/education",fld+"/processing/processing.gdb/dissolve_geographies/education_dis","prvdr_num;uidpreint","HC01_VC09 SUM;HC01_VC10 SUM;HC01_VC11 SUM;HC01_VC12 SUM;HC01_VC13 SUM;HC01_VC14 SUM;HC01_VC15 SUM;HC01_VC16 SUM;HC01_VC17 SUM;HC01_VC18 SUM","MULTI_PART","DISSOLVE_LINES")
print "3 of 5 done - only print memo!"
arcpy.Dissolve_management(fld+"/processing/processing.gdb/intersect_dissolves_by_topic/lingiso",fld+"/processing/processing.gdb/dissolve_geographies/lingiso_dis","prvdr_num;uidpreint","VD01 SUM;VD02 SUM;VD03 SUM;VD04 SUM;VD05 SUM;VD06 SUM;VD07 SUM;VD08 SUM;VD09 SUM;VD10 SUM;VD11 SUM;VD12 SUM;VD13 SUM;VD14 SUM","MULTI_PART","DISSOLVE_LINES")
arcpy.Dissolve_management(fld+"/processing/processing.gdb/intersect_dissolves_by_topic/poverty",fld+"/processing/processing.gdb/dissolve_geographies/poverty_dis","prvdr_num;uidpreint","HC02_VC01 SUM;HC03_VC01 SUM","MULTI_PART","DISSOLVE_LINES")




raw_input("Congrats! Processing has been completed effectively. Press any key to exit") 

