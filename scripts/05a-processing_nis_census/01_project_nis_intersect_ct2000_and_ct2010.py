# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "nis_xy"
arcpy.MakeXYEventLayer_management("nis_xy","final_x","final_y","nis_xy_layer","GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433],METADATA['World',-180.0,-90.0,180.0,90.0,0.0,0.0174532925199433,0.0,1262]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision","#")

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "nis_xy_layer"
arcpy.Project_management("nis_xy_layer","W:/GIS/Projects/hospitals/data/processing_nis/nis.gdb/nis_xy_project","GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433],METADATA['North America - NAD83',167.65,14.93,-47.74,86.45,0.0,0.0174532925199433,0.0,1350]]","WGS_1984_(ITRF00)_To_NAD_1983","GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433],METADATA['World',-180.0,-90.0,180.0,90.0,0.0,0.0174532925199433,0.0,1262]]")

#census tract 2000 and 2010
arcpy.Intersect_analysis("W:/GIS/Projects/hospitals/data/input/census/census.gdb/tracts_2000 #;W:/GIS/Projects/hospitals/data/processing_nis/nis.gdb/nis_xy_project #","W:/GIS/Projects/hospitals/data/processing_nis/nis.gdb/nis_intersect_ct2000","ALL","#","INPUT")
arcpy.Intersect_analysis("W:/GIS/Projects/hospitals/data/input/census/census.gdb/tracts_2010 #;W:/GIS/Projects/hospitals/data/processing_nis/nis.gdb/nis_xy_project #","W:/GIS/Projects/hospitals/data/processing_nis/nis.gdb/nis_intersect_ct2010","ALL","#","INPUT")

#census county 2000 and 2010
arcpy.Intersect_analysis("W:/GIS/Projects/hospitals/data/input/census/census_2000_counties/tl_2008_us_county/tl_2008_us_county.shp #;W:/GIS/Projects/hospitals/data/processing_nis/nis.gdb/nis_xy_project #","W:/GIS/Projects/hospitals/data/processing_nis/nis.gdb/nis_intersect_co2000","ALL","#","INPUT")
arcpy.Intersect_analysis("W:/GIS/Projects/hospitals/data/input/census/census_2010_counties/County_2010Census_DP1.shp #;W:/GIS/Projects/hospitals/data/processing_nis/nis.gdb/nis_xy_project #","W:/GIS/Projects/hospitals/data/processing_nis/nis.gdb/nis_intersect_co2010","ALL","#","INPUT")


arcpy.Intersect_analysis("W:/GIS/Projects/hospitals/data/input/census/census.gdb/zcta_2000 #;W:/GIS/Projects/hospitals/data/processing_nis/nis.gdb/nis_xy_project #","W:/GIS/Projects/hospitals/data/processing_nis/nis.gdb/nis_intersect_zt2000","ALL","#","INPUT")