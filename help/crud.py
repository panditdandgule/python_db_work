#import the sqlit package

import sqlite3

#create a database named backup
cnt=sqlite3.connect("backup.dp")

#create a table named gfg
#cnt.execute('''CREATE TABLE gfg(NAME TEXT,POINTS INTEGER,ACCURACY REAL);''')

# insert in default order
cnt.execute('''INSERT INTO gfg VALUES(
'Count Inversion',20,80.5);''')

# insert in different order
cnt.execute('''INSERT INTO gfg(ACCURACY, POINTS, NAME) VALUES(
90.5, 15, 'Kadanes Algo');''')

cnt.execute('''INSERT INTO gfg(NAME, ACCURACY, POINTS) VALUES(
'REVERSE STR', 100, 5);''')

# commit changes to the database
cnt.commit()
