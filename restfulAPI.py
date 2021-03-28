from flask import Flask
from flask_restful import Resource,Api,reqparse
import sqlite3

app = Flask(__name__)
api = Api(app)


#arguments required for get reqest to get a specific students info
getDataArgs = reqparse.RequestParser()
getDataArgs.add_argument("studentID",type=int,help="Student Number",required=True)


#arguments required for put request to add data
addDataArgs = reqparse.RequestParser()
addDataArgs.add_argument("studentID",type=int,help="Student Number",required=True)
addDataArgs.add_argument("firstName",type=str,help="Student first name",required=True)
addDataArgs.add_argument("lastName",type=str,help="Student last name",required=True)
addDataArgs.add_argument("dob",type=str,help="Student Date of Birth",required=True)
addDataArgs.add_argument("amountDue",type=str,help="Amount Student owes",required=True)


#arguments required for delete request to delete data
delDataArgs = reqparse.RequestParser()
delDataArgs.add_argument("studentID",type=int,help="Student Number",required=True)

#arguments required for put request to update data
putDataArgs = reqparse.RequestParser()
putDataArgs.add_argument("studentID",type=int,help="Student Number",required=True)
putDataArgs.add_argument("firstName",type=str,help="Student first name",required=True)
putDataArgs.add_argument("lastName",type=str,help="Student last name",required=True)
putDataArgs.add_argument("dob",type=str,help="Student Date of Birth",required=True)
putDataArgs.add_argument("amountDue",type=str,help="Amount Student owes",required=True)


#for showing all records
class dbmAll(Resource):
    def get(self):
        #create connection to database. Will be created if it doesnt exist
        conn = sqlite3.connect('studentInfo.db')

        #create cursor instance
        c = conn.cursor()

        c.execute("SELECT studentID, firstName, lastName, dateOfBirth, amountDue FROM Student")
        a = c.fetchall()

        #save the changes
        conn.commit()
        #close the connection
        conn.close()

        return  {"All records":a}

#for add/update/delete/and view database records
class dbm(Resource):
    def get(self):
        args = getDataArgs.parse_args()
        #create connection to database. Will be created if it doesnt exist
        conn = sqlite3.connect('studentInfo.db')

        #create cursor instance
        c = conn.cursor()

        c.execute("SELECT studentID, firstName, lastName, dateOfBirth, amountDue FROM Student")
        a = c.fetchone()

        #save the changes
        conn.commit()
        #close the connection
        conn.close()

        return  {"Found":a}

    def post(self):
        args = addDataArgs.parse_args()
        #create connection to database. Will be created if it doesnt exist
        conn = sqlite3.connect('studentInfo.db')

        #create cursor instance
        c = conn.cursor()

        c.execute("""INSERT INTO Student (studentID, firstName, lastName, dateOfBirth, amountDue)
                    VALUES(?,?,?,?,?)""",
                    (args["studentID"],args["firstName"],args["lastName"],args["dob"],args["amountDue"]))

        #save the changes
        conn.commit()
        #close the connection
        conn.close()

        return  {"Added":args}

    def put(self):
        args = putDataArgs.parse_args()

        conn = sqlite3.connect('studentInfo.db')
        c = conn.cursor()

        c.execute("""UPDATE Student SET firstName=?, lastName=?, dateOfBirth=?, amountDue=? WHERE studentID=? """,
                   (args["firstName"],args["lastName"],args["dob"],args["amountDue"],args["studentID"]))


        conn.commit()
        conn.close()

        return  {"UPDATED":args}


    def delete(self):

        args = delDataArgs.parse_args()

        conn = sqlite3.connect('studentInfo.db')
        c = conn.cursor()

        c.execute("DELETE FROM Student WHERE studentID=?", (args["studentID"],))

        conn.commit()
        conn.close()

        return  {"Deleted":args}



api.add_resource(dbm,'/')
api.add_resource(dbmAll,'/all')

if __name__ == '__main__':
    app.run(port=8080, debug=True)
