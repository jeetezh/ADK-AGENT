import sqlite3
from typing import List, Any,Dict,Tuple
from mcp.server.fastmcp import FastMCP

DB_PATH = "C:\\Users\\admin\\OneDrive\\Desktop\\Google-adk\\local\\database.db"
mcp = FastMCP("SQLite FastMCP Server")


def get_conn() -> sqlite3.Connection:
    """Return a fresh connection (SQLite connections are not thread‑safe)."""
    return sqlite3.connect(DB_PATH)

# LIST TABLES
@mcp.tool()
def list_tables() -> List[str]:
    """
    This function List all user‑defined tables in the connected SQLite database.

    returns:
    list of table from currebt database
    """
    query = """
        SELECT name FROM sqlite_master
        WHERE type='table' AND name NOT LIKE 'sqlite_%';
    """
    conn=get_conn()

    cursor=conn.cursor()
    cursor.execute(query)
    tables=cursor.fetchall()
    conn.close()
    return [table[0] for table in tables]


# delete table
@mcp.tool()
def delete_table(table: str) -> str:
    """
    Delete all rows from a specified table.

    Args:
        table (str): The name of the table to delete rows from.

    Returns:
        str: A message indicating how many rows were deleted.
    """
    conn = get_conn()
    cursor = conn.cursor()
    
    # Delete all rows from the specified table
    cursor.execute(f"DROP TABLE IF EXISTS {table}")
    row_count = cursor.rowcount
    
    conn.commit()
    conn.close()
    
    return f"Deleted {row_count} rows from '{table}'."


@mcp.tool()
def create_table(table: str, columns: List[str]) -> str:
    """
    Create a new table with the specified name and columns.

    Args:
        table (str): The name of the new table.
        columns (List[str]): A list of column definitions (e.g., "id INTEGER PRIMARY KEY", name VARCHAR etc.).

    Returns:
        str: A message indicating whether the table was created successfully.
    """
    conn = get_conn()
    cursor = conn.cursor()
    
    # Create the table with the specified columns
    column_definitions = ", ".join(columns)
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table} ({column_definitions})")
    
    conn.commit()
    conn.close()
    
    return f"Table '{table}' created successfully."

#insert row
@mcp.tool()
def insert_row(table: str, values: Dict[str,Any]) -> str:
    """
    Insert a new row into the specified table.
    Args:
        table (str): The name of the table to insert into.
        values (Dict[str, Any]): A dictionary where keys are column names and values are the data to insert.
        Returns:
        str: A message indicating whether the row was inserted successfully."""
    conn= get_conn()
    cursor = conn.cursor()
    # Prepare the SQL statement
    columns = ', '.join(values.keys())  
    placeholders = ', '.join(['?'] * len(values))
    query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
    # Execute the SQL statement with the provided values
    cursor.execute(query, tuple(values.values()))
    conn.commit()
    conn.close()
    return f"Inserted row into '{table}' with values: {values}"

#view data
@mcp.tool()
def view_rows(table: str) -> Tuple[List[str], List[Tuple]]:
    """
    View all rows in the specified table.

    Args:
        table (str): The name of the table to view.

    Returns:
        Tuple[List[str], List[Tuple]]: A tuple containing:
            - A list of column names in the table.
            - A list of tuples, each representing a row in the table.
    """
    conn = get_conn()
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    
    conn.close()
    return column_names, rows
    


# GREETING
@mcp.tool()
def greet(name: str) -> str:
    """
    Return a friendly greeting.
    """
    return f"Hello, {name}! SQLite tools are ready."


def main():
    mcp.run()  # STDIO transport by default


if __name__ == "__main__":
    main()
