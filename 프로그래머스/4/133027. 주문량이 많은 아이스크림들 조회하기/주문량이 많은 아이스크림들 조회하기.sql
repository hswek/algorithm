-- 코드를 입력하세요
SELECT FLAVOR
FROM 
(
SELECT FLAVOR,SUM(TOTAL_ORDER) FROM (SELECT * FROM FIRST_HALF UNION SELECT * FROM JULY)
GROUP BY FLAVOR 
ORDER BY SUM(TOTAL_ORDER) DESC
)
WHERE ROWNUM<=3