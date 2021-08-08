import mysql.connector
import keyring
from foodsearch import lookup

def connectToDB():
    try:
        cnx = mysql.connector.connect(user='root',
                                      password=keyring.get_password("system","root"),
                                      database='foods')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()

if __name__ == '__main__':
    connectToDB()
    lookup('073007107034')