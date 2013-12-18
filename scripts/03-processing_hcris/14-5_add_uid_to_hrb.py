#update this as it currently doesnt run off 008

arcpy.JoinField_management("E:/SpiderOak/projects/hospitals/data/output/tables/dbf/hrb_agesexrace.dbf","uidpreint","E:/SpiderOak/projects/hospitals/data/output/tables/dbf/uid_uidpreint.dbf","uidpreint","uid")
arcpy.JoinField_management("E:/SpiderOak/projects/hospitals/data/output/tables/dbf/hrb_econ.dbf","uidpreint","E:/SpiderOak/projects/hospitals/data/output/tables/dbf/uid_uidpreint.dbf","uidpreint","uid")
arcpy.JoinField_management("E:/SpiderOak/projects/hospitals/data/output/tables/dbf/hrb_education.dbf","uidpreint","E:/SpiderOak/projects/hospitals/data/output/tables/dbf/uid_uidpreint.dbf","uidpreint","uid")
arcpy.JoinField_management("E:/SpiderOak/projects/hospitals/data/output/tables/dbf/hrb_lingiso.dbf","uidpreint","E:/SpiderOak/projects/hospitals/data/output/tables/dbf/uid_uidpreint.dbf","uidpreint","uid")
arcpy.JoinField_management("E:/SpiderOak/projects/hospitals/data/output/tables/dbf/hrb_poverty.dbf","uidpreint","E:/SpiderOak/projects/hospitals/data/output/tables/dbf/uid_uidpreint.dbf","uidpreint","uid")

