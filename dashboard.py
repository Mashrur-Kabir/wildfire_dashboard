import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Page Setup ---
st.set_page_config(page_title="Australia Wildfire Dashboard", layout="wide")

# --- Title ---
st.title("Australia Wildfire Dashboard (2020–2025)")

# --- Load Data ---
DATA_FILE = "australia_wildfire_2020_2025.xlsx"
df = pd.read_excel(DATA_FILE)

# --- Region and Year Selection ---
regions = sorted(df["Region"].unique())
years = sorted(df["Year"].unique())

col_a, col_b = st.columns([2, 1])
with col_a:
    selected_region = st.selectbox("🌏 Select a Region", regions)
with col_b:
    selected_year = st.selectbox("📅 Select a Year", years)

filtered_df = df[(df["Region"] == selected_region) & (df["Year"] == selected_year)]

st.subheader(f"📊 Wildfire Insights for {selected_region} - {selected_year}")

# --- Chart Section ---
if st.session_state.get('screen_width', 1000) >= 992:
    col1, col2 = st.columns(2)
else:
    col1 = st.container()
    col2 = st.container()

# --- Pie Chart ---
with col1:
    st.markdown("### 🔥 Avg. Fire Area (Monthly)")
    pie_data = filtered_df.set_index("Month")["Avg_Fire_Area_km2"]
    fig1, ax1 = plt.subplots(figsize=(4, 4))
    wedges, texts, autotexts = ax1.pie(
        pie_data, autopct='%1.1f%%', startangle=90, radius=1, labels=None
    )
    ax1.axis("equal")

    # Legend on the right
    ax1.legend(wedges, pie_data.index, title="Month", loc="center left", bbox_to_anchor=(1, 0.5))

    st.pyplot(fig1)

# --- Bar Chart ---
with col2:
    st.markdown("### 🌿 Avg. Vegetation Pixel Count (Monthly)")
    bar_data = filtered_df.set_index("Month")["Avg_Veg_Pixel_Count"]
    fig2, ax2 = plt.subplots(figsize=(5, 3))
    bar_data.plot(kind="bar", ax=ax2, color="seagreen")
    ax2.set_ylabel("Pixel Count")
    ax2.set_xlabel("Month")
    ax2.tick_params(axis='x', rotation=45)
    st.pyplot(fig2)
