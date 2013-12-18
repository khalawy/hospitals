use W:\GIS\Projects\hospitals\data\output\tables\hcris_nis_relationship\hcris_hospitals_with_nisuid.dta 

drop  Match_addr street city state zip county hospname prov_num urban_rural po_box prvdr_ctrl_type_cd prvdr_num fy_bgn_dt fy_end_dt proc_dt fi_creat_dt npr_dt fi_rcpt_dt fyear

drop  addr_concate_str addr_concate_str_dup addr_match_prv_dup

gen nisuid = nsuid

drop nsuid

save "W:\GIS\Projects\hospitals\data\output\tables\hcris_nis_relationship\hcris_uid_and_nisuid.dta", replace