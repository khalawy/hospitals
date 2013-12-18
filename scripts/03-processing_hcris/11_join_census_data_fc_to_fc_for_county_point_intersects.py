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


featureclass = "/processing/processing.gdb/na_albers_equal_area_conic/points_intersect_county"

feature_layer_name = ["view_agesexrace_cny","view_econ_cny","view_education_cny","view_lingiso_cny","view_poverty_cny"]

tablefolder = "/processing/variables.gdb/"

table_name = ["agesexrace_county","econ_county","education_county","lingiso_county","poverty_county"]

out_path = fld+"/processing/processing.gdb/county_int_geographies"

for featurelayername, tablename in zip(feature_layer_name, table_name):
	print "Getting going for " + featurelayername
	arcpy.MakeFeatureLayer_management(fld+featureclass,featurelayername)
	arcpy.AddJoin_management(featurelayername,"CNTYIDFP",fld+tablefolder+tablename,"county","KEEP_ALL")
	arcpy.FeatureClassToFeatureClass_conversion (featurelayername, out_path, tablename+"_cny")

raw_input("Congrats! Processing has been completed effectively. Press any key to exit") 
