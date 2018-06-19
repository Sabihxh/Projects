#To get all table names where tables are not empty
SELECT table_name 
FROM information_schema.tables 
WHERE table_rows >= 1 
AND TABLE_SCHEMA='alanklinkhoff'

SELECT table_name 
FROM information_schema.tables 
WHERE table_rows >= 1 
AND TABLE_SCHEMA='officebaroque'

SELECT table_name 
FROM information_schema.tables 
WHERE table_rows >= 1 
AND TABLE_SCHEMA='esthellaprovas'

SELECT table_name 
FROM information_schema.tables 
WHERE table_rows >= 1 
AND TABLE_SCHEMA='froelickgallery'

SELECT table_name 
FROM information_schema.tables 
WHERE table_rows >= 1 
AND TABLE_SCHEMA='johnnoott'

SELECT table_name 
FROM information_schema.tables 
WHERE table_rows >= 1 
AND TABLE_SCHEMA='michaelhoppengallery'

SELECT table_name 
FROM information_schema.tables 
WHERE table_rows >= 1 
AND TABLE_SCHEMA='pontone'


