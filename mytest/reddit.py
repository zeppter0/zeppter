import sqlite3

conn = sqlite3.connect('db/reddit.db',check_same_thread=False)


class Reddit:

    def ct_db(self):
        conn = sqlite3.connect('db/reddit.db',echo=True, connect_args={"check_same_thread": False})

        print("Opened database successfully")
    def create_database(self,):
        conn.execute("""CREATE TABLE IF NOT EXISTS Book(Posion INTEGER,Name text);""")
        print("Table created successfully")

        conn.close()


    def creste_col(self,book_p,name ):
        sql = ''' INSERT INTO Book(Posion,Name) VALUES(?,?) '''

        cur =   conn.cursor()
        cur.execute(sql,(book_p,name))
        conn.commit()




    def update(self,book_p,name):
        sql = "UPDATE Book SET Posion = ? WHERE Name = ?"
        cur = conn.cursor()
        cur.execute(sql, (book_p,name))
        conn.commit()



    def select(self,name):
        cur = conn.cursor()
        cur.execute("SELECT * FROM book ")
       # print(cur.fetchone()[0])

        return cur.fetchone()[0]

rd = Reddit()



#rd.create_database()
#rd.creste_col(0,"devan")
#rd.update(0,'devan')
#print(rd.select("devan"))
