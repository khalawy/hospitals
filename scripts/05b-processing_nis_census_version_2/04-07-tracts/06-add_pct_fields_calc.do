use "W:\GIS\Projects\hospitals\data\processing_nis\variables\tract_vars\nis_ct2000_bint_agesexrace_freq.dta" 
gen ct2000bufpct65o = ct2000bufcnt65o/ ct2000bufcntpop
gen ct2000bufpctblk = ct2000bufcntblk/ ct2000bufcntpop
gen ct2000bufpcthis = ct2000bufcnthis/ ct2000bufcntpop
save "W:\GIS\Projects\hospitals\data\processing_nis\variables\tract_vars\nis_ct2000_bint_agesexrace_freq.dta", replace
use "W:\GIS\Projects\hospitals\data\processing_nis\variables\tract_vars\nis_ct2000_bint_econ_freq.dta", clear
gen ct2000bufpctune = ct2000bufcntune/ ct2000bufcnt16o
save "W:\GIS\Projects\hospitals\data\processing_nis\variables\tract_vars\nis_ct2000_bint_econ_freq.dta", replace
use "W:\GIS\Projects\hospitals\data\processing_nis\variables\tract_vars\nis_ct2000_bint_education_freq.dta", clear
gen ct2000bufpctlhs = ct2000bufcntlhs/ ct2000bufcnt25o
save "W:\GIS\Projects\hospitals\data\processing_nis\variables\tract_vars\nis_ct2000_bint_education_freq.dta", replace
use "W:\GIS\Projects\hospitals\data\processing_nis\variables\tract_vars\nis_ct2000_bint_lingiso_freq.dta", clear
gen ct2000bufpctlin = ct2000bufcntlin/ ct2000bufcntlan
save "W:\GIS\Projects\hospitals\data\processing_nis\variables\tract_vars\nis_ct2000_bint_lingiso_freq.dta", replace
use "W:\GIS\Projects\hospitals\data\processing_nis\variables\tract_vars\nis_ct2000_bint_poverty_freq.dta", clear
gen ct2000bufpctpov = ct2000bufcntpov/ ct2000bufcntppv
save "W:\GIS\Projects\hospitals\data\processing_nis\variables\tract_vars\nis_ct2000_bint_poverty_freq.dta", replace

use "W:\GIS\Projects\hospitals\data\processing_nis\variables\tract_vars\nis_ct2000_nest_agesexrace.dta" 
gen ct2000polpct65o = ct2000polcnt65o/ ct2000polcntpop
gen ct2000polpctblk = ct2000polcntblk/ ct2000polcntpop
gen ct2000polpcthis = ct2000polcnthis/ ct2000polcntpop
save "W:\GIS\Projects\hospitals\data\processing_nis\variables\tract_vars\nis_ct2000_nest_agesexrace.dta", replace
use "W:\GIS\Projects\hospitals\data\processing_nis\variables\tract_vars\nis_ct2000_nest_econ.dta", clear
gen ct2000polpctune = ct2000polcntune/ ct2000polcnt16o
save "W:\GIS\Projects\hospitals\data\processing_nis\variables\tract_vars\nis_ct2000_nest_econ.dta", replace
use "W:\GIS\Projects\hospitals\data\processing_nis\variables\tract_vars\nis_ct2000_nest_education.dta", clear
gen ct2000polpctlhs = ct2000polcntlhs/ ct2000polcnt25o
save "W:\GIS\Projects\hospitals\data\processing_nis\variables\tract_vars\nis_ct2000_nest_education.dta", replace
use "W:\GIS\Projects\hospitals\data\processing_nis\variables\tract_vars\nis_ct2000_nest_lingiso.dta", clear
gen ct2000polpctlin = ct2000polcntlin/ ct2000polcntlan
save "W:\GIS\Projects\hospitals\data\processing_nis\variables\tract_vars\nis_ct2000_nest_lingiso.dta", replace
use "W:\GIS\Projects\hospitals\data\processing_nis\variables\tract_vars\nis_ct2000_nest_poverty.dta", clear
gen ct2000polpctpov = ct2000polcntpov/ ct2000polcntppv
save "W:\GIS\Projects\hospitals\data\processing_nis\variables\tract_vars\nis_ct2000_nest_poverty.dta", replace
