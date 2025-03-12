#=================================
# SWEDEN OLYMPICS DASHBOARD
#=================================


# --- set up ---
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
from read_data import read_olympics_data

# --- Load Data ---
url = "https://en.wikipedia.org/wiki/Sweden_at_the_Olympics"
df = read_olympics_data(url)
#=================================
# DASHBOARD COMPONENTS
#=================================

# Markdown title
st.write("## Sweden Olympic Medal History From 1960s")

## Dropdown list
selected_year = st.selectbox("Select Year", ["All"] + sorted(df["Year"].unique()))


## DataFrame filter by dropdown list
if selected_year != "All":
    filtered_df = df[df["Year"] == selected_year]
else:
    filtered_df = df



st.dataframe(filtered_df.reset_index (drop = True))
## Three graphs
st.write("### Graphs by different libraries")
# by matplotlib
st.write("#### Matplotlib")
fig, ax = plt.subplots()
ax.plot(df["Year"], df["Total"], label="Total Medals", color='blue')
ax.set_xlabel('Year')
ax.set_ylabel('Total Medals')
ax.legend()
plt.xticks(rotation=45)
st.pyplot(fig)
# by plotly_express
st.write("#### Plotly Express")
st.write("#### Plotly Express")
fig2 = px.bar(df, x="Year", y="Total", labels={'Total': 'Total Medals'})
st.plotly_chart(fig2)
# by streamlit native  graph(built in graph)
st.write("#### Streamlit")
st.bar_chart(df.set_index("Year")["Total"])


