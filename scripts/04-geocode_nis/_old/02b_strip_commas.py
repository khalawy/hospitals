import arcpy, time, datetime, csv, sys, traceback
from arcpy import env
env.overwriteOutput = True

fin = csv.reader(open("E:/SpiderOak/projects/hospitals/scripts/processing_nis/03_geocode/addr_raw.csv", 'rb'), delimiter=',')
fout = open("E:/SpiderOak/projects/hospitals/scripts/processing_nis/03_geocode/addr.csv", 'w')

print 'Replace commas started at this time: ' + time.strftime('%c') 

for row in fin:
	for item in row:
		str_row = item     
		fout.write(str_row.replace(',',' '))
		fout.write(" ")
	fout.write("\n")

fout.close()
