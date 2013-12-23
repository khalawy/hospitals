import arcpy
import csv
from arcpy import env
env.overwriteOutput = True

data_path = 'W:\GIS\Projects\hospitals\data'

countygeolist = ['co2000_nest','co2010_nest']
tractgeolist  = ['ct2000_bint','ct2000_nest','ct2010_bint','ct2010_nest']
zctageolist   = ['zt2000_bint','zt2000_nest']
listofallgeos =  countygeolist + tractgeolist + zctageolist
listofgdbs    = ['county','county','tract','tract','tract','tract','zcta','zcta']
tract2000only =  ['ct2000_bint','ct2000_nest']
ct2000varsfilelist = ['agesexrace','econ','education','lingiso','poverty']

for vars2000 in ct2000varsfilelist:
	for geo   in tract2000only:
		toViews = data_path + '/processing_nis/variables/tract.gdb/nis_' + geo
		outViewsgdb = data_path + '/processing_nis/variables/tract.gdb/'
		outViews = 'nis_' + geo + "_" + vars2000
		join_table = data_path + "/input/census/variables.gdb/" + vars2000
		arcpy.MakeTableView_management(toViews,"nis_"+geo+"_"+vars2000+"_View","#","#","#")
		arcpy.AddJoin_management("nis_" + geo + "_" + vars2000 + "_View","ct2000",join_table,"ct2000","KEEP_ALL")
		arcpy.TableToTable_conversion("nis_" + geo + "_" + vars2000 + "_View",outViewsgdb, outViews)

theFields = [['cntpop','cnt65o','cntblk','cnthis'],
['cnt16o','cntune'],
['cnt25o','cntlhs'],
['cntlan','cntlin'],
['cntppv','cntpov']]

fieldprefix = ['ct2000pol','ct2000buf']
tract2000only =  ['ct2000_nest','ct2000_bint']

for fieldpre, geo in zip(fieldprefix, tract2000only):
	for vars2000, theField in zip(ct2000varsfilelist, theFields):
		addTable = data_path + '/processing_nis/variables/tract.gdb/nis_' + geo + "_" + vars2000
		#print addTable + "-" + fieldpre+str(theField)
		for aField in theField:
			print aField
			arcpy.AddField_management(addTable,fieldpre+aField,"DOUBLE")

thePolyCalcs = [['!agesexrace_HC01_VC01!','!agesexrace_HC01_VC24!','!agesexrace_HC01_VC30!','!agesexrace_HC01_VC56!'],
['!econ_HC01_VC02!','!econ_HC01_VC09!'],
['!education_HC01_VC09!','(!education_HC01_VC10!+!education_HC01_VC11!)'],
['!lingiso_VD01!','(!lingiso_VD04! + !lingiso_VD07! + !lingiso_VD10! + !lingiso_VD13!)'],
['!poverty_HC02_VC01!','!poverty_HC03_VC01!']]

for vars2000, theField, theCalc in zip(ct2000varsfilelist, theFields, thePolyCalcs):
	addTable = data_path + '/processing_nis/variables/tract.gdb/nis_ct2000_nest_' + vars2000
	for aField, aCalc in zip(theField, theCalc):
		exp = aCalc
		print exp
		arcpy.CalculateField_management(addTable,'ct2000pol'+aField, exp, "PYTHON_9.3") 

theBuffCalcs = [['!pcttractarea!*!agesexrace_HC01_VC01!','!pcttractarea!*!agesexrace_HC01_VC24!','!pcttractarea!*!agesexrace_HC01_VC30!','!pcttractarea!*!agesexrace_HC01_VC56!'],
['!pcttractarea!*!econ_HC01_VC02!','!pcttractarea!*!econ_HC01_VC09!'],
['!pcttractarea!*!education_HC01_VC09!','!pcttractarea!*(!education_HC01_VC10!+!education_HC01_VC11!)'],
['!pcttractarea!*!lingiso_VD01!','!pcttractarea!*(!lingiso_VD04! + !lingiso_VD07! + !lingiso_VD10! + !lingiso_VD13!)'],
['!pcttractarea!*!poverty_HC02_VC01!','!pcttractarea!*!poverty_HC03_VC01!']]

for vars2000, theField, theCalc in zip(ct2000varsfilelist, theFields, theBuffCalcs):
	addTable = data_path + '/processing_nis/variables/tract.gdb/nis_ct2000_bint_' + vars2000
	for aField, aCalc in zip(theField, theCalc):
		exp = aCalc
		print exp
		arcpy.CalculateField_management(addTable,'ct2000buf'+aField, exp, "PYTHON_9.3") 


arcpy.Frequency_analysis("W:/GIS/Projects/hospitals/data/processing_nis/variables/tract.gdb/nis_ct2000_bint_agesexrace","W:/GIS/Projects/hospitals/data/processing_nis/variables/tract.gdb/nis_ct2000_bint_agesexrace_freq","nisuid","ct2000bufcntpop;ct2000bufcnt65o;ct2000bufcntblk;ct2000bufcnthis")
arcpy.Frequency_analysis("W:/GIS/Projects/hospitals/data/processing_nis/variables/tract.gdb/nis_ct2000_bint_econ","W:/GIS/Projects/hospitals/data/processing_nis/variables/tract.gdb/nis_ct2000_bint_econ_freq","nisuid","ct2000bufcnt16o;ct2000bufcntune")
arcpy.Frequency_analysis("W:/GIS/Projects/hospitals/data/processing_nis/variables/tract.gdb/nis_ct2000_bint_education","W:/GIS/Projects/hospitals/data/processing_nis/variables/tract.gdb/nis_ct2000_bint_education_freq","nisuid","ct2000bufcnt25o;ct2000bufcntlhs")
arcpy.Frequency_analysis("W:/GIS/Projects/hospitals/data/processing_nis/variables/tract.gdb/nis_ct2000_bint_lingiso","W:/GIS/Projects/hospitals/data/processing_nis/variables/tract.gdb/nis_ct2000_bint_lingiso_freq","nisuid","ct2000bufcntlan;ct2000bufcntlin")
arcpy.Frequency_analysis("W:/GIS/Projects/hospitals/data/processing_nis/variables/tract.gdb/nis_ct2000_bint_poverty","W:/GIS/Projects/hospitals/data/processing_nis/variables/tract.gdb/nis_ct2000_bint_poverty_freq","nisuid","ct2000bufcntppv;ct2000bufcntpov")


arcpy.ImportToolbox('C:\Program Files (x86)\DataEast\XTools Pro\Toolbox\XTOOLS PRO.tbx')


arcpy.XToolsGP_Export2Text("W:/GIS/Projects/hospitals/data/processing_nis/variables/tract.gdb/nis_ct2000_bint_agesexrace_freq","nisuid;ct2000bufcntpop;ct2000bufcnt65o;ct2000bufcntblk;ct2000bufcnthis","#","false","false")
arcpy.XToolsGP_Export2Text("W:/GIS/Projects/hospitals/data/processing_nis/variables/tract.gdb/nis_ct2000_bint_econ_freq","nisuid;ct2000bufcnt16o;ct2000bufcntune","#","false","false")
arcpy.XToolsGP_Export2Text("W:/GIS/Projects/hospitals/data/processing_nis/variables/tract.gdb/nis_ct2000_bint_education_freq","nisuid;ct2000bufcnt25o;ct2000bufcntlhs","#","false","false")
arcpy.XToolsGP_Export2Text("W:/GIS/Projects/hospitals/data/processing_nis/variables/tract.gdb/nis_ct2000_bint_lingiso_freq","nisuid;ct2000bufcntlan;ct2000bufcntlin","#","false","false")
arcpy.XToolsGP_Export2Text("W:/GIS/Projects/hospitals/data/processing_nis/variables/tract.gdb/nis_ct2000_bint_poverty_freq","nisuid;ct2000bufcntppv;ct2000bufcntpov","#","false","false")

arcpy.XToolsGP_Export2Text("W:/GIS/Projects/hospitals/data/processing_nis/variables/tract.gdb/nis_ct2000_nest_agesexrace","nisuid;ct2000;ct2000polcntpop;ct2000polcnt65o;ct2000polcntblk;ct2000polcnthis","#","false","false")
arcpy.XToolsGP_Export2Text("W:/GIS/Projects/hospitals/data/processing_nis/variables/tract.gdb/nis_ct2000_nest_econ","nisuid;ct2000;ct2000polcnt16o;ct2000polcntune;ct2000polpctune","#","false","false")
arcpy.XToolsGP_Export2Text("W:/GIS/Projects/hospitals/data/processing_nis/variables/tract.gdb/nis_ct2000_nest_education","nisuid;ct2000;ct2000polcnt25o;ct2000polcntlhs","#","false","false")
arcpy.XToolsGP_Export2Text("W:/GIS/Projects/hospitals/data/processing_nis/variables/tract.gdb/nis_ct2000_nest_lingiso","nisuid;ct2000;ct2000polcntlan;ct2000polcntlin","#","false","false")
arcpy.XToolsGP_Export2Text("W:/GIS/Projects/hospitals/data/processing_nis/variables/tract.gdb/nis_ct2000_nest_poverty","nisuid;ct2000;ct2000polcntppv;ct2000polcntpov","#","false","false")