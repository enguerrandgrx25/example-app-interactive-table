# import module
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import notion_df

from PIL import Image


st.set_page_config(
    page_title="Cyber Motion by CYNA-IT",
    page_icon="👋",
)

image = Image.open('cyna.jpg')

st.image(image)

# Title
st.title("Cyber Motion by CYNA-IT")
st.caption("Nous analysons en permanance le traffic et l'activité de votre SI pour detecter toute tentative d'intrusion")



st.header("Page 1 - Settings")
st.markdown('##')
st.markdown('##')


ransomware = st.checkbox("Voulez vous bloquer automatiquement les intrusions de type Ransomware")
if ransomware:
     st.info('Nous allons bloquer tout les Ransomware !')

doss = st.checkbox("Voulez vous bloquer automatiquement les attaques de type DosS")
if doss:
     st.info('Nous allons bloquer tout les Doss !')

secu_grp = st.checkbox("Avez vous des postes plus sensibles que d'autres ?  ")
if secu_grp:
     st.info('Nous vous informerons en cas de fuite de données sur les postes sensibles !')

data = st.checkbox("Voulez etre alerte pour les fuite de données ")
if data:
     st.info('Nous allons vous alerter  pour les fuite de données !')



#st.checkbox(label, value=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False)
#st.checkbox(label, value=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False)


st.header("Page 2 - Intrusion detection dashboard")

## Get data from Notion
page_url = "https://www.notion.so/c7ade621ac57491ab4e17a9d8ce01d5d?v=5e82aacac0f94d6ba5ae736aaa17a03f"
api_key = "secret_y1reuQYpSgvNA13TKfzKm7Azk9mU4u78dexTXqaPdFi"


df_all = notion_df.download(page_url, api_key=api_key)
# Equivalent to: df = pd.read_notion(notion_database_url, api_key=api_key)

df_all = df_all[['Name', 'Date', 'Risk Score', "Status", "Asset Name"]]
df_all['Date'] = df_all['Date'].apply(lambda x: str(x).split()[0])


df_open = df_all[df_all["Status"] == "Open"]
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

st.markdown('##')
st.markdown('##')

if("Critique" in df_open["Risk Score"].to_list()):
    st.error("Alert vous avez une intrusion Critique")

elif("Majeur" in df_open["Risk Score"].to_list()):
    st.warning("Alert vous avez une intrusion Majeur")

elif("Modere" in df_open["Risk Score"].to_list()):
    st.info("Alert vous avez une intrusion Modere")

else:
    st.succes("Vous n'avez pas d'alerte grave")

st.markdown('##')
st.markdown('##')




# Inject CSS with Markdown

df_sort = df_open.sort_values(['Risk Score'], ascending=False).reset_index(drop=True).style.applymap(color_risk, subset=['Risk Score'])
df_sort_all = df_all.sort_values(['Risk Score'], ascending=False).reset_index(drop=True).style.applymap(color_risk, subset=['Risk Score'])



# CSS to inject contained in a string
hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)


if st.checkbox('Display close alert'):
    st.dataframe(df_sort_all)
else:
    st.dataframe(df_sort)



st.markdown('##')
st.markdown('##')



st.header("Page 3 - Statistic over the week")
st.subheader("Type of alerte")
fig = plt.figure(figsize=(10, 4))
sns.countplot(x="Risk Score", data=df_all)
st.pyplot(fig)

st.subheader("Asset touché")
fig = plt.figure(figsize=(10, 4))
sns.countplot(x="Asset Name", data=df_all)
st.pyplot(fig)

st.header("Page 4 - Statistic on IS")
col1, col2, col3 = st.columns(3)

col1.metric("Number of detected intrussion", len(df_all), len(df_all) - 5)
col2.metric(
    "Tracked assets",
    round(20),
    round(10-5))
col3.metric("Number of ...", 3)

st.markdown('##')
st.markdown('##')

#df = pd.DataFrame(data)
