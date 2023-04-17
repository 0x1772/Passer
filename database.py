import sqlite3

class DatabaseManager:
    def __init__(self, database_filename):
        self.connection = sqlite3.connect(database_filename)

    def __del__(self):
        self.connection.close()

    def create_table(self, table_name, columns):
        columns_with_types = [f"{column_name} {data_type}" for column_name, data_type in columns.items()]
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns_with_types)})"
        self.connection.execute(query)
        self.connection.commit()

    def add(self, table_name, data):
        placeholders = ", ".join(["?"] * len(data))
        column_names = ", ".join(data.keys())
        query = f"INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})"
        self.connection.execute(query, tuple(data.values()))
        self.connection.commit()

    def delete(self, table_name, criteria):
        placeholder_values = tuple(criteria.values())
        criteria_with_placeholders = " AND ".join([f"{key} = ?" for key in criteria.keys()])
        query = f"DELETE FROM {table_name} WHERE {criteria_with_placeholders}"
        self.connection.execute(query, placeholder_values)
        self.connection.commit()

    def select(self, table_name, criteria=None, order_by=None):
        query = f"SELECT * FROM {table_name}"
        placeholder_values = None
        if criteria:
            criteria_with_placeholders = " AND ".join([f"{key} = ?" for key in criteria.keys()])
            query += f" WHERE {criteria_with_placeholders}"
            placeholder_values = tuple(criteria.values())
        if order_by:
            query += f" ORDER BY {order_by}"
        cursor = self.connection.execute(query, placeholder_values)
        return cursor.fetchall()
