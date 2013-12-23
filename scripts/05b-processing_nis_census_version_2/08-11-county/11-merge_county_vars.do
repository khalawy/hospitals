use "W:\GIS\Projects\hospitals\data\processing_nis\variables\county_vars\nis_co2000_nest.dta", clear
merge m:1 co2000 using "W:\GIS\Projects\hospitals\data\processing_nis\variables\county_vars\nis_co2000_agesexrace.dta"
drop if _merge == 2
drop _merge
merge m:1 co2000 using "W:\GIS\Projects\hospitals\data\processing_nis\variables\county_vars\nis_co2000_econ.dta"
drop if _merge == 2
drop _merge
merge m:1 co2000 using "W:\GIS\Projects\hospitals\data\processing_nis\variables\county_vars\nis_co2000_education.dta"
drop if _merge == 2
drop _merge
merge m:1 co2000 using "W:\GIS\Projects\hospitals\data\processing_nis\variables\county_vars\nis_co2000_lingiso.dta"
drop if _merge == 2
drop _merge
merge m:1 co2000 using "W:\GIS\Projects\hospitals\data\processing_nis\variables\county_vars\nis_co2000_poverty.dta"
drop if _merge == 2
drop _merge
merge m:1 co2000 using "W:\GIS\Projects\hospitals\data\processing_nis\variables\county_vars\nis_co2000_health_insurance.dta"
drop if _merge == 2
drop _merge
save "W:\GIS\Projects\hospitals\data\processing_nis\variables\county_vars\nis_co2000_nest_all_vars.dta", replace
