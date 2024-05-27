import os
import streamlit as st
import google.generativeai as genai
import sqlite3 as sql

import dotenv

dotenv.load_dotenv()



"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

# genai.configure(api_key=os.environ["GEMINI_API_KEY"])
genai.configure(api_key=st.secrets['GEMINI_API_KEY'])

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    safety_settings=safety_settings,
    generation_config=generation_config,
    system_instruction="You are the SQL query generator for sqlite database having following ERD:\nTables and Columns:\nactor\n\nactor_id (PK)\nfirst_name\nlast_name\naddress\n\naddress_id (PK)\naddress\ncity_id (FK)\npostal_code\ncategory\n\ncategory_id (PK)\nname\ncity\n\ncity_id (PK)\ncity\ncountry_id (FK)\ncountry\n\ncountry_id (PK)\ncountry\ncustomer\n\ncustomer_id (PK)\nstore_id (FK)\nfirst_name\nlast_name\nemail\naddress_id (FK)\nactive\ncreate_date\nfilm\n\nfilm_id (PK)\ntitle\nrelease_year\nlanguage_id (FK)\nrental_duration\nrental_rate\nlength\nreplacement_cost\nrating\nspecial_features\nfilm_actor\n\nactor_id (FK)\nfilm_id (FK)\nfilm_category\n\nfilm_id (FK)\ncategory_id (FK)\ninventory\n\ninventory_id (PK)\nfilm_id (FK)\nstore_id (FK)\nlanguage\n\nlanguage_id (PK)\nname\npayment\n\npayment_id (PK)\ncustomer_id (FK)\nstaff_id (FK)\nrental_id (FK)\namount\npayment_date\nrental\n\nrental_id (PK)\nrental_date\ninventory_id (FK)\ncustomer_id (FK)\nreturn_date\nstaff_id (FK)\nstaff\n\nstaff_id (PK)\nfirst_name\nlast_name\naddress_id (FK)\nemail\nstore_id (FK)\nactive\nusername\npassword\nstore\n\nstore_id (PK)\nmanager_staff_id (FK)\naddress_id (FK)\nRelationships:\nactor has a many-to-many relationship with film through film_actor.\ncategory has a many-to-many relationship with film through film_category.\naddress is related to city through city_id.\ncity is related to country through country_id.\ncustomer is related to store through store_id.\ncustomer is related to address through address_id.\ncustomer has a one-to-many relationship with rental.\ncustomer has a one-to-many relationship with payment.\nfilm is related to language through language_id.\ninventory is related to film through film_id.\ninventory is related to store through store_id.\nrental is related to inventory through inventory_id.\nrental is related to customer through customer_id.\nrental is related to staff through staff_id.\npayment is related to customer through customer_id.\npayment is related to staff through staff_id.\npayment is related to rental through rental_id.\nstaff is related to store through store_id.\nstaff is related to address through address_id.\nstore is related to address through address_id.\nstore is related to staff (manager) through manager_staff_id.\nKeys:\nPK: Primary Key\nFK: Foreign Key",
)
