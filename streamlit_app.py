# import module
import streamlit as st
import pandas as pd
import numpy as np


import notion_df

from PIL import Image


st.set_page_config(
    page_title="Cyber Motion by CYNA-IT",
    page_icon="👋",
)

image = Image.open('cyna.jpg')

st.image(image)

# Title
st.write("""
# Cyber Motion by CYNA-IT
Hello *cyber analyst*""")


## Get data from Notion
page_url = "https://www.notion.so/c7ade621ac57491ab4e17a9d8ce01d5d?v=5e82aacac0f94d6ba5ae736aaa17a03f"
api_key = "secret_y1reuQYpSgvNA13TKfzKm7Azk9mU4u78dexTXqaPdFi"


df = notion_df.download(page_url, api_key=api_key)
# Equivalent to: df = pd.read_notion(notion_database_url, api_key=api_key)

df = df[['Name', 'Date', 'Risk Score']]
df['Date'] = df['Date'].apply(lambda x: str(x).split()[0])
#st.dataframe(df)

def color_risk(val):
    #val = int(val)
    color = "gold"
    if(val == "Critique"):
        color = 'red'
    elif(val == "Majeur"):
        color = 'orange'
    elif(val == "Modere"):
        color = "gold"
    else:
     color = 'blue'
    return f'background-color: {color}'


if("Critique" in df["Risk Score"].to_list()):
    st.error("Alert vous avez une intrusion critique")

st.markdown('##')
st.markdown('##')
st.markdown('##')


# Inject CSS with Markdown

df = df.sort_values(['Risk Score'], ascending=False).reset_index(drop=True).style.applymap(color_risk, subset=['Risk Score'])



# CSS to inject contained in a string
hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)



st.dataframe(df)

st.markdown('##')
st.markdown('##')
st.markdown('##')

col1, col2, col3 = st.columns(3)

col1.metric("Number of tracked assets", 10, 10 - 5)
col2.metric(
    "Squirrels per hectare",
    round(10 / 350, 2),
    round((10 - 2373) / 350, 2))
col3.metric("Number of primary colors", 3)

#df = pd.DataFrame(data)
