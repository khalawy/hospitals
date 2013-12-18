import arcpy, time, datetime, csv, sys, traceback
from arcpy import env
env.overwriteOutput = True

#MacBook Pro-Windows 7
drive_path = "V:/"
#dropbox_path = "W:/"

#008
#drive_path = "E:/SpiderOak/"
#dropbox_path = "W:/"

fl = drive_path + "projects/hospitals/"
fld = fl + "data"

print "convert input nad 83 tracts 2000 file and bring into na albers equal area conic"
arcpy.FeatureClassToFeatureClass_conversion(fld+"/input/census/census.gdb/tracts_2000",fld+"/processing/processing.gdb/na_albers_equal_area_conic","tracts_2000")
print "convert input nad 83 tracts 2010 file and bring into na albers equal area conic"
arcpy.FeatureClassToFeatureClass_conversion(fld+"/input/census/census.gdb/tracts_2010",fld+"/processing/processing.gdb/na_albers_equal_area_conic","tracts_2010")
print "convert input nad 83 water 2010 file and bring into na albers equal area conic - areawater 2010 easier for retrieval than 2000"
arcpy.FeatureClassToFeatureClass_conversion(fld+"/input/census/areawater.gdb/areawater_2010",fld+"/processing/processing.gdb/na_albers_equal_area_conic","areawater")

print "erase water from tracts"
#arcpy.Erase_analysis(fld+"/processing/processing.gdb/na_albers_equal_area_conic/tracts_2000",fld+"/processing/processing.gdb/na_albers_equal_area_conic/areawater",fld+"/processing/processing.gdb/na_albers_equal_area_conic/tracts_2000_e_water")
#arcpy.Erase_analysis(fld+"/processing/processing.gdb/na_albers_equal_area_conic/tracts_2010",fld+"/processing/processing.gdb/na_albers_equal_area_conic/areawater",fld+"/processing/processing.gdb/na_albers_equal_area_conic/tracts_2010_e_water")

print "add sq meters field to census"
arcpy.AddField_management(fld+"/processing/processing.gdb/na_albers_equal_area_conic/tracts_2000_e_water","tractareasqmeters","FLOAT","#","#","#","#","NULLABLE","NON_REQUIRED","#")
arcpy.AddField_management(fld+"/processing/processing.gdb/na_albers_equal_area_conic/tracts_2010_e_water","tractareasqmeters","FLOAT","#","#","#","#","NULLABLE","NON_REQUIRED","#")

print "calc tract sq meters"
arcpy.CalculateField_management(fld+"/processing/processing.gdb/na_albers_equal_area_conic/tracts_2000_e_water","tractareasqmeters","!shape.area@squaremeters!","PYTHON_9.3","#")
arcpy.CalculateField_management(fld+"/processing/processing.gdb/na_albers_equal_area_conic/tracts_2010_e_water","tractareasqmeters","!shape.area@squaremeters!","PYTHON_9.3","#")

print "add uid-preint field to points"
arcpy.AddField_management(fld+"/processing/processing.gdb/na_albers_equal_area_conic/points","uidpreint","DOUBLE","#","#","#","#","NULLABLE","NON_REQUIRED","#")

print "calc uid-preint field"
arcpy.CalculateField_management(fld+"/processing/processing.gdb/na_albers_equal_area_conic/points","uidpreint","!OBJECTID!","PYTHON_9.3","#")
 
print "buffer points"
arcpy.Buffer_analysis(fld+"/processing/processing.gdb/na_albers_equal_area_conic/points",fld+"/processing/processing.gdb/na_albers_equal_area_conic/points_b05mile","0.5 Miles","FULL","ROUND","NONE","#")

print "add sq meters field to buffer"
arcpy.AddField_management(fld+"/processing/processing.gdb/na_albers_equal_area_conic/points_b05mile","bufferareasqmeters","FLOAT","#","#","#","#","NULLABLE","NON_REQUIRED","#")

print "calc buffer sq meters"
arcpy.CalculateField_management(fld+"/processing/processing.gdb/na_albers_equal_area_conic/points_b05mile","bufferareasqmeters","!shape.area@squaremeters!","PYTHON_9.3","#")

print "intersect points to get tract"
inFeatures = [fld+"/processing/processing.gdb/na_albers_equal_area_conic/points", fld+"/processing/processing.gdb/na_albers_equal_area_conic/tracts_2000"]
arcpy.Intersect_analysis(inFeatures,fld+"/processing/processing.gdb/na_albers_equal_area_conic/points_intersect_tract","ALL","#","INPUT")

print "intersect buffers and tracts"
inFeatures = [fld+"/processing/processing.gdb/na_albers_equal_area_conic/points_b05mile", fld+"/processing/processing.gdb/na_albers_equal_area_conic/tracts_2000_e_water"]
arcpy.Intersect_analysis(inFeatures,fld+"/processing/processing.gdb/na_albers_equal_area_conic/points_b05mile_intersect_tracts_2000","ALL","#","INPUT")
inFeatures = [fld+"/processing/processing.gdb/na_albers_equal_area_conic/points_b05mile", fld+"/processing/processing.gdb/na_albers_equal_area_conic/tracts_2010_e_water"]
arcpy.Intersect_analysis(inFeatures,fld+"/processing/processing.gdb/na_albers_equal_area_conic/points_b05mile_intersect_tracts_2010","ALL","#","INPUT")

print "dissolve by unique id and tract id for 2000 and 2010"
dissolve_on = "Provider_Number;uidpreint;bufferareasqmeters;CTIDFP00;tractareasqmeters"
arcpy.Dissolve_management(fld+"/processing/processing.gdb/na_albers_equal_area_conic/points_b05mile_intersect_tracts_2000",fld+"/processing/processing.gdb/na_albers_equal_area_conic/points_b05mile_intersect_tracts_2000_dis",dissolve_on,"#","MULTI_PART","DISSOLVE_LINES")
dissolve_on = "Provider_Number;uidpreint;bufferareasqmeters;GEOID10;tractareasqmeters"
arcpy.Dissolve_management(fld+"/processing/processing.gdb/na_albers_equal_area_conic/points_b05mile_intersect_tracts_2010",fld+"/processing/processing.gdb/na_albers_equal_area_conic/points_b05mile_intersect_tracts_2010_dis",dissolve_on,"#","MULTI_PART","DISSOLVE_LINES")





#these are done to save a lot of space
print "delete input intermed features"
arcpy.Delete_management(fld+"/processing/processing.gdb/na_albers_equal_area_conic/tracts_2000")
arcpy.Delete_management(fld+"/processing/processing.gdb/na_albers_equal_area_conic/tracts_2010")
arcpy.Delete_management(fld+"/processing/processing.gdb/na_albers_equal_area_conic/areawater")

#raw_input("Congrats! Processing has been completed effectively. Press any key to exit") 