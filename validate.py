import os
import snowflake.connector

PASSWORD = os.getenv('SNOWSQL_PWD')

ctx = snowflake.connector.connect(
    user='MAXIMSUGROBOV',
    password=PASSWORD,
    account='sa01279.europe-west4.gcp'
    )
cs = ctx.cursor()
try:
    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    print(one_row[0])
finally:
    cs.close()
ctx.close()
