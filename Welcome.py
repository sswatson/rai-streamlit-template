
import streamlit as st

from railib import api
from lib.rai import ctx

print(api.list_databases(ctx))

st.write("""
Welcome to the RelationalAI Streamlit starter template!

To get started, check out the repo's `README.md` file.
""")