import mysql.connector
from mysql.connector import pooling
import atexit

# Database configuration
db_config = {
    "host": 'localhost',
    "user": 'root',
    "password": '',
    "port": 3307,
    "database": 'test'
}

# Create a connection pool
pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=32,  # Adjust the pool size as needed
    **db_config
)

# Function to acquire a connection from the pool
def get_connection():
    return pool.get_connection()

# Function to release the connection back to the pool
def release_connection(connection):
    connection.close()

# Register the release_connection function to be called at exit
#atexit.register(release_connection)
