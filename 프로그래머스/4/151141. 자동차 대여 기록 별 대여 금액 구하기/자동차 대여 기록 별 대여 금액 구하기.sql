-- 코드를 입력하세요
SELECT HISTORY_ID,
CASE 
WHEN H.END_DATE-H.START_DATE<7 THEN TRUNC(C.DAILY_FEE* ((END_DATE-START_DATE)+1),0)
WHEN H.END_DATE-H.START_DATE>=7 AND H.END_DATE-H.START_DATE<30 THEN TRUNC(C.DAILY_FEE* ((END_DATE-START_DATE)+1)
*(100-(SELECT REGEXP_REPLACE(DISCOUNT_RATE,'[^0-9]')
  FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN P 
  WHERE C.CAR_TYPE=P.CAR_TYPE AND DURATION_TYPE='7일 이상'))/100,0)
WHEN H.END_DATE-H.START_DATE>=30 AND H.END_DATE-H.START_DATE<90 THEN TRUNC(C.DAILY_FEE* ((END_DATE-START_DATE)+1)
*(100-(SELECT REGEXP_REPLACE(DISCOUNT_RATE,'[^0-9]')
  FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN P 
  WHERE C.CAR_TYPE=P.CAR_TYPE AND DURATION_TYPE='30일 이상'))/100,0)

WHEN H.END_DATE-H.START_DATE>=90 THEN TRUNC(C.DAILY_FEE* ((END_DATE-START_DATE)+1)
*(100-(SELECT REGEXP_REPLACE(DISCOUNT_RATE,'[^0-9]')
  FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN P 
  WHERE C.CAR_TYPE=P.CAR_TYPE AND DURATION_TYPE='90일 이상'))/100,0)
 END
AS FEE
FROM CAR_RENTAL_COMPANY_CAR C ,  CAR_RENTAL_COMPANY_RENTAL_HISTORY H
WHERE C.CAR_ID=H.CAR_ID AND C.CAR_TYPE='트럭'
ORDER BY FEE DESC,HISTORY_ID DESC