use "W:\GIS\Projects\hospitals\data\processing_nis\variables\county_vars\nis_co2000_agesexrace.dta", clear 
gen co2000polpct65o = co2000polcnt65o/ co2000polcntpop
gen co2000polpctblk = co2000polcntblk/ co2000polcntpop
gen co2000polpcthis = co2000polcnthis/ co2000polcntpop
gen co2000 = GEO_id
replace co2000 = subinstr(co2000, "0500000US", "",.)
drop GEO_id
save "W:\GIS\Projects\hospitals\data\processing_nis\variables\county_vars\nis_co2000_agesexrace.dta", replace

use "W:\GIS\Projects\hospitals\data\processing_nis\variables\county_vars\nis_co2000_econ.dta", clear
gen co2000polpctune = co2000polcntune/ co2000polcnt16o
gen co2000 = GEO_id
replace co2000 = subinstr(co2000, "0500000US", "",.)
drop GEO_id
save "W:\GIS\Projects\hospitals\data\processing_nis\variables\county_vars\nis_co2000_econ.dta", replace

use "W:\GIS\Projects\hospitals\data\processing_nis\variables\county_vars\nis_co2000_education.dta", clear
gen co2000polpctlhs = co2000polcntlhs/ co2000polcnt25o
gen co2000 = GEO_id
replace co2000 = subinstr(co2000, "0500000US", "",.)
drop GEO_id
save "W:\GIS\Projects\hospitals\data\processing_nis\variables\county_vars\nis_co2000_education.dta", replace

use "W:\GIS\Projects\hospitals\data\processing_nis\variables\county_vars\nis_co2000_lingiso.dta", clear
gen co2000polpctlin = co2000polcntlin/ co2000polcntlan
gen co2000 = GEO_id
replace co2000 = subinstr(co2000, "0500000US", "",.)
drop GEO_id
save "W:\GIS\Projects\hospitals\data\processing_nis\variables\county_vars\nis_co2000_lingiso.dta", replace

use "W:\GIS\Projects\hospitals\data\processing_nis\variables\county_vars\nis_co2000_poverty.dta", clear
gen co2000polpctpov = co2000polcntpov/ co2000polcntppv
gen co2000 = GEO_id
replace co2000 = subinstr(co2000, "0500000US", "",.)
drop GEO_id
save "W:\GIS\Projects\hospitals\data\processing_nis\variables\county_vars\nis_co2000_poverty.dta", replace

use "W:\GIS\Projects\hospitals\data\processing_nis\variables\county_vars\nis_co2000_health_insurance.dta", clear
gen co2000 = geoid
drop if co2000 == ""
drop postal state county
save "W:\GIS\Projects\hospitals\data\processing_nis\variables\county_vars\nis_co2000_health_insurance.dta", replace
