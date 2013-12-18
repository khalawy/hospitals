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


featureclass = "/processing/processing.gdb/na_albers_equal_area_conic/points_intersect_tract"

feature_layer_name = ["view_agesexrace_trt","view_econ_trt","view_education_trt","view_lingiso_trt","view_poverty_trt"]

tablefolder = "/processing/variables.gdb/"

table_name = ["agesexrace","econ","education","lingiso","poverty"]

out_path = fld+"/processing/processing.gdb/tract_int_geographies"

for featurelayername, tablename in zip(feature_layer_name, table_name):
	print "Getting going for " + featurelayername
	arcpy.MakeFeatureLayer_management(fld+featureclass,featurelayername)
	arcpy.AddJoin_management(featurelayername,"CTIDFP00",fld+tablefolder+tablename,"geoid","KEEP_ALL")
	arcpy.FeatureClassToFeatureClass_conversion (featurelayername, out_path, tablename+"_trt")

raw_input("Congrats! Processing has been completed effectively. Press any key to exit") 


