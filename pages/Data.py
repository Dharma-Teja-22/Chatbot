
import pandas as pd
import streamlit as s


tab1, tab2 = s.tabs(["Data", "Code"])

with tab1:
    data = pd.read_csv("annual-enterprise-survey-2023-financial-year-provisional.csv")
    s.write(data)

with tab2:
    code = '''data = pd.read_csv("fileName.csv")
s.write(data)'''
    s.code(code, language='python')
