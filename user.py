#Importing files to use in this file.
import bcrypt
from bson.son import SON
import mysql.connector

class User():

    def __init__(self):
        self.conn = mysql.connector.connect(user='ted',
                                password='pass',
                                host='localhost',
                                port=3307,
                                database='movies')
        self.cursor = self.conn.cursor()

    def check(self,username, password):
        #I first encode the password to utf-8
        password = password.encode('utf-8')
        query = ("""SELECT * FROM users WHERE username = %s""")
        self.cursor.execute(query, (username,))
        row = self.cursor.fetchone()
        if str(row) == 'None':
            flag = False
        #If the user is found, then another check is done to see if the hidden
        #password matches the original one.
        else:
            #Setting the hashed variable to be used in the conditional statement.
            hashed = row[1].encode('utf-8') #This will return the hashed password from the table.
            if bcrypt.hashpw(password, hashed) == hashed:
                flag = True
        return flag


#Movies is the database, users is the table.
