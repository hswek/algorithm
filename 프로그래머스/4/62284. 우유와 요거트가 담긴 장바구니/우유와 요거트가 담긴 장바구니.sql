-- 코드를 입력하세요
--WITH T AS 

SELECT CART_ID
FROM CART_PRODUCTS
WHERE NAME IN ('Milk','Yogurt')
GROUP BY CART_ID
HAVING COUNT(DISTINCT NAME) =2
ORDER BY CART_ID

/*
SELECT DISTINCT CART_ID 
FROM CART_PRODUCTS E
where (select count(*) from T where T.CART_ID=CART_ID)>=2
*/