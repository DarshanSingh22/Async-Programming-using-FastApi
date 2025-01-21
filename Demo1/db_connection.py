import pyodbc
import aioodbc

server = 'localhost'
database = 'master'
username = 'sa'
password = 'darshan123'


def execute_query(query):
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          f'SERVER={server};'
                          f'DATABASE={database};'
                          f'UID={username};'
                          f'PWD={password}')
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result 

async def execute_query_async(query):
    dsn = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    conn = await aioodbc.connect(dsn=dsn)
    cursor = await conn.cursor()
    await cursor.execute(query)
    result = await cursor.fetchone()
    await cursor.close()
    await conn.close()
    return result
