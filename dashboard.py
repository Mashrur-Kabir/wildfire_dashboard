import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Page Setup ---
st.set_page_config(page_title="Australia Wildfire Dashboard", layout="wide")
st.title("🔥 Australia Wildfire Dashboard (2025)")

# --- Load Data from Excel File ---
DATA_FILE = "australia_wildfire_2025.xlsx"  # Ensure this file is in the same directory
df = pd.read_excel(DATA_FILE)

# --- Sidebar Filter ---
st.sidebar.header("🌏 Select Region")
regions = sorted(df["Region"].unique())
selected_region = st.sidebar.radio("Region", regions)

# Filter based on selected region
filtered_df = df[df["Region"] == selected_region]

# --- Pie Chart: Average Estimated Fire Area by Month ---
st.subheader(f"🔥 Monthly Average Estimated Fire Area in 2025 — {selected_region}")
pie_data = filtered_df.set_index("Month")["Avg_Fire_Area_km2"]
fig1, ax1 = plt.subplots()
ax1.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90)
ax1.axis("equal")
st.pyplot(fig1)

# --- Bar Chart: Average Vegetation Pixel Count by Month ---
st.subheader(f"🌿 Average Vegetation Pixel Count per Month in 2025 — {selected_region}")
bar_data = filtered_df.set_index("Month")["Avg_Veg_Pixel_Count"]
fig2, ax2 = plt.subplots()
bar_data.plot(kind="bar", ax=ax2, color="green")
ax2.set_ylabel("Pixel Count")
ax2.set_xlabel("Month")
st.pyplot(fig2)
