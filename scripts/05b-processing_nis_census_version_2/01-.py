import arcpy
#import os
#import errno
#import re, urllib, time, zipfile, os
from arcpy import env
env.overwriteOutput = True


project_path = 'W:/GIS/Projects/hospitals/'
processing_path = 'data/processing_nis/'
nisgdb = 'nis.gdb/'
nisdir = project_path + processing_path + nisgdb
ngeogs = project_path + processing_path + "/geogs.gdb/"

inxy = nisdir + 'nis_xy_project'

print 'project xy to albers'
arcpy.Project_management(inxy,inxy + "_albers","PROJCS['North_America_Albers_Equal_Area_Conic',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Albers'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-96.0],PARAMETER['Standard_Parallel_1',20.0],PARAMETER['Standard_Parallel_2',60.0],PARAMETER['Latitude_Of_Origin',40.0],UNIT['Meter',1.0]]","#","GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433],METADATA['North America - NAD83',167.65,14.93,-47.74,86.45,0.0,0.0174532925199433,0.0,1350]]")
print 'buffer xy 0.5 miles'
arcpy.Buffer_analysis(inxy + "_albers", ngeogs + "nis_buffer_0_5mile","0.5 Miles","FULL","ROUND","NONE","#")

print 'add and calc original tract area in sq. meters'
arcpy.AddField_management(project_path + "data/input/census/census.gdb/tracts_2000","origtractarea","DOUBLE")
arcpy.CalculateField_management(project_path + "data/input/census/census.gdb/tracts_2000","origtractarea","!shape.area@squaremeters!","PYTHON_9.3","#")
arcpy.AddField_management(project_path + "data/input/census/census.gdb/zcta_2000","origzctaarea","DOUBLE")
arcpy.CalculateField_management(project_path + "data/input/census/census.gdb/zcta_2000","origzctaarea","!shape.area@squaremeters!","PYTHON_9.3","#")


print 'intersect buffer with ct2000'
arcpy.Intersect_analysis(ngeogs + "nis_buffer_0_5mile;" + project_path + "data/input/census/census.gdb/tracts_2000",ngeogs + "nis_buffer_0_5mile_ct2000_int","ALL","#","INPUT")
arcpy.Intersect_analysis(ngeogs + "nis_buffer_0_5mile;" + project_path + "data/input/census/census.gdb/zcta_2000",ngeogs + "nis_buffer_0_5mile_zt2000_int","ALL","#","INPUT")

print 'add newtractarea and pcttract area fields'
arcpy.AddField_management(ngeogs + "nis_buffer_0_5mile_ct2000_int","newtractarea","DOUBLE","#","#","#","#","NULLABLE","NON_REQUIRED","#")
arcpy.AddField_management(ngeogs + "nis_buffer_0_5mile_ct2000_int","pcttractarea","FLOAT","#","#","#","#","NULLABLE","NON_REQUIRED","#")
arcpy.AddField_management(ngeogs + "nis_buffer_0_5mile_zt2000_int","newzctaarea","DOUBLE","#","#","#","#","NULLABLE","NON_REQUIRED","#")
arcpy.AddField_management(ngeogs + "nis_buffer_0_5mile_zt2000_int","pctzctaarea","FLOAT","#","#","#","#","NULLABLE","NON_REQUIRED","#")
   
print 'calc newtractarea and pcttract area fields'     
arcpy.CalculateField_management(ngeogs + "nis_buffer_0_5mile_ct2000_int","newtractarea","!shape.area@squaremeters!","PYTHON","#")
arcpy.CalculateField_management(ngeogs + "nis_buffer_0_5mile_ct2000_int","pcttractarea","!newtractarea! / !origtractarea! ","PYTHON","#")
arcpy.CalculateField_management(ngeogs + "nis_buffer_0_5mile_zt2000_int","newzctaarea","!shape.area@squaremeters!","PYTHON","#")
arcpy.CalculateField_management(ngeogs + "nis_buffer_0_5mile_zt2000_int","pctzctaarea","!newzctaarea! / !origzctaarea! ","PYTHON","#")



