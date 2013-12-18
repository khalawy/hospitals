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

theme_list = ["agesexrace","econ","education","lingiso","poverty"]

geog_list = ["cny","hrb","trt"]

for themelist in theme_list:

	for geoglist in geog_list:

		arcpy.TableToTable_conversion(fld+"/output/geographies.gdb/"+geoglist+"/"+geoglist+"_"+themelist, fld+"/output/tables/dbf", geoglist+"_"+themelist+".dbf")


arcpy.TableToTable_conversion(fld+"/input.gdb/hospitals",fld+"/output/tables/dbf","hospitals.dbf")


#SEE #13 for health insurance data by county to DBF