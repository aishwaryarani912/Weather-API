def create_db(cursor,dataBaseName):
    db=f"create database {dataBaseName}"
    cursor.execute(db)
def create_table(cursor,Weather_info):
    tb=f"create TABLE IF NOT EXISTS {Weather_info} (Temperature float,Weather varchar(1000),Min_temp float,Max_temp float,Datetime varchar(100),Icon varchar(100));"
    cursor.execute(tb)
def insert_table(cursor,tb_name,lst):
    insert_query=f"INSERT INTO {Weather_info} (Temperature,Weather,Min_temp,Max_temp,Datetime,Icon) VALUES(%(Temperature)s,%(Weather)s,%(Min_temp)s ,%(Max_temp)s,%(Datetime)s,%(Icon)s);"
    cursor.executemany(insert_query,lst)