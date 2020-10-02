import sqlite3 as sl
import pandas as pd
import os.path
from os import path


# Do You Know Python Has A Built-In Database?
# https://towardsdatascience.com/do-you-know-python-has-a-built-in-database-d553989c87bd

# Create and connect to database
con = None
def create_db():
    con = sl.connect('my-test.db')
    return con


# Create a Table
def create_table():
    with con:
        con.execute("""
            CREATE TABLE USER (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER
            );
        """)

# Insert Records
def insert_records():
    sql = 'INSERT INTO USER (id, name, age) values(?, ?, ?)'
    data = [
        (1, 'Alice', 21),
        (2, 'Bob', 22),
        (3, 'Chris', 23)
    ]
    with con:
        con.executemany(sql, data)

# Query the Table
def query_table():
    with con:
        data = con.execute("SELECT * FROM USER WHERE age <= 22")
        for row in data:
            print(row)

# Seamless Integrate with Pandas
'''
We even don’t need to create the table in advance, the column data types and length will be inferred. Of course, you can still define it beforehand if you want to.
'''
def create_table_with_df():
    df_skill = pd.DataFrame({
        'user_id': [1,1,2,2,3,3,3],
        'skill': ['Network Security', 'Algorithm Development', 'Network Security', 'Java', 'Python', 'Data Science', 'Machine Learning']
    })

    df_skill.to_sql('SKILL', con)

# join the table USER and SKILL, and read the result into a Pandas data frame. 
def join_table_and_df():
    df = pd.read_sql('''
        SELECT s.user_id, u.name, u.age, s.skill 
        FROM USER u LEFT JOIN SKILL s ON u.id = s.user_id
    ''', con)

    df.to_sql('USER_SKILL', con)


con = create_db()
create_table_with_df()