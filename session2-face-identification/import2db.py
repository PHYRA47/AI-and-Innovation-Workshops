# Docker connection
# docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=my-secret-pw -e MYSQL_DATABASE=images_db -e MYSQL_USER=my_user -e MYSQL_PASSWORD=my_password -p 3306:3306 -d mysql:latest

import mysql.connector
from mysql.connector import Error
from PIL import Image
import io
import os

# MySQL connection details
mysql_config = {
    "host": "localhost",
    "user": "my_user",
    "password": "my_password",
    "port": 3306
}

def connect_without_db():
    return mysql.connector.connect(**mysql_config)

def connect_with_db(database_name):
    return mysql.connector.connect(database=database_name, **mysql_config)

def create_database(cursor, db_name):
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        print(f"Database '{db_name}' created or exists already.")
    except Error as e:
        print(f"Error creating database: {e}")

def create_table(cursor):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS images_store (
        id INT AUTO_INCREMENT PRIMARY KEY,
        image_name VARCHAR(255) UNIQUE,
        image_column LONGBLOB
    );
    """
    try:
        cursor.execute(create_table_query)
        print("Table created or exists already.")
    except Error as e:
        print(f"Error creating table: {e}")

def read_image(image_path):
    with Image.open(image_path) as img:
        img_byte_array = io.BytesIO()
        img.save(img_byte_array, format=img.format)
        img_byte_array = img_byte_array.getvalue()
    return img_byte_array

def image_exists(cursor, image_name):
    try:
        cursor.execute("SELECT image_name FROM images_store WHERE image_name = %s", (image_name,))
        return cursor.fetchone() is not None  # Returns True if image_name exists, False otherwise
    except Error as e:
        print(f"Error checking image existence: {e}")
        return False

def insert_image_to_db(cursor, image_name, image_data):
    try:
        cursor.execute("""
            INSERT INTO images_store (image_name, image_column) 
            VALUES (%s, %s)
        """, (image_name, image_data))
        print(f"Image '{image_name}' inserted into the database.")
    except Error as e:
        print(f"Error inserting image: {e}")

def main():
    db_name = "images_db"

    # Create database and table
    conn = connect_without_db()
    cursor = conn.cursor()

    create_database(cursor, db_name)
    cursor.close()
    conn.close()

    conn = connect_with_db(db_name)
    cursor = conn.cursor()

    create_table(cursor)

    # Insert images
    images_folder = "images/t2/faces"  # Path to the folder containing images

    for filename in os.listdir(images_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            image_path = os.path.join(images_folder, filename)
            image_name = os.path.splitext(filename)[0]  # Get filename without extension

            if not image_exists(cursor, image_name):
                image_data = read_image(image_path)
                insert_image_to_db(cursor, image_name, image_data)
            else:
                print(f"Image '{image_name}' already exists in the database, skipping insertion.")

    conn.commit()
    cursor.close()
    conn.close()

    print("Database setup complete.")

if __name__ == "__main__":
    main()
