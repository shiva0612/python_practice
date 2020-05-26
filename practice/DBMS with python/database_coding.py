import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "0612",
    database = "shiva"
)

l = [(),(),()]
csr = db.cursor()
csr.executemany("""
insert into new_table(name,fname,mname) values(?,?,?) # here, instead of ? we can also use %s
""",l)

name = "shiva"
with open("shiva.png","rb") as f:
    data = f.read()

csr.execute("""
create table images_table(name text , data BLOB)
""")

csr.executemany("""
insert into images_table(name,data) values(?,?)
""",(name,data))

csr.execute("select * from images_table")
print(csr.fetchall())

csr.execute("select * from new_table")
r = csr.fetchall()
for i in r:
    print(i)

csr.execute("select * from images_table")
t = csr.fetchall()
for i in t:
    print(t)

db.commit()

# important note:
# insert ,commit,see the data (this is the sequence you need to follow if you want to insert and see the data in a single file)
# if you write insert,see the data ,commit (you cannot see the newly inserted data because it has not been commited)
db.close()
