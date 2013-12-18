//clean NISUID table
use W:\GIS\Projects\hospitals\data\output\tables\nisuid_intersect_census\nis_census_county_tract_geoids.dta 
gen NISzip = zip
drop zip
save "W:\GIS\Projects\hospitals\data\output\tables\nisuid_intersect_census\nis_census_county_tract_geoids.dta", replace

//Merge with the relationship (crosswalk) file
use W:\GIS\Projects\hospitals\data\output\tables\hcris_census_data\dta\final\hospitals_final.dta 
drop _merge
merge 1:1 uid using "W:\GIS\Projects\hospitals\data\output\tables\hcris_nis_relationship\hcris_uid_and_nisuid.dta"
drop _merge

//merge HCRIS with NISUID
merge m:1 nisuid using "W:\GIS\Projects\hospitals\data\output\tables\nisuid_intersect_census\nis_census_county_tract_geoids.dta"

save "W:\GIS\Projects\hospitals\data\output\tables\final_hcris_nis_master\final_hcris_nis_master.dta", replace
