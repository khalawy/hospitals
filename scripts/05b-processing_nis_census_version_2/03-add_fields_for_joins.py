import arcpy
import csv
from arcpy import env
env.overwriteOutput = True

data_path = 'W:\GIS\Projects\hospitals\data'

countygeolist = ['co2000_nest','co2010_nest']
tractgeolist  = ['ct2000_bint','ct2000_nest','ct2010_bint','ct2010_nest']
zctageolist   = ['zt2000_bint','zt2000_nest']

listofallgeos =  countygeolist + tractgeolist+ zctageolist

listofgdbs    = ['county','county','tract','tract','tract','tract','zcta','zcta']

addfield1     = ['co2000','co2000']
addfield2     = ['ct2000','ct2000','ct2010','ct2010']
addfield3     = ['zt2000','zt2000']

listoffields = addfield1 + addfield2 + addfield3

for geos, fields, gdb in zip(listofallgeos, listoffields, listofgdbs):
	geos_full = data_path + '/processing_nis/variables/'+gdb+'.gdb/nis_'+geos
	arcpy.AddField_management(geos_full, fields, "TEXT")

geoidorigs    = ['CNTYIDFP','GEOID10','CTIDFP00','CTIDFP00','GEOID10','GEOID10', 'ZCTA5CE00', 'ZCTA5CE00']

for geos, fields, gdb, exporig in zip(listofallgeos, listoffields, listofgdbs, geoidorigs):
	geos_full = data_path + '/processing_nis/variables/'+gdb+'.gdb/nis_'+geos
	exp = '!'+ exporig + '!'
	arcpy.CalculateField_management(geos_full, fields, exp, "PYTHON")


ct2000varsfilelist = ['agesexrace','econ','education','lingiso','poverty']

for topic in ct2000varsfilelist:
	geos_full = data_path + '/input/census/variables.gdb/'+ topic
	arcpy.AddField_management(geos_full, 'ct2000', "TEXT")

for topic in ct2000varsfilelist:
	exp = "!GEO_id![9:]"
	geos_full = data_path + '/input/census/variables.gdb/'+ topic
	arcpy.CalculateField_management(geos_full, 'ct2000', exp, "PYTHON_9.3")

