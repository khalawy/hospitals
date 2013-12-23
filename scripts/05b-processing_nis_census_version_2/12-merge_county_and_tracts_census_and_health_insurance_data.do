use "W:\GIS\Projects\hospitals\data\processing_nis\variables\tract_vars\nis_ct2000_buffer_and_nest_variables.dta", clear
merge 1:1 nisuid using "W:\GIS\Projects\hospitals\data\processing_nis\variables\county_vars\nis_co2000_nest_all_vars.dta"
drop _merge
drop ct2000
save "W:\GIS\Projects\hospitals\data\processing_nis\variables\niuid_ct2000_ctbuffer_co2000_census_vars_and_health_insurance.dta", replace
