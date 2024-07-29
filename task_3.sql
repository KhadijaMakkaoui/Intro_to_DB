-- This script will list all tables in the specified database
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'alx_book_store';

