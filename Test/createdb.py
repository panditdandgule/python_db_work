import sqlite3
import csv

import mysql.connector
print('connected')


conn = mysql.connector.connect(host="localhost", user="root",   password ="", database="ORG")
print('MydbName:',conn)

db_name = 'ORG'
table_name = 'sn_buy_rated'
# Create a cursor (an instance) to manipulate your SQL Database
mycursor = conn.cursor(buffered=True)

mycursor.execute('SHOW DATABASES')
for x in mycursor:
     print(x)

# Create new Table
mycursor.execute(f'DROP TABLE IF EXISTS {table_name}')
mycursor.execute(f"create table {table_name} (last_known_ticker varchar(10), record_date VARCHAR(50), un_adj_ticker varchar(10), ec_unique_sec varchar(15), unique_id varchar(20), name varchar(50), un_adj_price decimal(8,2), 1mf_total_ret decimal(8,5), fset_perm_id varchar(50), eps_mom varchar(8), mean_valuation_deviation decimal(8,5), mpt_class varchar(2), gics_sector varchar(75), 1yf_total_ret decimal(8,5), isin varchar(50), sedol varchar(50), adv_mil decimal(8,5), vbeta decimal(8,5), vba_mvd decimal(8,5), svi_2_score decimal(8,5), svi_2_grade varchar(1))")
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)