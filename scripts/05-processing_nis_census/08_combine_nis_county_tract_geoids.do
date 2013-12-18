use W:\GIS\Projects\hospitals\data\processing_nis\nis_census_tables\nisuid_co2000.dta 
gen co2000 = cntyidfp
drop cntyidfp
save "W:\GIS\Projects\hospitals\data\processing_nis\nis_census_tables\nisuid_co2000.dta", replace

use W:\GIS\Projects\hospitals\data\processing_nis\nis_census_tables\nisuid_co2010.dta 
gen co2010 = GEOID10
drop GEOID10
save "W:\GIS\Projects\hospitals\data\processing_nis\nis_census_tables\nisuid_co2010.dta", replace

use W:\GIS\Projects\hospitals\data\processing_nis\nis_census_tables\nisuid_ct2000.dta 
gen ct2000 = CTIDFP00
drop CTIDFP00
save "W:\GIS\Projects\hospitals\data\processing_nis\nis_census_tables\nisuid_ct2000.dta", replace

use W:\GIS\Projects\hospitals\data\processing_nis\nis_census_tables\nisuid_ct2010.dta 
gen ct2010 = GEOID10
drop GEOID10
save "W:\GIS\Projects\hospitals\data\processing_nis\nis_census_tables\nisuid_ct2010.dta", replace

use W:\GIS\Projects\hospitals\data\processing_nis\nis_census_tables\nisuid_co2000.dta 
merge 1:1 nisuid using "W:\GIS\Projects\hospitals\data\processing_nis\nis_census_tables\nisuid_co2010.dta"
drop _merge
merge 1:1 nisuid using "W:\GIS\Projects\hospitals\data\processing_nis\nis_census_tables\nisuid_ct2000.dta"
drop _merge
merge 1:1 nisuid using "W:\GIS\Projects\hospitals\data\processing_nis\nis_census_tables\nisuid_ct2010.dta"
drop _merge

merge 1:1 nisuid using "W:\GIS\Projects\hospitals\data\processing_nis\nis_census_tables\nisuid_orig_nis_data.dta"
drop _merge

save "W:\GIS\Projects\hospitals\data\output\tables\nisuid_intersect_census\nis_census_county_tract_geoids.dta", replace
