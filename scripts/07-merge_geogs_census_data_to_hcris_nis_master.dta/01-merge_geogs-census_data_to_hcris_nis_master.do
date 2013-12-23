use "W:\GIS\Projects\hospitals\data\output\tables\final_hcris_nis_master\final_hcris_nis_master.dta", clear
drop _merge
merge m:1 nisuid using 
drop totpop
drop _merge
drop cntyidfp cnycntpop cnycnt65o cnypct65o cnycntblk cnypctblk cnycnthis cnypcthis

"W:\GIS\Projects\hospitals\data\processing_nis\variables\niuid_ct2000_ctbuffer_co2000_census_vars_and_health_insurance.dta"
save "W:\GIS\Projects\hospitals\data\output\tables\final_hcris_nis_master\final_hcris_nis_master.dta", replace
