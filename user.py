#Importing files to use in this file.
import bcrypt
from bson.son import SON
import mysql.connector
#import pymysql

class User():

    def __init__(self):
        self.conn = mysql.connector.connect(user='ted',
                                password='pass',
                                host='localhost',
                                port=3306,
                                database='movies')
        self.cursor = self.conn.cursor()

    #This method checks to see if the user name is in the table.
    def check(self, username, password):
        #I first encode the password to utf-8
        password = password.encode('utf-8')
        #This query really does not work sense I could have multiple entries
        #of the same user name. I did not realize this on earlier projects and
        #I think for now on I will not use this as much but instead some pre made
        #authentication system.
        query = ("""SELECT * FROM users WHERE username = %s""")
        self.cursor.execute(query, (username,))
        row = self.cursor.fetchone()
        if str(row) == 'None':
            print(row)
            flag = False
        #If the user is found, then another check is done to see if the hidden
        #password matches the original one.
        else:
            print(row)
            #Setting the hashed variable to be used in the conditional statement.
            hashed = row[1].encode('utf-8') #This will return the hashed password from the table.
            if bcrypt.hashpw(password, hashed) == hashed:
                flag = True
            #This is a final 'catch all' to prevent an error from occuring if
            #there is no match in the database. The query above should really be
            #matching by both user name and password. 
            else:
                flag = False
        return flag

    #This method will encrypt the password
    def encrypt_pass(self, password):
        password = password.encode('utf-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        return password, hashed

      #This method will insert a new user into the database.
    def insert(self, username, hashed):
        self._SQL = """insert into users
          (username, password)
          values
          (%s, %s)"""
        self.cursor.execute(self._SQL, (username, hashed))
        self.conn.commit()


#Movies is the database, users is the table.
