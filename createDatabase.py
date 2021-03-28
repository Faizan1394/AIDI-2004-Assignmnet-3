import sqlite3

#create connection to database. Will be created if it doesnt exist
conn = sqlite3.connect('studentInfo.db')

#create cursor instance
c = conn.cursor()

#Create the table
c.execute("""Create Table Student (
           studentID INTEGER PRIMARY KEY,
           firstName TEXT,
           lastName TEXT,
           dateOfBirth TEXT,
           amountDue REAL
         )""")

#save the changes
conn.commit()

#close the connection
conn.close()