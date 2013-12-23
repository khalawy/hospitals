use "W:\GIS\Projects\hospitals\data\processing_nis\variables\tract_vars\nis_ct2000_nest_agesexrace.dta", clear
merge 1:1 nisuid using "W:\GIS\Projects\hospitals\data\processing_nis\variables\tract_vars\nis_ct2000_bint_agesexrace_freq.dta"
drop _merge
merge 1:1 nisuid using "W:\GIS\Projects\hospitals\data\processing_nis\variables\tract_vars\nis_ct2000_nest_econ.dta"
drop _merge
merge 1:1 nisuid using "W:\GIS\Projects\hospitals\data\processing_nis\variables\tract_vars\nis_ct2000_bint_econ_freq.dta"
drop _merge
merge 1:1 nisuid using "W:\GIS\Projects\hospitals\data\processing_nis\variables\tract_vars\nis_ct2000_nest_education.dta"
drop _merge
merge 1:1 nisuid using "W:\GIS\Projects\hospitals\data\processing_nis\variables\tract_vars\nis_ct2000_bint_education_freq.dta"
drop _merge
merge 1:1 nisuid using "W:\GIS\Projects\hospitals\data\processing_nis\variables\tract_vars\nis_ct2000_nest_lingiso.dta"
drop _merge
merge 1:1 nisuid using "W:\GIS\Projects\hospitals\data\processing_nis\variables\tract_vars\nis_ct2000_bint_lingiso_freq.dta"
drop _merge
merge 1:1 nisuid using "W:\GIS\Projects\hospitals\data\processing_nis\variables\tract_vars\nis_ct2000_nest_poverty.dta"
drop _merge
merge 1:1 nisuid using "W:\GIS\Projects\hospitals\data\processing_nis\variables\tract_vars\nis_ct2000_bint_poverty_freq.dta"
drop _merge

save "W:\GIS\Projects\hospitals\data\processing_nis\variables\tract_vars\nis_ct2000_buffer_and_nest_variables.dta", replace
