import mysql.connector

db = mysql.connector.connect(
    user='root',
    host='localhost',
    password='',
    port=3306,
    database="python-jun-1"
)

terminal = db.cursor()

# INSERT
insert = "INSERT INTO pythonjun1 (name, sddress, phone, age) VALUES ('sanjay','sisaiya','12365','25'),('Kapil','sisaiya','456321','30')"
terminal.execute(insert)
db.commit()

# DELETE
dequery = "DELETE FROM pythonjun1 WHERE name='sanjay'"
terminal.execute(dequery)
db.commit()

# ALTER TABLE
upquery = "ALTER TABLE pythonjun1 ADD COLUMN `email` VARCHAR(100)"
emailupdate="UPDATE TABLE pythonjun1 email='kapildevjoshi2@gmail.com'"
terminal.execute(upquery)
terminal.execute(emailupdate)

#UPDATE SPECIFIC USER ONLY 
upuser="UPDATE TABLE pythonjun1 "

# SELECT (LAST step)
query = "SELECT * FROM pythonjun1"
terminal.execute(query)

result = terminal.fetchall()
print(result)