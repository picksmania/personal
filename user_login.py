import jwt
import MySQLdb

class user_login():
    def __init__(self,hostname,username,password,dbname):
          self.hostname = hostname
          self.username = username
          self.password = password
          self.dbname = dbname


    def db_connection(self):
          # Open database connection
          try:
                database = MySQLdb.connect(self.hostname,self.username,self.password,self.dbname)
                # prepare a cursor object using cursor() method
                cursor = database.cursor()
                print "Successfully able to connect to database...."
                return True
          except Exception,e:
                print "Unable to connect to Database...",e
                return False

    def user_login(self):
        try:
            username = raw_input("Please enter your username")
            password = raw_input("Please enter your password")

        except Exception  as e:
            print e


if __name__ == '__main__':
    obj = user_login('localhost','root','HPQ12345','SKP_database')
    obj.db_connection()