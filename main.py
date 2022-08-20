import streamlit as st
from PIL import Image
import pandas as pd

# Local imports
from subgraphs.subgraph import SubGraph
from keys.private_keys import THEGRAPH_API_KEY

# -----------------------------------------------------------
# Aux Functions
# -----------------------------------------------------------


def clean_query(raw_query):
    subgraph = raw_query.split("{")[0]
    query = raw_query.split(subgraph)[-1].replace("'", '"')
    return subgraph, query


def query_subgraph(raw_query):
    # GPT3 part missing! add it here plz

    subgraph, query = clean_query(raw_query)
    subgraph = SubGraph(subgraph, api_key=THEGRAPH_API_KEY)
    return subgraph.run_query(query), query


def prettify_json(ugly_json):
    for data_point in ugly_json["data"]:
        st.subheader(data_point)
        if isinstance(ugly_json["data"][data_point], list):
            pretty_df = pd.DataFrame(ugly_json["data"][data_point])
            st.dataframe(pretty_df)
            st.download_button(
                "Download", pretty_df.to_csv(index=False), mime="text/csv"
            )
        else:
            st.write(ugly_json["data"][data_point])


# -----------------------------------------------------------
# Main Section
# -----------------------------------------------------------

subgraph_response = {}
query = ""
actual_query = ""
image = Image.open(
    "/Users/robertoyamanaka/Documents/EthHack/gpt3_testing/media/google_logo.png"
)
st.image(image, use_column_width=True)
text_query = st.text_input(
    label="",
    placeholder="give me the id, exact, decimals and simple for the first 7 metrics in the mStable protocol subgraph",
)
query_action = st.button("Run Search")

if query_action:  # if pressed
    st.write("pressed")
    raw_query = "uniswap-v2{pairs(first: 9, where: {reserveETH_gt: '100000'}, orderBy: reserveETH, orderDirection: desc) {reserveUSD}}"
    subgraph_response, actual_query = query_subgraph(raw_query)

results_tab, json_results_tab, query_code_tab = st.tabs(
    ["Results", "Code Results", "Query"]
)

# Tabs section
with results_tab:
    if subgraph_response:
        prettify_json(subgraph_response)
        # We need to make the prettify_json func


with json_results_tab:
    st.json(subgraph_response)

with query_code_tab:
    st.code(actual_query)
