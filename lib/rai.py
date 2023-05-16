
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

def rai_query(query: str, readonly: bool = True):
    rsp = api.exec(
        ctx,
        database=st.secrets["rai"]["database"],
        engine=st.secrets["rai"]["engine"],
        command=query,
        readonly=readonly,
    )
    dfs = [
        relation["table"].to_pandas() for relation in rsp.results
    ]
    return dfs