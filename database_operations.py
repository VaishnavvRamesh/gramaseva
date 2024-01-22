import sqlite3
import os

class database_operations():
    def __init__(self):

        # Database path
        self.db_path = 'database/user_db.db'
        
        # Table name
        self.table_name = 'user_info'
        
        # Database connection
        self.conn = None

        # Create table if not exits
        self.create_table()
    

    def create_table(self):
        '''
        1. Create "database" folder if not present
        2. Create database table if not present
        '''
        try:
            if not os.path.isdir('database'):
                os.mkdir('database')
                print('database folder created')

            self.connect_db()
            query = f"create table if not exists {self.table_name} (name char(1000), age int, gender char(1), contact_no int, username char(1000) primary key not null, password char(1000) not null);"
            self.conn.execute(query)

            self.conn.close()
            print('Table created successfully')
        except Exception as e:
            print(f'Exception while creating table - {str(e)}')


    def connect_db(self):
        '''
        1. Create connection with database
        '''
        try:
            self.conn = sqlite3.connect(self.db_path)
            print('Connection established successfully with database.')
        except Exception as e:
            print(f'Database connection exception - {e}')
        

    def validate_user(self,username,pwd):
        '''
        1. Validate if user exists in database or not while login
        '''
        try:
            query = f"select * from {self.table_name} where username = '{username}' and password = '{pwd}'"

            res = self.conn.execute(query)

            for row in res:
                return [True,row[0]]  # Valid user

            return [False,'Invalid user']  # Invalid user

        except Exception as e:
            print(f'Exception while validating username and password while login - {str(e)}')
            return [False,str(e)]


    def is_user_exit(self,data):
        '''
         validate if username is already present in database while signup
        '''
        try:
            query = f"select * from {self.table_name} where username = '{data['username']}'"

            res = self.conn.execute(query)

            for row in res:
                return [True,'Username already exist!! select another username'] # username exist

            return [False,'Username does not exit'] # username not exist
        except Exception as e:
            print(f'Exception while valdating username - {str(e)}')
            return [False,str(e)]


    def add_user(self,data):
        
        try:
            query = f"insert into {self.table_name} (name, age, gender, contact_no, username, password) values ('{data['name']}',{data['age']},'{data['gender']}',{data['phone']},'{data['username']}','{data['password']}')"
            res = self.conn.execute(query)
            self.conn.commit()

            return 'Account created successfully!'
        except Exception as e:
            print(f'Exception while adding user to database - {str(e)}')
            return str(e)

    
