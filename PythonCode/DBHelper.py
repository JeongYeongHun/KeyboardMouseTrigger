import sqlite3

def insert(name, w, a, s, d, shift, c, alt, tab, space, one, two, three, esc, mousemove, e, q):
    conn = sqlite3.connect("key.db")
    cur = conn.cursor()
    sql = "insert into key(name, w, a, s, d, shift, c, alt, tab, space, one, two, three, esc, lclick, rclick, mousemove, e, q) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cur.execute(sql, (name, w, a, s, d, shift, c, alt, tab, space, one, two, three, esc, 'lclick', 'rclick', mousemove, e, q))
    conn.commit()
    conn.close()

def load(num):
    conn = sqlite3.connect("key.db")
    cur = conn.cursor()
    sql = "select * from key where id=?"
    cur.execute(sql, (num,))
    row = cur.fetchone()
    conn.close()
    return row

def list():
    conn = sqlite3.connect("key.db")
    cur = conn.cursor()
    cur.execute("select id,name from key")
    rows = cur.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    print("test code")
    
    rows = list()
    print ("list : ", rows, "\n")

    row = load(1)
    print ("load : ", row, "\n")
