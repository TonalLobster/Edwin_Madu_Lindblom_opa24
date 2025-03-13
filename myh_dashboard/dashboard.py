# =========================
# MYH dashboard
# =========================

# --- set up ---
import streamlit as st
from read_data import read_data # from a module, import a function
from kpis import number_approved, total_applications, approved_percentage

# --- reading data ---
df = read_data()

# --- dashboard components ---
#title
st.markdown("# YH dashboard 2024 application")

st.markdown("This is a simple dashboard about higher vocational education in Sweden (yrkeshögskola). The results from the education can me filtered in this dashboard")


#kpi components
st.markdown("## KPIs in Sweden")

labels = ("Total applications", "Number of approved", "Approved percentage")
kpis = (total_applications, number_approved, approved_percentage)
cols = st.columns(3)

for col, label, kpi in zip(cols, labels, kpis):
    with col:
        st.metric(label=label, value = kpi)

#data table
st.markdown("## Raw Data")
st.dataframe(df)
