
import pandas as pd

from streamlit_agraph import agraph, Node, Edge, Config

def dataframe_graph(df: pd.DataFrame, edge_label: str = None):
    df = df.applymap(str) # you can get JSON serializability errors otherwise
    col1name = df.columns[0]
    col2name = df.columns[1]
    unique_nodes = set(df[col1name].to_list() + df[col2name].to_list())
    nodes = [
        Node(
            id=entry,
            size=20,
        )
        for entry in unique_nodes
    ]
    edges = []
    for _, row in df.iterrows():
        edges.append(
            Edge(
                source=row[col1name],
                target=row[col2name],
                label=edge_label,
            )
        )
    config = Config(
        width=750,
        height=450,
        directed=True,
        hierarchical=False,
        timestep=0.25,
    )

    agraph(nodes=nodes, edges=edges, config=config)