import streamlit as st
from PIL import Image
import pandas as pd
import openai
import plotly.express as px

# Local imports
from subgraphs.subgraph import SubGraph
from nlp_models.gpt import GPT
from nlp_models.gpt_training import add_graphQL_examples
from metamask_component import metamask_component

from keys.private_keys import OPENAI_PRIVATE_KEY, THEGRAPH_API_KEY

from etherscan.etherscan_data import Etherscan_scan
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

# CSS
with open("styles/style.css", "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

@st.cache
def load_gpt3_model():
    openai.api_key = OPENAI_PRIVATE_KEY
    gpt = GPT(engine="davinci", temperature=0.5, max_tokens=100)
    add_graphQL_examples(gpt)
    return gpt

def json_to_df(raw_json):
    df = pd.DataFrame(columns=["token","similar_symbol","percentage"])
    for x in raw_json.keys():
        pre = {}
        pre["token"] = x
        for y in raw_json[x].keys():
            if y == "percentage":
                raw_json[x][y] = round( float(raw_json[x][y] * 100),2)
            pre[y] = raw_json[x][y]
        df = df.append(pre, ignore_index=True)
    df = df.rename(columns={"percentage": "similarity", "token": "token_owner", "similar_symbol": "similar_token"})
    return df
# -----------------------------------------------------------
# Main Section
# -----------------------------------------------------------
# GPT
gpt = load_gpt3_model()

# Metamask
value = metamask_component(account_results="hello there")

subgraph_response = {}
query = ""
actual_query = ""
image = Image.open(
    "/Users/gerardogodfreyc/Documents/Proyectos/ETH_Hackaton/eth-mexico/media/waphl_logo.png"
)
st.image(image, use_column_width=True)


st.markdown("## Search:")
text_query = st.text_input(
    label="",
    placeholder="give me the id, exact, decimals and simple for the first 7 metrics in the mStable protocol subgraph",
)
query_action = st.button("Run Search")

if query_action:  # if pressed
    if value:
        #raw_query = gpt.submit_request(text_query).choices[0].text.split("output: ")[-1] # gpt
        raw_query = "uniswap-v2{pairs(first: 9, where: {reserveETH_gt: '100000'}, orderBy: reserveETH, orderDirection: desc) {reserveUSD}}"
        subgraph_response, actual_query = query_subgraph(raw_query)
        st.code(actual_query)

        results_tab, json_results_tab, query_code_tab = st.tabs(["Results", "Code Results", "Query"])

        # Tabs section
        with results_tab:
            if subgraph_response:
                prettify_json(subgraph_response)
                # We need to make the prettify_json func

        with json_results_tab:
            st.json(subgraph_response)

        with query_code_tab:
            st.code(actual_query)

    else:
        st.error('Connect the wallet', icon="🚨")




#Balance

with st.expander("Balance and recomenndations"):
    
    if value :
        st.markdown("### Wallet:")
        st.write(value)
        c1 = Etherscan_scan(value,testing=True)
        st.markdown("### Balance:")
        st.write(c1.get_json_balance())

        st.markdown("### Recomendation:")
        raw_json = {
            'GEL': {'similar_symbol': 'APE', 'percentage': 0.39872121810913086},
            'SUSHI': {'similar_symbol': 'UNI', 'percentage': 0.5800848007202148},
            'SNX': {'similar_symbol': 'HEX', 'percentage': 0.34170082211494446},
            'DAI': {'similar_symbol': 'APE', 'percentage': 0.5156382918357849},
            'APE': {'similar_symbol': 'DAI', 'percentage': 0.5156382918357849}
        }
        df_data = json_to_df(raw_json)
        st.markdown("#### Description similarity:")
        table, plot,recommendation = st.tabs(["table", "plot","recommendation"])
        with table:
            st.table(data= df_data)
        with plot:
            fig = px.bar(df_data, x='token_owner', y='similarity', color='similar_token')
            st.plotly_chart(fig)
        with recommendation:
            df_data = df_data.sort_values(by='similarity', ascending=False)
            row_1=df_data.iloc[0]
            a = row_1['token_owner']
            b = row_1['similar_token']
            c = row_1['similarity']
            dont = ["HEX","BNB","USDT","SHIBA","APE","WBTC","Matic","DAI"]
            st.write(f"For this model, we find that the cryptocurrency {a} you have is a {c} similar to {b}.") 
            if b not in dont:
                st.write(f"{b} It does have a subgraph in The graph !!! Look for browsing in it on this page ")
            else:
                st.write(f"{b} It does not have a subgraph in The graph !!! Look for browsing in it on this page:")
                st.write("https://thegraph.com/docs/en/cookbook/quick-start/")

         
        st.markdown("#### Social Trends :")
        st.table(data= df_data) 
        st.markdown("#### Similar Protocol:")
        st.table(data= df_data) 

    else:
        st.write("Sin datos actualizados")

