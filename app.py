import streamlit as st
import pandas as pd
from utils import *

st.title("Get data from Database.")

question = st.text_input("Enter you question here.")


if question:
    db = sql.connect("D:/Data Science Practices/ai_db_query/data/sqlite-sakila.db/sqlite-sakila.db")
    
    chat_session = model.start_chat(
    history=[]
    )

    response = chat_session.send_message(question)
    
    result1 = pd.read_sql_query(response.text.replace("`", '').replace("sql\n", ""), db)

    st.dataframe(result1)