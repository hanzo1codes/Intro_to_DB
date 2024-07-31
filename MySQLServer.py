import mysql.connector
from mysql.connector import Error


def create_database():
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="your_username",  # Replace with your MySQL username
            password="your_password",  # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            try:
                # Attempt to create the database
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except mysql.connector.Error as db_error:
                print(f"Failed to create database: {db_error}")
            finally:
                cursor.close()

    except mysql.connector.Error as conn_error:
        print(f"Error connecting to MySQL: {conn_error}")

    finally:
        if "connection" in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")


if __name__ == "__main__":
    create_database()
