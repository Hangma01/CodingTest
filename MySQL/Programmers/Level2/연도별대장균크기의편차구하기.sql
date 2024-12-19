SELECT B.YEAR, (MAX_SIZE - A.SIZE_OF_COLONY) AS YEAR_DEV, ID
FROM ECOLI_DATA A
LEFT JOIN (SELECT YEAR(DIFFERENTIATION_DATE) AS YEAR, MAX(SIZE_OF_COLONY) AS MAX_SIZE
          FROM ECOLI_DATA
          GROUP BY YEAR(DIFFERENTIATION_DATE)) B
ON YEAR(A.DIFFERENTIATION_DATE) = B.YEAR
ORDER BY B.YEAR, YEAR_DEV