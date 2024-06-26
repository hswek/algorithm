SELECT USER_ID, NICKNAME, SUM(PRICE) AS S
FROM USED_GOODS_BOARD,USED_GOODS_USER
WHERE WRITER_ID=USER_ID AND STATUS='DONE'
GROUP BY USER_ID,NICKNAME
HAVING SUM(PRICE)>=700000
ORDER BY S