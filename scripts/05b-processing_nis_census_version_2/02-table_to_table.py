arcpy.TableToTable_conversion("W:/GIS/Projects/hospitals/data/processing_nis/nis.gdb/nis_intersect_co2000","W:/GIS/Projects/hospitals/data/processing_nis/variables/county.gdb","nis_co2000_nest","#","""CNTYIDFP "CNTYIDFP" true true false 5 Text 0 0 ,First,#,W:/GIS/Projects/hospitals/data/processing_nis/nis.gdb/nis_intersect_co2000,CNTYIDFP,-1,-1;nisuid "nisuid" true true false 4 Long 0 0 ,First,#,W:/GIS/Projects/hospitals/data/processing_nis/nis.gdb/nis_intersect_co2000,nisuid,-1,-1""","#")
arcpy.TableToTable_conversion("W:/GIS/Projects/hospitals/data/processing_nis/nis.gdb/nis_intersect_co2010","W:/GIS/Projects/hospitals/data/processing_nis/variables/county.gdb","nis_co2010_nest","#","""GEOID10 "GEOID10" true true false 5 Text 0 0 ,First,#,W:/GIS/Projects/hospitals/data/processing_nis/nis.gdb/nis_intersect_co2010,GEOID10,-1,-1;nisuid "nisuid" true true false 4 Long 0 0 ,First,#,W:/GIS/Projects/hospitals/data/processing_nis/nis.gdb/nis_intersect_co2010,nisuid,-1,-1""","#")
arcpy.TableToTable_conversion("W:/GIS/Projects/hospitals/data/processing_nis/nis.gdb/nis_intersect_ct2000","W:/GIS/Projects/hospitals/data/processing_nis/variables/tract.gdb","nis_ct2000_nest","#","""CTIDFP00 "CTIDFP00" true true false 11 Text 0 0 ,First,#,W:/GIS/Projects/hospitals/data/processing_nis/nis.gdb/nis_intersect_ct2000,CTIDFP00,-1,-1;nisuid "nisuid" true true false 4 Long 0 0 ,First,#,W:/GIS/Projects/hospitals/data/processing_nis/nis.gdb/nis_intersect_ct2000,nisuid,-1,-1""","#")
arcpy.TableToTable_conversion("W:/GIS/Projects/hospitals/data/processing_nis/nis.gdb/nis_intersect_ct2010","W:/GIS/Projects/hospitals/data/processing_nis/variables/tract.gdb","nis_ct2010_nest","#","""GEOID10 "GEOID10" true true false 11 Text 0 0 ,First,#,W:/GIS/Projects/hospitals/data/processing_nis/nis.gdb/nis_intersect_ct2010,GEOID10,-1,-1;nisuid "nisuid" true true false 4 Long 0 0 ,First,#,W:/GIS/Projects/hospitals/data/processing_nis/nis.gdb/nis_intersect_ct2010,nisuid,-1,-1""","#")
arcpy.TableToTable_conversion("W:/GIS/Projects/hospitals/data/processing_nis/nis.gdb/nis_intersect_zt2000","W:/GIS/Projects/hospitals/data/processing_nis/variables/zcta.gdb","niz_zt2000_nest","#","""ZCTA5CE00 "ZCTA5CE00" true true false 5 Text 0 0 ,First,#,W:/GIS/Projects/hospitals/data/processing_nis/nis.gdb/nis_intersect_zt2000,ZCTA5CE00,-1,-1;nisuid "nisuid" true true false 4 Long 0 0 ,First,#,W:/GIS/Projects/hospitals/data/processing_nis/nis.gdb/nis_intersect_zt2000,nisuid,-1,-1""","#")

arcpy.TableToTable_conversion("W:/GIS/Projects/hospitals/data/processing_nis/geogs.gdb/nis_buffer_0_5mile_ct2000_int","W:/GIS/Projects/hospitals/data/processing_nis/variables/tract.gdb","nis_ct2000_bint","#","""nisuid "nisuid" true true false 4 Long 0 0 ,First,#,W:/GIS/Projects/hospitals/data/processing_nis/geogs.gdb/nis_buffer_0_5mile_ct2000_int,nisuid,-1,-1;CTIDFP00 "CTIDFP00" true true false 11 Text 0 0 ,First,#,W:/GIS/Projects/hospitals/data/processing_nis/geogs.gdb/nis_buffer_0_5mile_ct2000_int,CTIDFP00,-1,-1;origtractarea "origtractarea" true true false 8 Double 0 0 ,First,#,W:/GIS/Projects/hospitals/data/processing_nis/geogs.gdb/nis_buffer_0_5mile_ct2000_int,origtractarea,-1,-1;newtractarea "newtractarea" true true false 8 Double 0 0 ,First,#,W:/GIS/Projects/hospitals/data/processing_nis/geogs.gdb/nis_buffer_0_5mile_ct2000_int,newtractarea,-1,-1;pcttractarea "pcttractarea" true true false 4 Float 0 0 ,First,#,W:/GIS/Projects/hospitals/data/processing_nis/geogs.gdb/nis_buffer_0_5mile_ct2000_int,pcttractarea,-1,-1""","#")
arcpy.TableToTable_conversion("W:/GIS/Projects/hospitals/data/processing_nis/geogs.gdb/nis_buffer_0_5mile_ct2010_int","W:/GIS/Projects/hospitals/data/processing_nis/variables/tract.gdb","nis_ct2010_bint","#","""nisuid "nisuid" true true false 4 Long 0 0 ,First,#,W:/GIS/Projects/hospitals/data/processing_nis/geogs.gdb/nis_buffer_0_5mile_ct2010_int,nisuid,-1,-1;GEOID10 "GEOID10" true true false 11 Text 0 0 ,First,#,W:/GIS/Projects/hospitals/data/processing_nis/geogs.gdb/nis_buffer_0_5mile_ct2010_int,GEOID10,-1,-1;origtractarea "origtractarea" true true false 8 Double 0 0 ,First,#,W:/GIS/Projects/hospitals/data/processing_nis/geogs.gdb/nis_buffer_0_5mile_ct2010_int,origtractarea,-1,-1;newtractarea "newtractarea" true true false 8 Double 0 0 ,First,#,W:/GIS/Projects/hospitals/data/processing_nis/geogs.gdb/nis_buffer_0_5mile_ct2010_int,newtractarea,-1,-1;pcttractarea "pcttractarea" true true false 4 Float 0 0 ,First,#,W:/GIS/Projects/hospitals/data/processing_nis/geogs.gdb/nis_buffer_0_5mile_ct2010_int,pcttractarea,-1,-1""","#")
arcpy.TableToTable_conversion("W:/GIS/Projects/hospitals/data/processing_nis/geogs.gdb/nis_buffer_0_5mile_zt2000_int","W:/GIS/Projects/hospitals/data/processing_nis/variables/zcta.gdb","nis_zt2000_bint","#","""nisuid "nisuid" true true false 4 Long 0 0 ,First,#,W:/GIS/Projects/hospitals/data/processing_nis/geogs.gdb/nis_buffer_0_5mile_zt2000_int,nisuid,-1,-1;ZCTA5CE00 "ZCTA5CE00" true true false 5 Text 0 0 ,First,#,W:/GIS/Projects/hospitals/data/processing_nis/geogs.gdb/nis_buffer_0_5mile_zt2000_int,ZCTA5CE00,-1,-1;origzctaarea "origzctaarea" true true false 8 Double 0 0 ,First,#,W:/GIS/Projects/hospitals/data/processing_nis/geogs.gdb/nis_buffer_0_5mile_zt2000_int,origzctaarea,-1,-1;newzctaarea "newzctaarea" true true false 8 Double 0 0 ,First,#,W:/GIS/Projects/hospitals/data/processing_nis/geogs.gdb/nis_buffer_0_5mile_zt2000_int,newzctaarea,-1,-1;pctzctaarea "pctzctaarea" true true false 4 Float 0 0 ,First,#,W:/GIS/Projects/hospitals/data/processing_nis/geogs.gdb/nis_buffer_0_5mile_zt2000_int,pctzctaarea,-1,-1""","#")
