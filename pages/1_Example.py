
import streamlit as st

from railib import api
from lib.rai import ctx

st.write("""
# List of Databases

Here is a list of the databases in the RAI account connected to this app:
""")

st.write(api.list_databases(ctx))