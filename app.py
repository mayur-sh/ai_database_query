import streamlit as st
import pandas as pd
from utils import *

st.title("Get data from Database.")

st.page_link("https://raw.githubusercontent.com/mayurzlr/ai_query_db/main/data/SakilaDatabaseERD.png", label="Database ERD🔗")

question = st.text_input("Enter you question here.")


if question:
    db = sql.connect("data/sqlite-sakila.db/sqlite-sakila.db")
    
    chat_session = model.start_chat(
    history=[]
    )

    response = chat_session.send_message(question)
    
    result1 = pd.read_sql_query(response.text.replace("`", '').replace("sql\n", ""), db)

    st.dataframe(result1)
