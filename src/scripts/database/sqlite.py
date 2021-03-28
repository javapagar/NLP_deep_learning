import sqlite3

class SqliteDB():
    
    con= None
    cursorObj = None
    def __init__(self, dbPath,foreign_keys = True):
        self.dbPath=dbPath
        self.foreign_keys = foreign_keys

    def connect(self):
        try:
            self.con=sqlite3.connect(self.dbPath)
            if self.foreign_keys:
                self.executeQuery("PRAGMA foreign_keys = ON")
            print("Connection Opened")
        except :
            print("Connection KO")
    
    def close(self):
        try:
            self.con.close
            print("Connection closed")
        except:
            pass
    
    def executeQuery(self,query, params= None):
        resp =None

        if self.con != None and self.cursorObj == None :
            self.cursorObj = self.con.cursor()

        try:

            if params != None:
                resp = self.cursorObj.execute(query,params)
            else:
                resp =self.cursorObj.execute(query)

            self.con.commit()
            return resp
        except sqlite3.Error as er:
            print("error al ejecutar:",query)
            print(' '.join(er.args))
            return None
    