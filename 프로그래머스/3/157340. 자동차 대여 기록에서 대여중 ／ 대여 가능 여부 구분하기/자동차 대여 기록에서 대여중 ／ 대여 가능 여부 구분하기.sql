-- 코드를 입력하세요
SELECT DISTINCT CAR_ID, 
CASE 
WHEN CAR_ID 
IN ( SELECT CAR_ID
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE TO_DATE('2022-10-16','YYYY-MM-DD')>=START_DATE AND TO_DATE('2022-10-16','YYYY-MM-DD')<=END_DATE 
GROUP BY CAR_ID)
THEN '대여중'
ELSE '대여 가능'
END
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
ORDER BY CAR_ID DESC