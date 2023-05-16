
import streamlit as st

from railib import api
from lib.rai import ctx
from lib.graph import dataframe_graph

st.write("""
## Graph Visualization

Here's an example showing how you can create a graph visualization:


""")
         
query = """
def output = range[1, 8, 1], range[4, 12, 2]
"""

st.code(query)

rsp = api.exec(
    ctx,
    database="foobar",
    engine="hello-rel",
    command=query,
)

dfs = [relation["table"].to_pandas() for relation in rsp.results]

dataframe_graph(dfs[0])

st.write("""
Here's the same graph in table form:
""")

st.write(dfs[0])