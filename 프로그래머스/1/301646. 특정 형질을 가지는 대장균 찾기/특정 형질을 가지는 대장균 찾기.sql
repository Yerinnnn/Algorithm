SELECT COUNT(*) AS COUNT
FROM ECOLI_DATA
WHERE (2 & GENOTYPE = 0) AND ((1 & GENOTYPE != 0) OR (4 & GENOTYPE != 0));