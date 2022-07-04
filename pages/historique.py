# import module
import streamlit as st
import pandas as pd
import numpy as np

import notion_df
import seaborn as sns
import matplotlib.pyplot as plt



st.set_page_config(
    page_title="Cyber Motion by Cynait",
    page_icon="👋",
)

# Title
st.write("""
# Historique
Hello *cyber analyst*""")



## Get data from Notion
page_url = "https://www.notion.so/c7ade621ac57491ab4e17a9d8ce01d5d?v=5e82aacac0f94d6ba5ae736aaa17a03f"
api_key = "secret_y1reuQYpSgvNA13TKfzKm7Azk9mU4u78dexTXqaPdFi"


df = notion_df.download(page_url, api_key=api_key)
# Equivalent to: df = pd.read_notion(notion_database_url, api_key=api_key)

df = df[['Name', 'Date', "Risk Score"]]
df['Date'] = df['Date'].apply(lambda x: str(x).split()[0])

fig = plt.figure(figsize=(10, 4))
sns.countplot(x="Risk Score", data=df, palette="Set2")
st.pyplot(fig)


df_test = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df_test['first column'])

'You selected: ', option


import streamlit as st

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

#df = pd.DataFrame(data)

#st.dataframe(df)
