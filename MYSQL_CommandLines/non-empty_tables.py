#To get all table names where tables are not empty

SELECT table_name 
FROM information_schema.tables 
WHERE table_rows >= 1 
AND TABLE_SCHEMA='alanklinkhoff'

SELECT table_name 
FROM information_schema.tables 
WHERE table_rows >= 1 
AND TABLE_SCHEMA='ivde'

SELECT table_name 
FROM information_schema.tables 
WHERE table_rows >= 1 
AND TABLE_SCHEMA='nac'