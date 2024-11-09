
import mysql.connector
from utility.niche_details import host,db_credential

def get_database_connection(niche):
    db_connection = mysql.connector.connect(
    host = host,
    user = db_credential[niche]['user'],
    password = db_credential[niche]['password'],
    database = db_credential[niche]['database'],
    )

    db_cursor = db_connection.cursor()

    return db_connection, db_cursor
