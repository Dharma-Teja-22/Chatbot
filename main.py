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

def storeData(data):
    sql = "INSERT INTO StudentForm(Name, age, Gender, PocketMoney) VALUES (%s, %s, %s, %s)"
    try:
        mycursor.execute(sql, data)
        mydb.commit()
        return "Data inserted successfully"
    except Exception as e:
        return f"An error occurred: {e}"

s.title("Welcome to Streamlit Application")

s.subheader("Application Form")
# s.markdown("Streamlit is an open-source Python library that allows for the creation of web apps for data science and machine learning projects with ease.")
# text = s.chat_input()

name = s.text_input("Name", "")
age = s.slider("How old are you?", 0, 130, 10)
gender = s.radio("Gender", ["male", "Female", "others"])
salary = s.number_input("Enter your Pocket Money", step=1)

option = s.multiselect(
    "How would you like to be connected?",
    ("Email", "Home phone", "Mobile phone"),
)
des = s.text_area("Any feedbacks ...")

ex = s.checkbox("I agree!")

clicked = s.button("Submit")

if clicked:
    if ex:  # Check if the user agreed
        s.write("Name = ", name)
        s.write("Age = ", age)
        s.write("Gender = ",  gender)
        s.write("Pocket Money = ", salary)
        res = storeData((name, age, gender, salary))
        s.write(res)
        if(res == "Data inserted successfully"):
            s.page_link("pages/Login_To_GPT.py", label="Go to GPT")
    else:
        s.warning("You need to agree before submitting the form!")

# s.link_button("Route..", "gpt")
# s.page_link("pages/gpt.py", label="Go to GPT")

# col1, col2 = s.columns(2)
# col1.header("Left Side")
# col2.header("Right Side")
