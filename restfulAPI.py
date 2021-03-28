from flask import Flask
from flask_restful import Resource,Api,reqparse
import sqlite3

app = Flask(__name__)
api = Api(app)

#arguments required for put request to add data
addDataArgs = reqparse.RequestParser()
addDataArgs.add_argument("studentID",type=int,help="Student Number",required=True)
addDataArgs.add_argument("firstName",type=str,help="Student first name",required=True)
addDataArgs.add_argument("lastName",type=str,help="Student last name",required=True)
addDataArgs.add_argument("dob",type=str,help="Student Date of Birth",required=True)
addDataArgs.add_argument("amountDue",type=str,help="Amount Student owes",required=True)

#for showing all records
class dbmAll(Resource):
    def get(self):
        pass

#for add/update/delete/and view database records
class dbm(Resource):
    def get(self):
        return  {"name":"hello world"}

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
        return  {"name":"hello world 3"}

    def delete(self):
        return  {"name":"hello world 4"}



api.add_resource(dbm,'/')
api.add_resource(dbmAll,'/all')



if __name__ == '__main__':
    app.run(port=8080, debug=True)
