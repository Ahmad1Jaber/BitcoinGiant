import mysql.connector
import status
from abc import ABCMeta,abstractstaticmethod

class DBConncection(metaclass=ABCMeta):

    @abstractstaticmethod
    def request():
        """API Request Interface"""

    #Initiate Connection
class conn(DBConncection):
    config = {
        'user': 'root',
        'password': 'Aamkaj@1998',
        'host': '104.154.25.152',
        'database': 'bitcoingiant',
    }
    # now we establish our connection
    cnxn = mysql.connector.connect(user = 'root',password='Aamkaj@1998',host = '104.154.25.152',database= 'bitcoingiant',)
    def request(self):
        return self.cnxn

class connectAgent():
    #Call Connection
    @staticmethod
    def connect():
        try:
            connect = conn()
            connection= connect.request()
            print(f"{status.bcolors.OK}(+) Connected to Database{status.bcolors.RESET}")
            return connection
            raise AssertionError("Failed to connect")
        except AssertionError as _e:
            print(_e) 
def connection():
    conn=connectAgent.connect()
    result = conn.execute("")
    return result
if __name__ == "__main__":
    """Main Section"""
    connect = connectAgent.connect()
    mydb = connect.cursor()
    # result = mydb.execute("Select * From newsAPI")
    # print(result)
    #dbConnection.close()