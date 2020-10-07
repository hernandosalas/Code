# Python has a Built-in Database — Here’s How to use it
# https://towardsdatascience.com/python-has-a-built-in-database-heres-how-to-use-it-47826c10648a

import sqlite3 

# The movies.db database will get created if it doesn’t exist, and if it does, only a connection gets established.
conn = sqlite3.connect('movies.db') 
c = conn.cursor()

# Next, we’ll declare a function that checks if a table exists. The table name gets passed as a function parameter, and it returns True if the table exists, and False otherwise
def table_exists(table_name): 
    c.execute('''SELECT count(name) FROM sqlite_master WHERE TYPE = 'table' AND name = '{}' '''.format(table_name)) 
    if c.fetchone()[0] == 1: 
        return True 
    return False

# Create table if doesn't exist
if not table_exists('movies'): 
    c.execute(''' 
        CREATE TABLE movies( 
            movie_id INTEGER, 
            name TEXT, 
            release_year INTEGER, 
            genre TEXT, 
            rating REAL 
        ) 
    ''')

# To start, we need a function that inserts a movie to the table (the Create part). It is quite an easy one to write, as we need to execute a single INSERT statement and commit the transaction. Here’s the code
def insert_movie(movie_id, name, release_year, genre, rating): 
    c.execute(''' INSERT INTO movies (movie_id, name, release_year, genre, rating) VALUES(?, ?, ?, ?, ?) ''', (movie_id, name, release_year, genre, rating)) 
    conn.commit()


# fetching all of the movies
def get_movies(): 
    c.execute('''SELECT * FROM movies''') 
    data = [] 
    for row in c.fetchall(): 
        data.append(row) 
    return data

# fetch a single movie
def get_movie(movie_id): 
    c.execute('''SELECT * FROM movies WHERE movie_id = {}'''.format(movie_id)) 
    data = [] 
    for row in c.fetchall():  
        data.append(row) 
    return data

# Update movie by id
# Our update function will accept two parameters:
#       movie ID — the ID of a movie you want to update
#       update dictionary — key/value pairs to update
def update_movie(movie_id, update_dict): 
    valid_keys = ['name', 'release_year', 'genre', 'rating'] 
    for key in update_dict.keys():  
        if key not in valid_keys: 
            raise Exception('Invalid field name!') 
    for key in update_dict.keys(): 
        if type(update_dict[key]) == str: 
            stmt = '''UPDATE movies SET {} = '{}' WHERE movie_id = {}'''.format(key, update_dict[key], movie_id) 
        else: 
            stmt = '''UPDATE movies SET {} = '{}' WHERE movie_id = {}'''.format(key, update_dict[key], movie_id) 
        c.execute(stmt) 
    conn.commit()

# Delete movie by id
def delete_movie(movie_id): 
    c.execute('''DELETE FROM movies WHERE movie_id = {}'''.format(movie_id)) 
    conn.commit()

# DRIVER CODE
insert_movie(1, 'Titanic', 1997, 'Drama', 7.8) 
insert_movie(2, 'The Day After Tomorrow', 2004, 'Action', 6.4) 
insert_movie(3, '2012', 2009, 'Action', 5.8) 
insert_movie(4, 'Men in Black', 1997, 'Action', 7.3) 
insert_movie(5, 'World War Z', 2013, 'Romance', 10)

print(get_movies())

# Let’s now get only a single movie
print(get_movie(2))

# Now we’ll see how to update a movie
update_movie(5, {'genre': 'Horror', 'rating': 7.0})

# The only thing left to do is to delete a movie
delete_movie(3)