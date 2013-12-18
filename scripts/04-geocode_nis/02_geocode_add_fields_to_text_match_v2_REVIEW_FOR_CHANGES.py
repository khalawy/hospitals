#Geocode using these settings:
#GeocodeAddresses V://projects/hospitals/data/input.gdb/hospitals_addr W://GIS/Data/Esri/Data_and_Maps_10-1/streetmap_na/data/Street_Addresses_US "Street Street VISIBLE NONE;City City VISIBLE NONE;State State VISIBLE NONE;ZIP ZIP VISIBLE NONE" V:\\projects\hospitals\data\input.gdb\hospitals_addr_geocode_1 STATIC
#manually reviewwd rematched


# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "nis_hospitals_geocode_1"
arcpy.AddField_management("nis_hospitals_geocode_1","addr_concate_str","TEXT","#","#","#","#","NULLABLE","NON_REQUIRED","#")

