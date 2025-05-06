import os
import psycopg2

def main():
    host = os.environ.get("POSTGRES_HOST", "localhost")
    port = os.environ.get("POSTGRES_PORT", "5432")
    user = "postgres"
    password = "postgres"
    dbname = "postgres"

    conn = psycopg2.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        dbname=dbname
    )

    with conn.cursor() as cur:
        cur.execute("SELECT version()")
        result = cur.fetchone()
        print(f"PostgreSQL Version: {result[0]}")

if __name__ == "__main__":
    main()
