import arcpy, time, datetime, csv, sys, traceback
from arcpy import env
env.overwriteOutput = True

## Check out any necessary licenses
#from arcpy.sa import *
#arcpy.CheckOutExtension("Network")
#arcpy.CheckOutExtension("Spatial")

## -----------------------------------------------------------------------------------------------------------------
## PATH VARIABLES
## -----------------------------------------------------------------------------------------------------------------

arcpy.ImportToolbox('C:\Program Files (x86)\DataEast\XTools Pro\Toolbox\XTOOLS PRO.tbx')

arcpy.XToolsPro_Table2Text("W:/GIS/Projects/hospitals/data/processing_nis/nis.gdb/nis_xy_project","Match_addr;ARC_Street;ARC_City;ARC_State;ARC_ZIP;ID;NAME;STATE;YEAR;ADDRESS;CITY;FIPS_STATE;ZIP;ST;ZIPcode;nisuid;edit;final_match_address;hcris_join;final_x;final_y;hcris_join_num","W:/GIS/Projects/hospitals/data/processing_nis/nis_census_tables/nisuid_orig_nis_data.csv")


# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "nis_intersect_ct2000"
arcpy.XToolsPro_Table2Text("nis_intersect_ct2000","CTIDFP00;nisuid","W:/GIS/Projects/hospitals/data/processing_nis/nis_census_tables/nisuid_ct2000.csv")

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "nis_intersect_ct2010"
arcpy.XToolsPro_Table2Text("nis_intersect_ct2010","GEOID10;nisuid","W:/GIS/Projects/hospitals/data/processing_nis/nis_census_tables/nisuid_ct2010.csv")