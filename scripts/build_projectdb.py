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
    with open(os.path.join("sql", "import_data.sql")) as file:
        commands = file.readlines()

        # Pre-process the CSV file to handle empty values
        with open(os.path.join("data", "cleaned_tickets.csv"), "r") as data_file:
            # Read the file and replace empty numeric fields with NULL
            lines = data_file.readlines()
            processed_lines = []
            header = lines[0]
            processed_lines.append(header)
            
            for line in lines[1:]:
                parts = line.strip().split(',')
                # Handle empty price field (column 8)
                if len(parts) > 8 and parts[8] == '""' or parts[8] == '':
                    parts[8] = 'NULL'
                processed_lines.append(','.join(parts))
            
            # Create a temporary processed file
            temp_file = os.path.join("data", "processed_dataset.csv")
            with open(temp_file, "w") as f:
                f.write('\n'.join(processed_lines))
            
            # Import the processed file
            with open(temp_file, "r") as clean_file:
                # Skip header
                next(clean_file)
                cur.copy_expert(commands[0], clean_file)
            
            # Remove temporary file
            os.remove(temp_file)

    conn.commit()

    # Test the database
    cur = conn.cursor()
    with open(os.path.join("sql", "test_database.sql")) as file:
        commands = file.readlines()
        for command in commands:
            cur.execute(command)
            pprint(cur.fetchall())