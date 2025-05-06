import psycopg2 as psql
from pprint import pprint
import os

# Read password from secrets file
password = "hgVwomtl0OIAe7cF"

# build connection string
conn_string = "host=hadoop-04.uni.innopolis.ru port=5432 user=team17 dbname=team17_projectdb password={}".format(password)

# Connect to the remote dbms
with psql.connect(conn_string) as conn:
    # Create a cursor for executing psql commands
    cur = conn.cursor()
    
    # Read and execute table creation commands
    with open(os.path.join("sql", "create_tables.sql")) as file:
        content = file.read()
        cur.execute(content)
    conn.commit()

    # Import data with proper NULL handling
    with open(os.path.join("data", "cleaned_tickets.csv"), "r") as f:
        # Skip header
        next(f)
        cur.copy_expert("COPY train_tickets FROM STDIN WITH CSV NULL AS 'NULL'", f)
    
    conn.commit()

    # Test the database
    cur = conn.cursor()
    with open(os.path.join("sql", "test_database.sql")) as file:
        commands = file.readlines()
        for command in commands:
            cur.execute(command)
            pprint(cur.fetchall())