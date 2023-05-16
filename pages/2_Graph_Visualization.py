
import streamlit as st

from lib.rai import rai_query
from lib.graph import dataframe_graph

st.write("""
## Graph Visualization

Here's an example showing how you can create a graph visualization:


""")
         
query = """
def output = range[1, 8, 1], range[4, 12, 2]
"""

st.code(query)

dfs = rai_query(query)

dataframe_graph(dfs[0])

st.write("""
Here's the same graph in table form:
""")

st.write(dfs[0])