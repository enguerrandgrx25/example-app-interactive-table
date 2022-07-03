# import module
import streamlit as st
import pandas as pd
import numpy as np

import notion_df

st.set_page_config(
    page_title="Cyber Motion by Cynait",
    page_icon="👋",
)

# Title
st.write("""
# Historique
Hello *cyber analyst*""")


data = {'Nom':  ['Détection d’un ransomware', 'Impression de document confidentiel ',
"Export de données depuis une librairie confidentiel "],
        'Date': ['22/6/2022', '14/6/2022', "17/6/2022"],
        "Risk score": ['8', '6', "3"]
        }

## Get data from Notion
page_url = "https://www.notion.so/c7ade621ac57491ab4e17a9d8ce01d5d?v=5e82aacac0f94d6ba5ae736aaa17a03f"
api_key = "secret_y1reuQYpSgvNA13TKfzKm7Azk9mU4u78dexTXqaPdFi"


df = notion_df.download(page_url, api_key=api_key)


st.line_chart(df)

#df = pd.DataFrame(data)

#st.dataframe(df)
