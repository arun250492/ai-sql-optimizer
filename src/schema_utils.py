def connect_to_database(connection_string):
    import sqlalchemy

    engine = sqlalchemy.create_engine(connection_string)
    return engine.connect()

def fetch_table_schema(connection, table_name):
    query = f"SELECT * FROM {table_name} WHERE 1=0"  # Fetching no rows, just the schema
    result = connection.execute(query)
    return [column.name for column in result.cursor.description]

def validate_schema(schema, query):
    # Basic validation logic to check if the query references valid tables and columns
    # This can be expanded based on specific requirements
    for table in schema:
        if table not in query:
            raise ValueError(f"Table {table} not found in query.")
    return True

def get_all_tables(connection):
    query = "SELECT table_name FROM information_schema.tables WHERE table_schema='public'"
    result = connection.execute(query)
    return [row[0] for row in result.fetchall()]