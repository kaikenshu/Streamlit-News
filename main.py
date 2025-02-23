import streamlit as st
from pymongo import MongoClient
from pymongo.server_api import ServerApi

# uri = st.secrets["uri"]
uri = "mongodb+srv://nutrition:tracker@storage.vna8d.mongodb.net/?retryWrites=true&w=majority&appName=Storage"

mongo = MongoClient(uri, server_api=ServerApi('1'))

db = mongo.get_database("news")
collection = db.get_collection("summaries")

st.write(collection.find())