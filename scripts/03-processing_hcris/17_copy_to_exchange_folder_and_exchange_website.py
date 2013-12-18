import shutil

drivepath = 'E:/SpiderOak/projects/hospitals/'
fldata = 'data/output/tables/dta'
flexch = 'exchange/to_catie_20130617'

fldocu = 'docs'

#copy stata file
shutil.copy2(drivepath+fldata+'/hcris.dta', drivepath+flexch+'/hcris.dta')
shutil.copy2(drivepath+fldocu+'/hospitals_data_dictionary.pdf', drivepath+flexch+'/hospitals_data_dictionary.pdf')