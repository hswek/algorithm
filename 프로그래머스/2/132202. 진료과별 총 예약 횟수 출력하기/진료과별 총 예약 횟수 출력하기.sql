-- 코드를 입력하세요
SELECT MCDP_CD,COUNT(*)
FROM APPOINTMENT 
WHERE TO_CHAR(APNT_YMD,'YYYY-MM')='2022-05'
GROUP BY MCDP_CD	
ORDER BY COUNT(*),MCDP_CD