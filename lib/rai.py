
import streamlit as st

from railib import api
from railib.credentials import ClientCredentials

ctx = api.Context(
    host=st.secrets["rai"]["host"],
    credentials=ClientCredentials(
      st.secrets["rai"]["client_id"],
      st.secrets["rai"]["client_secret"],
    )
)