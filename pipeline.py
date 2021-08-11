import mysql.connector 
from mysql.connector import Error
import pandas as pd

csv_data = pd.read_csv(r"C:\Users\Kiran.Kopperla\Downloads/third_party_sales.csv", index_col=False)
print(csv_data.head())


try:
    conn = mysql.connector.connect(user='root',
    password='root',
    host='localhost',
    database='tickets_system')

    if conn.is_connected():
        mycursor = conn.cursor()
        mycursor.execute("select database();")
        record = mycursor.fetchone()
        print("You are conntecte to database", record)
        mycursor.execute("DROP TABLE IF EXISTS ticket_sales")
        print("creating table ...")
        mycursor.execute("""CREATE TABLE ticket_sales(
            ticket_id INT, 
            trans_date DATE,
            event_id INT,
            event_name VARCHAR(100), 
            event_date DATE, 
            event_type VARCHAR(30), 
            event_city VARCHAR(30), 
            customer_id INT, 
            price DECIMAL,
            num_tickets INT
            )""")

        print("table is created...")

        for i, row in csv_data.iterrows():
            
            sql = "INSERT INTO tickets_system.ticket_sales VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            mycursor.execute(sql,tuple(row))
            # print("Record inserted")

            conn.commit()

except Error as e:
    print("Error while connecting to database", e)


# sql = "SELECT * FROM ticket_sales"
# mycursor.execute(sql)

# result = mycursor.fetchall()
# for i in result:
#     print(i)


def query_popular_tickets():
# Get the most popular ticket in the past month
    sql_statement = "SELECT event_name FROM ticket_sales ORDER BY num_tickets DESC LIMIT 3"
    cursor = conn.cursor()
    cursor.execute(sql_statement)
    records = cursor.fetchall()
    cursor.close()
    return records

tkt = query_popular_tickets()
for i in tkt:
    print(tkt)
    print(f'-{tkt[0]}')

# print('\n'.join([i for i in str(tkt[1:])]))


# mydb = mysql.connector.connect(
#     user = "root",
#     password = "root",
#     host = "localhost",
#     database = "tickets_system"
# )

# mycursor = mydb.cursor()

# # mycursor.execute("CREATE DATABASE IF NOT EXISTS tickets_system")

# # mycursor.execute("SHOW DATABASES")

# # for db in mycursor:
# #     print(db)


# mycursor.execute("""CREATE TABLE IF NOT EXISTS ticket_sales(
#     ticket_id INT, 
#     trans_date INT,
#     event_name VARCHAR(50), 
#     event_date DATE, 
#     event_type VARCHAR(10), 
#     event_city VARCHAR(20), 
#     customer_id INT, 
#     price DECIMAL,
#     num_tickets INT
#     )""")

# mycursor.execute("SHOW TABLES")

# for tb in mycursor:
#     print(tb)



# def get_connection():
#     connection = None
#     try:
#         connection = mysql.connector.connect(user='root',
#         password='root',
#         host='localhost',
#         port='3306',
#         database='<database name>')
#     except Exception as error:
#         print("Error while connecting to database for job tracker", error)
#     return connection





# from mysql.connector import connect, Error
# from pyspark.sql import SparkSession

# spark = SparkSession.builder.getOrCreate()


# schema = StructType([
#   StructField("trans_date", DateType(), nullable=False),
#   StructField("ticket_id", IntegerType(), nullable=False),
#   StructField("event_name", StringType(), nullable=True),
#   StructField("event_date", DateType(), nullable=True),
#   StructField("event_type", StringType(), nullable=True),
#   StructField("event_city", StringType(), nullable=True),
#   StructField("cust_id", IntegerType(), nullable=False),
#   StructField("price", FolatType(), nullable=False),
#   StructField("num_of_tkts", IntegerType(), nullable=False),
# ])
# csv_ticket_sales = spark.read.schema(schema).csv("third_party_sales.csv")

# csv_ticket_sales.show()

# try:
#     with connect(
#         host="localhost",
#         user="root",
#         password="root",
#         port='3306'
#     ) as connection:
#         create_db_query = "CREATE DATABASE IF NOT EXISTS ticket_system"
#         create_table_query = """
#                             CREATE TABLE IF NOT EXISTS ticket_sales (ticket_id INT, 
#                                                                         trans_date INT, 
#                                                                         event_id INT,
#                                                                         event_name VARCHAR(50), 
#                                                                         event_date DATE, 
#                                                                         event_type VARCHAR(10), 
#                                                                         event_city VARCHAR(20), 
#                                                                         customer_id INT, 
#                                                                         price DECMAL,
#                                                                         num_tickets INT)
#                             """
#         with connection.cursor() as cursor:
#             cursor.execute(create_db_query)
#             cursor.execute(create_table_query)
        

# except Error as e:
#     print(e)