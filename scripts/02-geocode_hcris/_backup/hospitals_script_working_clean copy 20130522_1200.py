import arcpy

#MacBook Pro-Windows 7

drive_path = "V:/"
dropbox_path = "W:/"

#Rundle-008

#Static
project_folder = "/projects/hospitals"
proj = drive_path+project_folder
datafold = proj + "/data"
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

#bring the csv input table into the geodatabase
arcpy.TableToTable_conversion(hosp_csv, inputgdb, "hospitals")

#add unique ID field
arcpy.AddField_management(hosp_tbl, "uid", "LONG", )

#cal uniq ID field
arcpy.CalculateField_management(hosp_tbl,"uid","!OBJECTID! + 1000000","PYTHON_9.3","#")

#strip fields for geocode
arcpy.TableToTable_conversion(hosp_tbl,inputgdb,"hospitals_addr")

#DELETE THE UNNECESSAARY FIELDS WITH DELETE FIELD MANAGEEMET
arcpy.DeleteField_management("hospitals_addr","rpt_rec_num;cash;notes_rec;acc_rec;inventory;oth_cur_asset;tot_cur_asset;land;land_imp;building;fixed_equipt;auto_truck;major_mov_equipt;tot_fix_asset;invetment;oth_asset;tot_oth_asset;tot_asset;acc_pay;salary_fee_pay;oth_cur_liab;tot_cur_liab;notes_pay;other_lt_liab;tot_lt_liab;tot_liab;gen_fund_bal;tot_fund;tot_liab_fund;tot_pat_rev;tot_rev;contract;net_rev;tot_op;net_inc;contr_don_beq;income_invest;rev_tel;purchase_disc;rev_meal;rev_sale_med_sup;rev_sale_med_rec;tuition;ren_hosp_space;other;tot_oth_income;total_income;oth_exp;tot_oth_exp;net_income;type_of_control;type_of_hospital;oth_rec;allow_uncollect;prep_exp;minor_equipt_nondep;payroll_tax_pay;st_notes_pay;mortage_pay;rebate_exp;rev_rental;rev_sale_drug;gov_approp;type_of_subprovider;leasehold_imp;minor_mov_equipt;due_to_oth_fund;rent_vending;rev_gift_shop;_13_;rev_laundry;_14_;due_from_owner;temp_invest;deposit_on_lease;rev_tv_ratio;def_income;due_from_oth_fund;unsec_loan;parking_receipt;accel_pay;rpt_stus_cd;initl_rpt_sw;last_rpt_sw;trnsmtl_num;fi_num;adr_vndr_cd;util_cd;spec_ind;npi")

#add "addr_concate_str" field
arcpy.AddField_management(hospaddr, "addr_concate_str", "TEXT")

#calc "addr_concate_str" field
arcpy.CalculateField_management(hospaddr,"addr_concate_str","""!street!.strip('/').strip("\").strip('#') + "^" + !city! + "^" + !state! + "^" + !zip!.strip('-') ""","PYTHON_9.3","#")

#add "addr_concate_str_dup" field
arcpy.AddField_management(hospaddr, "addr_concate_str_dup", "SHORT")
arcpy.AddField_management(hospaddr, "addr_match_prv_dup", "SHORT")

#calc
arcpy.CalculateField_management(hospaddr,"addr_concate_str_dup", dup_expression_1, "PYTHON_9.3", dup_codeblock)
arcpy.CalculateField_management(hospaddr,"addr_match_prv_dup", dup_expression_3, "PYTHON_9.3", dup_codeblock)

#UPDATE THIS SO ITS NOT UNIQUE ADDRESS STRINGS ONLY, BUT UNIQUE PRVDR_NUM's 
#table of unique fields
arcpy.TableToTable_conversion(hospaddr,inputgdb,"hospitals_uniqprvd",""""addr_match_prv_dup" = 0""")

#geocode 10.1
arcpy.GeocodeAddresses_geocoding(hospaddr,geocoder_10_1,"Street Street VISIBLE NONE;City City VISIBLE NONE;State State VISIBLE NONE;ZIP ZIP VISIBLE NONE",hospgeo1,"STATIC")

#geocode business f'ing analyst
#arcpy.GeocodeAddresses_geocoding(hospaddr,geocoder_biza,"Street Street VISIBLE NONE;City City VISIBLE NONE;State State VISIBLE NONE;ZIP ZIP VISIBLE NONE",hospgeoc,"STATIC")

#sort by locator, match address, score and provider number
arcpy.Sort_management(hospgeo1, hospgeo1_sort,"Loc_name DESCENDING;Match_addr ASCENDING;Score DESCENDING;prvdr_num ASCENDING","UR")

#add "addr_concate_str_dup" and providor field
arcpy.AddField_management(hospgeo1_sort, "addr_match_str_dup", "SHORT")
arcpy.AddField_management(hospgeo1_sort, "addr_match_prv_dup", "SHORT")

#calc those fields
arcpy.CalculateField_management(hospgeo1_sort,"addr_match_str_dup", dup_expression_2, "PYTHON_9.3", dup_codeblock)
arcpy.CalculateField_management(hospgeo1_sort,"addr_match_prv_dup", dup_expression_3, "PYTHON_9.3", dup_codeblock)

#generate tables of unique fields
arcpy.TableToTable_conversion(hospgeo1_sort,inputgdb,"hospitals_addr_geocode_1_sort_export",""" "addr_match_str_dup" = 0 AND "addr_match_prv_dup" = 0 """)
arcpy.TableToTable_conversion(hospgeo1_stex,inputgdb,"hospitals_addr_geocode_1_sort_export_missed", """"Loc_name" = 'Postal_US' AND "state" <> 'PR'        """)

#remove carrots from address strings
arcpy.CalculateField_management(hospgeo1_semi,"addr_concate_str", "!addr_concate_str!.replace('^', ' ', 5) ", "PYTHON_9.3")

#from here need to update path names as will only run on MacBook Pro, not using variables and paths, etc. 

#export missed to csv - currently shouldn't work b/c don't have code to import XTOOLS in this yet.
arcpy.XToolsPro_Table2Text("V:/projects/hospitals/data/input.gdb/hospitals_addr_geocode_1_sort_export_missed","prvdr_num;addr_concate_str","V:/projects/hospitals/data/processing/geocoding/export_missed.csv")

#copy csv file to geocoding script location and change to addr.csv
import shutil
shutil.copy2("V:/projects/hospitals/data/processing/geocoding/export_missed.csv", "V:/projects/hospitals/scripts/geocode/addr.csv")

#GOOGLE GEOCODER RUN IN MAC TERMINAL

#open terminal, run  
# ---- $cd SpiderOak/projects/hospitals/scripts/geocode
# ---- $ python geocode.py
# copy paste into sublime save as /Users/danielmsheehan/SpiderOak/projects/hospitals/data/processing/geocoding/export_missed_google.txt

#bring in google geocoded file to file geodatabase
arcpy.TableToTable_conversion("V:/projects/hospitals/data/processing/geocoding/export_missed_google.txt","V:/projects/hospitals/data/input.gdb","export_missed_google","#","""result_field "result_field" true true false 255 Text 0 0 ,First,#,V:/projects/hospitals/data/processing/geocoding/export_missed_google.txt,bad address,-1,-1""","#")

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
arcpy.AddField_management("V:/projects/hospitals/data/input.gdb/export_missed_google","prvdr_num","DOUBLE","#","#","#","#","NULLABLE","NON_REQUIRED","#")

#calc address
arcpy.CalculateField_management("V:/projects/hospitals/data/input.gdb/export_missed_google","addr","!result_field!.split('^')[0]","PYTHON_9.3","#")
#create new view b/c bad address has no carrots
arcpy.MakeTableView_management("V:/projects/hospitals/data/input.gdb/export_missed_google","export_missed_google_view",""""result_field" <> 'bad address'""","#","OBJECTID OBJECTID VISIBLE NONE;result_field result_field VISIBLE NONE;addr addr VISIBLE NONE;cord cord VISIBLE NONE;type type VISIBLE NONE")
#calc remaineder of fields with address strings, not 'bad address'
arcpy.CalculateField_management("export_missed_google_view","cord","!result_field!.split('^')[1].strip('(').strip(')')","PYTHON_9.3","#")
arcpy.CalculateField_management("export_missed_google_view","type","!result_field!.split('^')[2]","PYTHON_9.3","#")
arcpy.CalculateField_management("export_missed_google_view","x","!cord!.split(',')[1]","PYTHON_9.3","#")
arcpy.CalculateField_management("export_missed_google_view","y","!cord!.split(',')[0]","PYTHON_9.3","#")

#make view to do join, here I want to join back the Provider number from the Postal Geocodes output to the output of the Google Geocoders
arcpy.MakeTableView_management("V:/projects/hospitals/data/input.gdb/export_missed_google","export_missed_google_view_join","#","#","OBJECTID OBJECTID VISIBLE NONE;result_field result_field VISIBLE NONE;addr addr VISIBLE NONE;cord cord VISIBLE NONE;type type VISIBLE NONE;x x VISIBLE NONE;y y VISIBLE NONE")
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



