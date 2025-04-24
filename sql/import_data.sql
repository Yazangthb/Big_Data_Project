-- always test if you can import the data from PgAdmin then you automate it by writing the script
COPY depts FROM STDIN WITH CSV HEADER DELIMITER ',' NULL AS 'null';

COPY emps FROM STDIN WITH CSV HEADER DELIMITER ',' NULL AS 'null';
