import mysql.connector
db = mysql.connector.connect(user="root", passwd='pwd', db="UserDB")

cursor = db.cursor()


class Mysqlhandler:
    def __init__(self):
        pass
    def add_user(self,value1,value2,value3):
        query="INSERT INTO user_data values('{}',{},'{}')".format(value1,value2,value3)
        cursor.execute(query)
        db.commit()
    def update_user(self,name,dob,pno):
        query=("update user_data set name='{}',dob='{}' where phno={}".format(name,dob,pno))
        cursor.execute(query)
        db.commit()
       
    def delete_user(self,name):
        query=("Delete from user_data  where name='{}'".format(name))
        cursor.execute(query)
        db.commit()
       
    def display_user(self,value):
        query=("select * from user_data where name='{}'".format(value))
        cursor.execute(query)


