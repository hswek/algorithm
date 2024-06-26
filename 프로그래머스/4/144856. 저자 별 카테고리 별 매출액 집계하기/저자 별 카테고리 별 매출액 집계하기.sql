-- 코드를 입력하세요
SELECT A.AUTHOR_ID,AUTHOR_NAME,CATEGORY, SUM( PRICE * (SELECT SUM(SALES) FROM BOOK_SALES S WHERE S.BOOK_ID=B.BOOK_ID AND TO_CHAR(SALES_DATE,'YYYY-MM')='2022-01'))
FROM BOOK B,AUTHOR A
WHERE B.AUTHOR_ID=A.AUTHOR_ID 
GROUP BY A.AUTHOR_ID,AUTHOR_NAME,CATEGORY
ORDER BY AUTHOR_ID,CATEGORY DESC