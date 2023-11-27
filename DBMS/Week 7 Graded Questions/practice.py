# import psycopg2

# conn = None

# try:
#     conn = psycopg2.connect(database = 'test', user = 'postgres', password = 'admin', host = '127.0.0.1', port = '5432')
#     print("Database Connected Succesfully\n")
# except (Exception, psycopg2.DatabaseError) as error:
#     print("Some error")
# # finally:
# #     if conn is not None:
# #         # conn.close()
# #     else:
# #         pass




# # Create Table
# curr = conn.cursor()
# curr.execute('''create table colors (colorId varchar(10) primary key,
#              color varchar(20),
#              type varchar(10),
#              rateIt int)''')
# conn.commit()
# print("Table Created Succesfully\n")
# conn.close()




# # Insert data into table
# curr = conn.cursor()

# # # Insert singel row
# # curr.execute('''INSERT INTO colors (colorId, color, type, rateIt) VALUES ('1f6feb', 'Blue', 'Medium', 8)''')
# # curr.execute('''Insert into colors values('1f6feb', 'Blue', 'Medium', '8')''')

# Insert multiple rows
# curr.execute('''INSERT INTO colors (colorId, color, type, rateIt) 
#                             VALUES ('ea5fff', 'Purple', 'Good', 9),
#                                     ('ff0000', 'Red', 'Good', 7),
#                                     ('00f002', 'Green', 'Good', 9)''')

# curr.execute('''Insert into colors values('1f6fec', 'Blue', 'Medium', '8')''')

# conn.commit()
# print("Data Inserted Succesfully\n")
# conn.close()




# # Delete data from table

# def delete_row_byId(id):
#     curr = conn.cursor()
#     curr.execute(f"delete from colors where colorId = {id}")
#     conn.commit()
# print("Data Deleted Succesfully\n")
#     conn.close()

# delete_row_byId("'1f6fec'")


# # Update data in table
# def update_data(colorId, type):
#     curr = conn.cursor()
#     curr.execute(f"update colors set type = '{type}' where colorId = '{colorId}'")
#     conn.commit()
# print("Data Deleted Succesfully\n")
#     conn.close()

# update_data("00f002", "Average")


# # show all data of table

# def show(table):
#     curr = conn.cursor()
#     curr.execute(f"select * from {table}")
#     result = curr.fetchall()
#     # for i in result:
#     #     print(i[0],",",i[1],",",i[2],",",i[3])
#     print(result)
#     # print("Data Fetched Succesfully\n")
#     conn.close()

# show("colors")





# import psycopg2

# conn = None

# try:
#     conn = psycopg2.connect(database = 'FLIS', user = 'postgres', password = 'admin', host = '127.0.0.1', port = '5432')
#     print("Database Connected Succesfully\n")
# except (Exception, psycopg2.DatabaseError) as error:
#     print("Some error")
# # finally:
# #     if conn is not None:
# #         # conn.close()
# #     else:
# #         pass

# curr = conn.cursor()
# curr.execute('''
# select players.name as player_name, teams.name as team_name from players left join teams on players.team_id = teams.team_id where jersey_no in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97) order by player_name desc, team_name desc
#              ''')
# result = curr.fetchall()
# for x in result:
#     print(x[0],", ",x[1])

# conn.close()



import pandas as pd
a = {'t1':[3,2,3,4,5], 't2': [4,65,6,6,3]}
print(pd.DataFrame(a))
aa = pd.DataFrame(a)

for x in range(len(list(aa['t1']))):
    if aa['t2'][x] % 2 == 0:
        print(aa['t2'][x], " : ", "Even")
    else:
        print(aa['t2'][x], " : ", "Odd")


# import pandas as pd

# a = {'t1': [3, 2, 3, 4, 5], 't2': [4, 65, 6, 6, 3]}
# print(pd.DataFrame(a))
# aa = pd.DataFrame(a)

# for x in range(len(list(aa['t1']))):
#     if aa['t2'][x] % 2 == 0:
#         print(aa['t2'][x], " : ", "Even")
#     else:
#         print(aa['t2'][x], " : ", "Odd")



# import sys
# import os
# import psycopg2

# database = sys.argv[1]
# user = os.environ.get('PGUSER') 
# password = os.environ.get('PGPASSWORD') 
# host = os.environ.get('PGHOST')
# port = os.environ.get('PGPORT')

# try:
#     conn = psycopg2.connect(database = database, user = user, password = password, host = host, port = port)
#     # print("Database Connected Succesfully")
# except (Exception, psycopg2.DatabaseError) as error:
#     print("Some error")
# # finally:
# #     if conn is not None:
# #         conn.close()

# cur = conn.cursor()
# cur.execute('''
# select players.name as player_name, teams.name as team_name from players left join teams on players.team_id = teams.team_id where jersey_no in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
#              ''')
# result = cur.fetchall()
# for x in result:
#     print(x[0],", ",x[1])
# # print(result)
# conn.close()
