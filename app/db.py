import mysql.connector
import os

def get_connection():
    host = os.getenv("MYSQL_HOST", "localhost")
    user = os.getenv("MYSQL_USER", "root")
    password = os.getenv("MYSQL_PASSWORD", "yg123654")
    database = os.getenv("MYSQL_DATABASE", "weapon_db")


    conn = mysql.connector.connect(
        host=host, user=user, password=password, database=database
    )
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weapons (
            id INT AUTO_INCREMENT PRIMARY KEY,
            weapon_id VARCHAR(255),
            weapon_name VARCHAR(255),
            weapon_type VARCHAR(255),
            range_km INT,
            weight_kg FLOAT,
            manufacturer VARCHAR(255),
            origin_country VARCHAR(255),
            storage_location VARCHAR(255),
            year_estimated INT,
            risk_level VARCHAR(50)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()