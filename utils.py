import sqlite3

def insertfile(id, file_name , security_key):
    conn = sqlite3.connect('ds.db')
    try:
        
        cursor = conn.cursor()
        cursor.execute('insert into files (id , file_name,security_key) values(?,?,?)',(id, file_name, security_key))
        conn.commit()
        conn.close()
        return True
    except:
        return False
    finally:
        try:
            conn.close()
        except:
            pass
    