-- 코드를 입력하세요
SELECT *
FROM (SELECT I.ANIMAL_ID,I.NAME
FROM ANIMAL_INS I, ANIMAL_OUTS O 
WHERE I.ANIMAL_ID=O.ANIMAL_ID AND I.ANIMAL_ID IN (SELECT ANIMAL_ID FROM ANIMAL_OUTS)
ORDER BY O.DATETIME-I.DATETIME DESC)
WHERE ROWNUM<=2