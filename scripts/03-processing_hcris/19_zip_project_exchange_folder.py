#zip file manually here. E:\SpiderOak\projects\hospitals\exchange

#then this copies to SpiderOak main Exchange folder
import shutil

drivepath = 'E:/SpiderOak/'
fldata = 'projects/hospitals/exchange'
flexch = 'exchange/to_20130617_catie'

shutil.copy2(drivepath+fldata+'/to_catie_20130617.zip', drivepath+flexch+'/to_catie_20130617.zip')
#E:/SpiderOak/projects/hospitals/exchange
#E:/SpiderOak/exchange/to_20130617_catie
#drivepath+flexch+