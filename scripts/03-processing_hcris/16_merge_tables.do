use E:\SpiderOak\projects\hospitals\data\output\tables\dta\hcris.dta 
merge 1:1 uid using "E:\SpiderOak\projects\hospitals\data\output\tables\dta\cny_agesexrace.dta"
drop _merge
merge 1:1 uid using "E:\SpiderOak\projects\hospitals\data\output\tables\dta\cny_econ.dta"
drop _merge
merge 1:1 uid using "E:\SpiderOak\projects\hospitals\data\output\tables\dta\cny_education.dta"
drop _merge
merge 1:1 uid using "E:\SpiderOak\projects\hospitals\data\output\tables\dta\cny_lingiso.dta"
drop _merge
merge 1:1 uid using "E:\SpiderOak\projects\hospitals\data\output\tables\dta\cny_poverty.dta"
drop _merge

save "E:\SpiderOak\projects\hospitals\data\output\tables\dta\hcris.dta", replace

merge 1:1 uid using "E:\SpiderOak\projects\hospitals\data\output\tables\dta\trt_agesexrace.dta"
drop _merge
merge 1:1 uid using "E:\SpiderOak\projects\hospitals\data\output\tables\dta\trt_econ.dta"
drop _merge
merge 1:1 uid using "E:\SpiderOak\projects\hospitals\data\output\tables\dta\trt_education.dta"
drop _merge
merge 1:1 uid using "E:\SpiderOak\projects\hospitals\data\output\tables\dta\trt_lingiso.dta"
drop _merge
merge 1:1 uid using "E:\SpiderOak\projects\hospitals\data\output\tables\dta\trt_poverty.dta"
drop _merge

save "E:\SpiderOak\projects\hospitals\data\output\tables\dta\hcris.dta", replace

merge 1:1 uid using "E:\SpiderOak\projects\hospitals\data\output\tables\dta\hrb_agesexrace.dta"
drop _merge
merge 1:1 uid using "E:\SpiderOak\projects\hospitals\data\output\tables\dta\hrb_econ.dta"
drop _merge
merge 1:1 uid using "E:\SpiderOak\projects\hospitals\data\output\tables\dta\hrb_education.dta"
drop _merge
merge 1:1 uid using "E:\SpiderOak\projects\hospitals\data\output\tables\dta\hrb_lingiso.dta"
drop _merge
merge 1:1 uid using "E:\SpiderOak\projects\hospitals\data\output\tables\dta\hrb_poverty.dta"
drop _merge

save "E:\SpiderOak\projects\hospitals\data\output\tables\dta\hcris.dta", replace

merge 1:1 uid using "E:\SpiderOak\projects\hospitals\data\output\tables\dta\cny_health_ins.dta"
drop _merge

save "E:\SpiderOak\projects\hospitals\data\output\tables\dta\hcris.dta", replace
