SELECT * FROM NCMCODM.TAI_NCMS_IFS_COLLECT_MAP
SELECT * FROM NCMCODM.TAI_NCMS_IFS_COLLECT_NE
SELECT T.*,ROWID FROM NCMCODM.TAI_NCMS_IFS_COLLECT_INST T WHERE ORDER_ID IN ('04336ab1-e645-44b0-a70e-9c11a348e110')(SELECT ODM_ORDER_ID FROM NCMCODM.TAI_NCMS_IFS_ODM_ORDER_MAP WHERE PR_ORDER_ID IN ('02fdf529-fd18-4e60-8687-e5e1b6fe3685'));
SELECT T.*,ROWID FROM NCMCODM.TAI_NCMS_IFS_COLLECT_REPORT T where grp_order_id = '45d05641-9a35-4b6a-a2f1-c341646ba18e'
SELECT T.*,ROWID FROM NCMCODM.TAI_NCMS_IFS_COLLECT_REPORT T where zip_path like '%2020-09%GS%' or zip_path like '%2020-09%DS%' 
grp_order_id = '45d05641-9a35-4b6a-a2f1-c341646ba18e'
select * from ncmcodm.tai_ncms_ifs_grp_order where task_id LIKE '%_%'
select * from ncmcodm.tai_ncms_ifs_grp_check_task 
select * from ncmcodm.tai_ncms_ifs_pr_order
D:\Installed programs\PycharmProjects\pyStudy\爬虫\案例>python 20小说网.py