import mysql.connector
from mysql.connector import errorcode

def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed to create database: {err}")

def main():
    try:
        # Establish a connection to MySQL server
        cnx = mysql.connector.connect(
            user='root',  # replace with your MySQL username
            password='root',  # replace with your MySQL password
            host='localhost'  # replace with your MySQL server address if different
        )
        
        # Create a cursor object
        cursor = cnx.cursor()
        
        # Call the function to create the database
        create_database(cursor)
        
        # Close the cursor and connection
        cursor.close()
        cnx.close()
    
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()