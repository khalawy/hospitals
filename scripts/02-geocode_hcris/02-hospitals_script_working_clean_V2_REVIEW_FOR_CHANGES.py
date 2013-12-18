import arcpy

#MacBook Pro-Windows 7

drive_path = "V:/"
drive_path = "E:/"
dropbox_path = "W:/"

#Rundle-008

#Static
project_folder = "/projects/hospitals"
proj = drive_path+project_folder
datafold = proj + "/data"
procfold = datafold + "/processing"
inputgdb = proj + "/data/input.gdb"

hosp_csv = proj + "/data/_original/hcris/hospitals_hcris.csv"
hosp_tbl = proj + "/data/input.gdb/hospitals"
hospaddr = proj + "/data/input.gdb/hospitals_addr"
hospgeo1 = proj + "/data/input.gdb/hospitals_addr_geocode_1"
hospgeo1nis = proj + "/data/input.gdb/nis_addr_geocode_1"
hospgeo1_sort = proj + "/data/input.gdb/hospitals_addr_geocode_1_sort"
hospgeo1_stex = proj + "/data/input.gdb/hospitals_addr_geocode_1_sort_export"
hospgeo1_semi = proj + "/data/input.gdb/hospitals_addr_geocode_1_sort_export_missed"
hospprvd = proj + "/data/input.gdb/hospitals_uniqprvd"

#Geocoders
geocoder_10_1 = dropbox_path + "/GIS/Data/Esri/Data_and_Maps_10-1/streetmap_na/data/Street_Addresses_US"
#geocoder_biza


# Expresssions

#calc "addr_concate_str_dup" field
dup_expression_1 = "isDuplicate(!addr_concate_str!)"
dup_expression_2 = "isDuplicate(!Match_addr!)"
dup_expression_3 = "isDuplicate(!prvdr_num!)"

dup_codeblock = """uniqueList = []
def isDuplicate(inValue):
  if inValue in uniqueList:
    return 1
  else:
    uniqueList.append(inValue)
    return 0"""






#Processing

#createt the fild geodatabse  container only do once
arcpy.CreateFileGDB_management(datafold, "input","CURRENT")
arcpy.CreateFileGDB_management(procfold, "processing","CURRENT")


#bring the csv input table into the geodatabase
arcpy.TableToTable_conversion(hosp_csv, inputgdb, "hospitals")

#add unique ID field
arcpy.AddField_management(hosp_tbl, "uid", "LONG", )

#cal uniq ID field
arcpy.CalculateField_management(hosp_tbl,"uid","!OBJECTID! + 1000000","PYTHON_9.3","#")

#Run frequency just to see the count of unique Provider Numbers.
arcpy.Frequency_analysis("V:/projects/hospitals/data/input.gdb/hospitals","V:/projects/hospitals/data/input.gdb/hospitals_freq_prvdr_num","prvdr_num","#")

#strip fields for geocode
arcpy.TableToTable_conversion(hosp_tbl,inputgdb,"hospitals_addr")

#DELETE THE UNNECESSAARY FIELDS WITH DELETE FIELD MANAGEEMET
arcpy.DeleteField_management("hospitals_addr","rpt_rec_num;cash;notes_rec;acc_rec;inventory;oth_cur_asset;tot_cur_asset;land;land_imp;building;fixed_equipt;auto_truck;major_mov_equipt;tot_fix_asset;invetment;oth_asset;tot_oth_asset;tot_asset;acc_pay;salary_fee_pay;oth_cur_liab;tot_cur_liab;notes_pay;other_lt_liab;tot_lt_liab;tot_liab;gen_fund_bal;tot_fund;tot_liab_fund;tot_pat_rev;tot_rev;contract;net_rev;tot_op;net_inc;contr_don_beq;income_invest;rev_tel;purchase_disc;rev_meal;rev_sale_med_sup;rev_sale_med_rec;tuition;ren_hosp_space;other;tot_oth_income;total_income;oth_exp;tot_oth_exp;net_income;type_of_control;type_of_hospital;oth_rec;allow_uncollect;prep_exp;minor_equipt_nondep;payroll_tax_pay;st_notes_pay;mortage_pay;rebate_exp;rev_rental;rev_sale_drug;gov_approp;type_of_subprovider;leasehold_imp;minor_mov_equipt;due_to_oth_fund;rent_vending;rev_gift_shop;_13_;rev_laundry;_14_;due_from_owner;temp_invest;deposit_on_lease;rev_tv_ratio;def_income;due_from_oth_fund;unsec_loan;parking_receipt;accel_pay;rpt_stus_cd;initl_rpt_sw;last_rpt_sw;trnsmtl_num;fi_num;adr_vndr_cd;util_cd;spec_ind;npi")

#add "addr_concate_str" field
arcpy.AddField_management(hospaddr, "addr_concate_str", "TEXT")

#calc "addr_concate_str" field
arcpy.CalculateField_management(hospaddr,"addr_concate_str","""!street!.strip('/').strip("\").strip('#') + "^" + !city! + "^" + !state! + "^" + !zip!.strip('-') ""","PYTHON_9.3","#")

#geocode 10.1
arcpy.GeocodeAddresses_geocoding(hospaddr,geocoder_10_1,"Street Street VISIBLE NONE;City City VISIBLE NONE;State State VISIBLE NONE;ZIP ZIP VISIBLE NONE",hospgeo1,"STATIC")

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "hospitals_addr_geocode_1"
arcpy.Statistics_analysis("hospitals_addr_geocode_1","V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_summary","fyear MIN;fyear MAX","prvdr_num;Match_addr")

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "hospitals_addr_geocode_1_summary"
arcpy.Sort_management("hospitals_addr_geocode_1_summary","V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_summary_sort","prvdr_num ASCENDING;MIN_fyear ASCENDING","UR")

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "hospitals_addr_geocode_1_summary_sort"
arcpy.AddField_management("hospitals_addr_geocode_1_summary_sort","prvdr_dup","SHORT","#","#","#","#","NULLABLE","NON_REQUIRED","#")

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "hospitals_addr_geocode_1_summary_sort"
arcpy.CalculateField_management("hospitals_addr_geocode_1_summary_sort","prvdr_dup","isDuplicate(!prvdr_num!)","PYTHON_9.3","/nuniqueList = []/ndef isDuplicate(inValue):/n  if inValue in uniqueList:/n    return 1/n  else:/n    uniqueList.append(inValue)/n    return 0/n")

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "hospitals_addr_geocode_1_summary_sort"
arcpy.AddField_management("hospitals_addr_geocode_1_summary_sort","addr","TEXT","#","#","#","#","NULLABLE","NON_REQUIRED","#")

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "hospitals_addr_geocode_1_summary_sort"
arcpy.CalculateField_management("hospitals_addr_geocode_1_summary_sort","addr","!Match_addr!.split(',')[0]","PYTHON_9.3","#")

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "hospitals_addr_geocode_1_summary_sort"
arcpy.StandardizeAddresses_geocoding("hospitals_addr_geocode_1_summary_sort","addr","US Address - Dual Ranges","HouseNum;PreDir;PreType;StreetName;SufType;SufDir","V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_summary_sort_stdz","Static")

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "hospitals_addr_geocode_1_summary_sort_stdz"
arcpy.AddField_management("hospitals_addr_geocode_1_summary_sort_stdz","prvd_street","TEXT","#","#","#","#","NULLABLE","NON_REQUIRED","#")

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "hospitals_addr_geocode_1_summary_sort_stdz"
arcpy.CalculateField_management("hospitals_addr_geocode_1_summary_sort_stdz","prvd_street","str(!prvdr_num!) + '^' + !ADDR_SN!","PYTHON_9.3","#")

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "hospitals_addr_geocode_1_summary_sort_stdz"
arcpy.Sort_management("hospitals_addr_geocode_1_summary_sort_stdz","V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_summary_sort_stdz_sort","prvd_street ASCENDING;FREQUENCY DESCENDING","UR")

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "hospitals_addr_geocode_1_summary_sort_stdz_sort"
arcpy.AddField_management("hospitals_addr_geocode_1_summary_sort_stdz_sort","prvd_street_dup","SHORT","#","#","#","#","NULLABLE","NON_REQUIRED","#")

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "hospitals_addr_geocode_1_summary_sort_stdz_sort"
arcpy.CalculateField_management("hospitals_addr_geocode_1_summary_sort_stdz_sort","prvd_street_dup","isDuplicate(!prvd_street!)","PYTHON_9.3","/nuniqueList = []/ndef isDuplicate(inValue):/n  if inValue in uniqueList:/n    return 1/n  else:/n    uniqueList.append(inValue)/n    return 0/n")

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "hospitals_addr_geocode_1_summary_sort_stdz_sort"
arcpy.AddField_management("hospitals_addr_geocode_1_summary_sort_stdz_sort","no_addr","SHORT","#","#","#","#","NULLABLE","NON_REQUIRED","#")

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "hospitals_addr_geocode_1_summary_sort_stdz_sort"
arcpy.CalculateField_management("hospitals_addr_geocode_1_summary_sort_stdz_sort","no_addr","NoAddr( !addr!)","PYTHON_9.3","def NoAddr(addr):/n  if addr == '':/n    return 1/n  else:/n    return 0")

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "hospitals_addr_geocode_1_summary_sort_stdz_sort"
arcpy.TableToTable_conversion("hospitals_addr_geocode_1_summary_sort_stdz_sort","V:/projects/hospitals/data/input.gdb","hospitals_addr_geocode_1_summary_sort_stdz_sort_tablett",""""prvd_street_dup" = 0 AND "no_addr" = 0""","""ADDR_HN "HouseNum" true true false 12 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_summary_sort_stdz_sort,ADDR_HN,-1,-1;ADDR_PD "PreDir" true true false 12 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_summary_sort_stdz_sort,ADDR_PD,-1,-1;ADDR_PT "PreType" true true false 40 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_summary_sort_stdz_sort,ADDR_PT,-1,-1;ADDR_SN "StreetName" true true false 60 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_summary_sort_stdz_sort,ADDR_SN,-1,-1;ADDR_ST "SufType" true true false 40 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_summary_sort_stdz_sort,ADDR_ST,-1,-1;ADDR_SD "SufDir" true true false 12 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_summary_sort_stdz_sort,ADDR_SD,-1,-1;prvdr_num "prvdr_num" true true false 4 Long 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_summary_sort_stdz_sort,prvdr_num,-1,-1;Match_addr "Match_addr" true true false 120 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_summary_sort_stdz_sort,Match_addr,-1,-1;FREQUENCY "FREQUENCY" true true false 4 Long 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_summary_sort_stdz_sort,FREQUENCY,-1,-1;MIN_fyear "MIN_fyear" true true false 8 Double 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_summary_sort_stdz_sort,MIN_fyear,-1,-1;MAX_fyear "MAX_fyear" true true false 8 Double 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_summary_sort_stdz_sort,MAX_fyear,-1,-1;prvdr_dup "prvdr_dup" true true false 2 Short 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_summary_sort_stdz_sort,prvdr_dup,-1,-1;addr "addr" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_summary_sort_stdz_sort,addr,-1,-1;prvd_street "prvd_street" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_summary_sort_stdz_sort,prvd_street,-1,-1;prvd_street_dup "prvd_street_dup" true true false 2 Short 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_summary_sort_stdz_sort,prvd_street_dup,-1,-1;no_addr "no_addr" true true false 2 Short 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_summary_sort_stdz_sort,no_addr,-1,-1""","#")

#this resulting table has 8373 records and a freq of unique Provider IDs of 7792 of the 8907 uniqure provider addresses

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "hospitals_addr_geocode_1_summary"
arcpy.AddField_management("hospitals_addr_geocode_1_summary","prvd_years","TEXT","#","#","#","#","NULLABLE","NON_REQUIRED","#")

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "hospitals_addr_geocode_1_summary"
arcpy.CalculateField_management("hospitals_addr_geocode_1_summary","prvd_years","str(!prvdr_num!) + '^' + str(int(!MIN_fyear!)) + '^' + str(int(!MAX_fyear!))","PYTHON_9.3","#")


#unmatched geocodes

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "hospitals_addr_geocode_1"
arcpy.TableToTable_conversion("hospitals_addr_geocode_1","V:/projects/hospitals/data/input.gdb","hospitals_addr_geocode_1_unmatched",""""Status" = 'U'""","""Status "Status" true true false 1 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,Status,-1,-1;Score "Score" true true false 8 Double 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,Score,-1,-1;Match_type "Match_type" true true false 2 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,Match_type,-1,-1;Match_addr "Match_addr" true true false 120 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,Match_addr,-1,-1;Side "Side" true true false 1 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,Side,-1,-1;Ref_ID "Ref_ID" true true false 8 Double 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,Ref_ID,-1,-1;Addr_type "Addr_type" true true false 20 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,Addr_type,-1,-1;ARC_Street "Street or Intersection" true true false 100 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,ARC_Street,-1,-1;ARC_City "City or Placename" true true false 40 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,ARC_City,-1,-1;ARC_State "State" true true false 20 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,ARC_State,-1,-1;ARC_ZIP "ZIP Code" true true false 10 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,ARC_ZIP,-1,-1;street "street" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,street,-1,-1;city "city" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,city,-1,-1;state "state" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,state,-1,-1;zip "zip" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,zip,-1,-1;county "county" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,county,-1,-1;hospname "hospname" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,hospname,-1,-1;prov_num "prov_num" true true false 4 Long 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,prov_num,-1,-1;urban_rural "urban_rural" true true false 4 Long 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,urban_rural,-1,-1;po_box "po_box" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,po_box,-1,-1;prvdr_ctrl_type_cd "prvdr_ctrl_type_cd" true true false 4 Long 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,prvdr_ctrl_type_cd,-1,-1;prvdr_num "prvdr_num" true true false 4 Long 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,prvdr_num,-1,-1;fy_bgn_dt "fy_bgn_dt" true true false 8 Date 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,fy_bgn_dt,-1,-1;fy_end_dt "fy_end_dt" true true false 8 Date 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,fy_end_dt,-1,-1;proc_dt "proc_dt" true true false 8 Date 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,proc_dt,-1,-1;fi_creat_dt "fi_creat_dt" true true false 8 Date 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,fi_creat_dt,-1,-1;npr_dt "npr_dt" true true false 8 Date 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,npr_dt,-1,-1;fi_rcpt_dt "fi_rcpt_dt" true true false 8 Date 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,fi_rcpt_dt,-1,-1;fyear "fyear" true true false 4 Long 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,fyear,-1,-1;uid "uid" true true false 4 Long 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,uid,-1,-1;addr_concate_str "addr_concate_str" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,addr_concate_str,-1,-1;addr_concate_str_dup "addr_concate_str_dup" true true false 2 Short 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,addr_concate_str_dup,-1,-1;addr_match_prv_dup "addr_match_prv_dup" true true false 2 Short 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1,addr_match_prv_dup,-1,-1""","#")
#REMOVE PUERTO RICO HOSPITALS 


# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "hospitals_addr_geocode_1_unmatched"
arcpy.CalculateField_management("hospitals_addr_geocode_1_unmatched","addr_concate_str","!addr_concate_str!.replace('.', ' ').replace(' STREET', ' ST').replace(' ROAD', ' RD').replace('  ', ' ').replace('   ', ' ').replace(' FLOOR', ' FL').replace( ' ^', '^')","PYTHON_9.3","#")

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "hospitals_addr_geocode_1_unmatched_summary"
arcpy.AddField_management("hospitals_addr_geocode_1_unmatched_summary","addr","TEXT","#","#","#","#","NULLABLE","NON_REQUIRED","#")

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "hospitals_addr_geocode_1_unmatched_summary"
arcpy.CalculateField_management("hospitals_addr_geocode_1_unmatched_summary","addr","!addr_concate_str!.replace('^', ' ', 5)","PYTHON_9.3","#")

#export missed to csv - currently shouldn't work b/c don't have code to import XTOOLS in this yet.
# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "hospitals_addr_geocode_1_unmatched_summary"
arcpy.XToolsPro_Table2Text("hospitals_addr_geocode_1_unmatched_summary","addr","V:/projects/hospitals/data/processing/geocoding/export_missed.csv")

import shutil
shutil.copy2("V:/projects/hospitals/data/processing/geocoding/export_missed.csv", "V:/projects/hospitals/scripts/geocode/addr.csv")

#GOOGLE GEOCODER RUN IN MAC TERMINAL

#open terminal, run  
# ---- $cd SpiderOak/projects/hospitals/scripts/geocode
# ---- $ python geocode.py
# copy paste into sublime save as /Users/danielmsheehan/SpiderOak/projects/hospitals/data/processing/geocoding/export_missed_google.txt

#bring in google geocoded file to file geodatabase
arcpy.TableToTable_conversion("V:/projects/hospitals/data/processing/geocoding/export_missed_google.txt","V:/projects/hospitals/data/input.gdb","export_missed_google","#","""bad "bad" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/processing/geocoding/export_missed_google.txt,bad,-1,-1;address "address" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/processing/geocoding/export_missed_google.txt,address,-1,-1""","#")
# deleteed second field
# #Google Geocoder results - geography type

# "ROOFTOP" indicates that the returned result is a precise geocode for which we have location information accurate down to street address precision.
# "RANGE_INTERPOLATED" indicates that the returned result reflects an approximation (usually on a road) interpolated between two precise points (such as intersections). Interpolated results are generally returned when rooftop geocodes are unavailable for a street address.
# "GEOMETRIC_CENTER" indicates that the returned result is the geometric center of a result such as a polyline (for example, a street) or polygon (region).
# "APPROXIMATE" indicates that the returned result is approximate.

#add fields to parse all the information 
arcpy.AddField_management("V:/projects/hospitals/data/input.gdb/export_missed_google","addr","TEXT","#","#","#","#","NULLABLE","NON_REQUIRED","#")
arcpy.AddField_management("V:/projects/hospitals/data/input.gdb/export_missed_google","cord","TEXT","#","#","#","#","NULLABLE","NON_REQUIRED","#")
arcpy.AddField_management("V:/projects/hospitals/data/input.gdb/export_missed_google","type","TEXT","#","#","#","#","NULLABLE","NON_REQUIRED","#")
arcpy.AddField_management("V:/projects/hospitals/data/input.gdb/export_missed_google","x","DOUBLE","#","#","#","#","NULLABLE","NON_REQUIRED","#")
arcpy.AddField_management("V:/projects/hospitals/data/input.gdb/export_missed_google","y","DOUBLE","#","#","#","#","NULLABLE","NON_REQUIRED","#")
arcpy.AddField_management("V:/projects/hospitals/data/input.gdb/export_missed_google","y","DOUBLE","#","#","#","#","NULLABLE","NON_REQUIRED","#")
#arcpy.AddField_management("V:/projects/hospitals/data/input.gdb/export_missed_google","prvdr_num","DOUBLE","#","#","#","#","NULLABLE","NON_REQUIRED","#")

#calc address
arcpy.CalculateField_management("V:/projects/hospitals/data/input.gdb/export_missed_google","addr","!bad!.split('^')[0]","PYTHON_9.3","#")
#create new view b/c bad address has no carrots
arcpy.MakeTableView_management("V:/projects/hospitals/data/input.gdb/export_missed_google","export_missed_google_view",""""bad" <> 'bad'""","#","OBJECTID OBJECTID VISIBLE NONE;result_field result_field VISIBLE NONE;addr addr VISIBLE NONE;cord cord VISIBLE NONE;type type VISIBLE NONE")
#calc remaineder of fields with address strings, not 'bad address'
arcpy.CalculateField_management("export_missed_google_view","cord","!bad!.split('^')[1].strip('(').strip(')')","PYTHON_9.3","#")
arcpy.CalculateField_management("export_missed_google_view","type","!bad!.split('^')[2]","PYTHON_9.3","#")
arcpy.CalculateField_management("export_missed_google_view","x","!cord!.split(',')[1]","PYTHON_9.3","#")
arcpy.CalculateField_management("export_missed_google_view","y","!cord!.split(',')[0]","PYTHON_9.3","#")


arcpy.MakeTableView_management("V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_unmatched_summary","hospitals_addr_geocode_1_unm","#","#","OBJECTID OBJECTID VISIBLE NONE;addr_concate_str addr_concate_str VISIBLE NONE;FREQUENCY FREQUENCY VISIBLE NONE;COUNT_prvdr_num COUNT_prvdr_num VISIBLE NONE;addr addr VISIBLE NONE")
# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "hospitals_addr_geocode_1_unm"
arcpy.AddJoin_management("hospitals_addr_geocode_1_unm","OBJECTID","V:/projects/hospitals/data/input.gdb/export_missed_google","OBJECTID","KEEP_ALL")
# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "hospitals_addr_geocode_1_unm"
arcpy.TableToTable_conversion("hospitals_addr_geocode_1_unm","V:/projects/hospitals/data/input.gdb","hospitals_addr_geocode_1_unmatched_summary_google","#","""addr_concate_str "addr_concate_str" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_unmatched_summary,hospitals_addr_geocode_1_unmatched_summary.addr_concate_str,-1,-1;FREQUENCY "FREQUENCY" true true false 4 Long 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_unmatched_summary,hospitals_addr_geocode_1_unmatched_summary.FREQUENCY,-1,-1;COUNT_prvdr_num "COUNT_prvdr_num" true true false 4 Long 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_unmatched_summary,hospitals_addr_geocode_1_unmatched_summary.COUNT_prvdr_num,-1,-1;addr "addr" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_unmatched_summary,hospitals_addr_geocode_1_unmatched_summary.addr,-1,-1;google_OBJECTID "google_OBJECTID" false true false 4 Long 0 9 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_unmatched_summary,export_missed_google.OBJECTID,-1,-1;bad "bad" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_unmatched_summary,export_missed_google.bad,-1,-1;address "address" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_unmatched_summary,export_missed_google.address,-1,-1;gaddr "gaddr" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_unmatched_summary,export_missed_google.addr,-1,-1;cord "cord" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_unmatched_summary,export_missed_google.cord,-1,-1;type "type" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_unmatched_summary,export_missed_google.type,-1,-1;x "x" true true false 8 Double 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_unmatched_summary,export_missed_google.x,-1,-1;y "y" true true false 8 Double 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_unmatched_summary,export_missed_google.y,-1,-1;prvdr_num "prvdr_num" true true false 8 Double 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_unmatched_summary,export_missed_google.prvdr_num,-1,-1""","#")
arcpy.TableToTable_conversion("V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_unmatched_summary_google","V:/projects/hospitals/data/input.gdb","hospitals_addr_geocode_1_unmatched_summary_google_rooftop_interp",""""type" = 'ROOFTOP' OR "type" = 'RANGE_INTERPOLATED'""","""addr_concate_str "addr_concate_str" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_unmatched_summary_google,addr_concate_str,-1,-1;FREQUENCY "FREQUENCY" true true false 4 Long 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_unmatched_summary_google,FREQUENCY,-1,-1;COUNT_prvdr_num "COUNT_prvdr_num" true true false 4 Long 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_unmatched_summary_google,COUNT_prvdr_num,-1,-1;addr "addr" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_unmatched_summary_google,addr,-1,-1;google_OBJECTID "google_OBJECTID" true true false 4 Long 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_unmatched_summary_google,google_OBJECTID,-1,-1;bad "bad" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_unmatched_summary_google,bad,-1,-1;address "address" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_unmatched_summary_google,address,-1,-1;gaddr "gaddr" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_unmatched_summary_google,gaddr,-1,-1;cord "cord" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_unmatched_summary_google,cord,-1,-1;type "type" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_unmatched_summary_google,type,-1,-1;x "x" true true false 8 Double 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_unmatched_summary_google,x,-1,-1;y "y" true true false 8 Double 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_unmatched_summary_google,y,-1,-1;prvdr_num "prvdr_num" true true false 8 Double 0 0 ,First,#,V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_unmatched_summary_google,prvdr_num,-1,-1""","#")







#make view to do join, here I want to join back the Provider number from the Postal Geocodes output to the output of the Google Geocoders
arcpy.MakeTableView_management("V:/projects/hospitals/data/input.gdb/export_missed_google","export_missed_google_view_join","#","#","OBJECTID OBJECTID VISIBLE NONE;bad bad VISIBLE NONE;addr addr VISIBLE NONE;cord cord VISIBLE NONE;type type VISIBLE NONE;x x VISIBLE NONE;y y VISIBLE NONE")
#add the join so we got the provider number now joined to the google geocode output - we're joining on OBJECT ID b/c we know the order is the same
arcpy.AddJoin_management("export_missed_google_view_join","OBJECTID","V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_sort_export_missed","OBJECTID","KEEP_ALL")
#calc the field so we have Provider Number




arcpy.CalculateField_management("export_missed_google_view_join","export_missed_google.prvdr_num","!hospitals_addr_geocode_1_sort_export_missed.prvdr_num!","PYTHON_9.3","#")
#remove the join
arcpy.RemoveJoin_management("export_missed_google_view_join","hospitals_addr_geocode_1_sort_export_missed")

#Run frequency just to see the count of unique Provider Numbers.
arcpy.Frequency_analysis("V:/projects/hospitals/data/input.gdb/hospitals","V:/projects/hospitals/data/input.gdb/hospitals_freq_prvdr_num","prvdr_num","#")

# Okay now we are going to geocode the center_for_medicaid_and_medicare data
# CMS (medicaid medicare)
#bring table in, CMS
arcpy.TableToTable_conversion("V:/projects/hospitals/data/_original/center_for_medicaid_and_medicare/Hospital_Data.csv","V:/projects/hospitals/data/input.gdb","cms_hospitals","#","""Provider_Number "Provider_Number" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/_original/center_for_medicaid_and_medicare/Hospital_Data.csv,Provider Number,-1,-1;Hospital_Name "Hospital_Name" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/_original/center_for_medicaid_and_medicare/Hospital_Data.csv,Hospital Name,-1,-1;Address_1 "Address_1" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/_original/center_for_medicaid_and_medicare/Hospital_Data.csv,Address 1,-1,-1;Address_2 "Address_2" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/_original/center_for_medicaid_and_medicare/Hospital_Data.csv,Address 2,-1,-1;Address_3 "Address_3" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/_original/center_for_medicaid_and_medicare/Hospital_Data.csv,Address 3,-1,-1;City "City" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/_original/center_for_medicaid_and_medicare/Hospital_Data.csv,City,-1,-1;State "State" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/_original/center_for_medicaid_and_medicare/Hospital_Data.csv,State,-1,-1;ZIP_Code "ZIP_Code" true true false 4 Long 0 0 ,First,#,V:/projects/hospitals/data/_original/center_for_medicaid_and_medicare/Hospital_Data.csv,ZIP Code,-1,-1;County "County" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/_original/center_for_medicaid_and_medicare/Hospital_Data.csv,County,-1,-1;Phone_Number "Phone_Number" true true false 8 Double 0 0 ,First,#,V:/projects/hospitals/data/_original/center_for_medicaid_and_medicare/Hospital_Data.csv,Phone Number,-1,-1;Hospital_Type "Hospital_Type" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/_original/center_for_medicaid_and_medicare/Hospital_Data.csv,Hospital Type,-1,-1;Hospital_Ownership "Hospital_Ownership" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/_original/center_for_medicaid_and_medicare/Hospital_Data.csv,Hospital Ownership,-1,-1;Emergency_Services "Emergency_Services" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/_original/center_for_medicaid_and_medicare/Hospital_Data.csv,Emergency Services,-1,-1""","#")
#geocode
arcpy.GeocodeAddresses_geocoding("V:/projects/hospitals/data/input.gdb/cms_hospitals","W:/GIS/Data/Esri/Data_and_Maps_10-1/streetmap_na/data/Composite_US","Street Address_1 VISIBLE NONE;City City VISIBLE NONE;State State VISIBLE NONE;ZIP ZIP_Code VISIBLE NONE","V:/projects/hospitals/data/input.gdb/cms_hospitals_geocode_1","STATIC")



