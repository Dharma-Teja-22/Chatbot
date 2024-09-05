import pandas as pd
import streamlit as s
import mysql.connector 
import os
from dotenv import load_dotenv
load_dotenv()

# Database connection
mydb = mysql.connector.connect(
    host=os.environ["HOST"],
    user=os.environ['USER'],
    password=os.environ['PASSWORD'],
    database=os.environ['DB_NAME']
)

mycursor = mydb.cursor()

tab1, tab2 = s.tabs(["Data", "Code"])

with tab1:
    sql = "Select * from StudentForm"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    column_names = [column[0] for column in mycursor.description]

# Display the table in Streamlit
    s.table(pd.DataFrame(data, columns=column_names))

with tab2:
    code = '''sql = "Select * from StudentForm"
mycursor.execute(sql)
data = mycursor.fetchall()
column_names = [column[0] for column in mycursor.description]

# Display the table in Streamlit
s.table(pd.DataFrame(data, columns=column_names))'''
    s.code(code, language='python')
