import streamlit as st
from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = st.secrets["uri"]

mongo = MongoClient(uri, server_api=ServerApi('1'))

db = mongo.get_database("news")
collection = db.get_collection("summaries")

doc_limit = 3

docs = collection.find().sort("_id", -1).limit(doc_limit)

def print_colored_dict(data):
    for key, value in data.items():
        st.markdown(f"<span style='color:white'>{key}:</span> <span style='color:white'>{value}</span>", unsafe_allow_html=True)


# st.markdown(f'<h1 style="color:white;font-size:24px;">{"ColorMeBlue text”"}</h1>', unsafe_allow_html=True)

for doc in docs:
    # st.write(doc)
    print_colored_dict(doc)