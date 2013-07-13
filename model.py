import sqlite3
import re
import datetime

DB = None
CONN = None

class User(object):
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
    
    def get_posts(self):
        sql = "SELECT * FROM Posts where user_id=?"
        posts = DB.execute(sql, (self.id,))

        p_list = []
        for p in posts:
            p = Post(p[0], p[1], p[2], p[3], p[4])
            p_list.append(p)

        return p_list

    def make_post(self, title, body):
        created_at = datetime.datetime.now()
        sql= """INSERT INTO Posts (title, body, user_id, created_at) values (?,?,?,?)"""
        DB.execute(sql, (title, body, self.id, created_at))
        CONN.commit()

class Post(object):
    def __init__(self, id, title, body, user_id, created_at):
        self.id = id
        self.title = title
        self.body = body
        self.user_id = user_id
        self.created_at = created_at


################# Users############################################
def make_user(name, email, password):
    sql= """INSERT INTO Users (name, email, password) values (?,?,?)"""
    DB.execute(sql, (name, email, password))
    CONN.commit()

def get_users():
    sql = "SELECT * FROM Users"
    DB.execute(sql,)
    users = DB.fetchall()
    u_list = []
   
    for u in users:
        u = User(u[0], u[1], u[2], u[3])
        u_list.append(u)
    return u_list

def get_user_by_id(id):
    sql ="SELECT * FROM Users where id = ?"
    DB.execute(sql, (id,))
    user = DB.fetchone()
    u = User(user[0],user[1],user[2],user[3])
    return u


########################Posts################################
# def make_post(title, body, user_id, created_at=datetime.datetime.now()):
#     user = get_user_by_id(user_id)
#     user.make_post(title, body)




####################################################################

def connect():
    global DB, CONN
    CONN = sqlite3.connect("model.db")
    DB = CONN.cursor()

def main():
    connect()
    command = None

    while command != "quit":
        input_string = raw_input("Enter info>")    
        tokens = input_string.split(", ")

        command = tokens[0]
        args = tokens[1:]

        if command == "add_user":
            make_user(*args)
        elif command == "show_users":
            get_users()
        elif command == "make_post":
            make_post(*args)

    CONN.close()

if __name__ == "__main__":
        main()
