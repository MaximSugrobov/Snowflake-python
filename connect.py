import os
import snowflake.connector

PASSWORD = os.getenv('SNOWSQL_PWD')

# Connecting to my Snowflake account
'''conn = snowflake.connector.connect(
    user='MAXIMSUGROBOV',
    password=PASSWORD,
    account='sa01279.europe-west4.gcp',
    session_parameters={
        'QUERY_TAG': 'EndOfMonthFinancials'
    }
)

# Creating and using the WH
conn.cursor().execute('CREATE WAREHOUSE IF NOT EXISTS my_new_wh')
conn.cursor().execute('USE WAREHOUSE my_new_wh')

# Creating and using the DB
conn.cursor().execute('CREATE DATABASE IF NOT EXISTS my_new_db')
conn.cursor().execute('USE DATABASE my_new_db')

# Creating and using schemas
conn.cursor().execute('CREATE SCHEMA IF NOT EXISTS my_schema')
conn.cursor().execute('USE SCHEMA my_schema')

# Creating a table
conn.cursor().execute(
    'CREATE OR REPLACE TABLE '
    'my_table(col1 integer, col2 string, col3 boolean)')

# Inserting data
conn.cursor().execute(
    "INSERT INTO my_table(col1, col2, col3) "
    "VALUES(10, 'string_1', true),(20, 'string_2', false)")

# Query data
col1, col2, col3 = conn.cursor().execute("Select col1, col2, col3 from my_table").fetchone()
print(f'{col1}, {col2}, {col3}')

for (col1, col2, col3) in conn.cursor().execute("select col1, col2, col3 from my_table"):
    print(f'{col1}, {col2}, {col3}')
conn.close()'''
