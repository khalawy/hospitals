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


featureclass = "/processing/processing.gdb/na_albers_equal_area_conic/points_b05mile_intersect_tracts_2000_dis"

feature_layer_name = ["view_agesexrace","view_econ","view_education","view_lingiso","view_poverty"]

tablefolder = "/processing/variables.gdb/"

table_name = ["agesexrace","econ","education","lingiso","poverty"]

out_path = fld+"/processing/processing.gdb/intersect_dissolves_by_topic"

print "go"

for featurelayername, tablename in zip(feature_layer_name, table_name):

	arcpy.MakeFeatureLayer_management(fld+featureclass,featurelayername)
	arcpy.AddJoin_management(featurelayername,"CTIDFP00",fld+tablefolder+tablename,"geoid","KEEP_ALL")
	arcpy.FeatureClassToFeatureClass_conversion (featurelayername, out_path, tablename)

	print "1 down"

#run with PYTHON.EXE 

raw_input("Congrats! Processing has been completed effectively. Press any key to exit") 

