import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="phonebook",
        user="postgres",
        password="Amikosha2007",
        host="localhost",
        port="5432"
    )