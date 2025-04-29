import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Setup ---
st.set_page_config(page_title="AUS Wildfire Overview", layout="wide")

# --- Header ---
st.title("Australia Wildfire Dashboard")

# --- Load Data ---
DATA_FILE = "australia_wildfire_2020_2025.xlsx"
df = pd.read_excel(DATA_FILE)

# --- User Selection ---
regions = sorted(df["Region"].unique())
years = sorted(df["Year"].unique())

left_col, right_col = st.columns([2, 1])
with left_col:
    selected_region = st.selectbox("Select Region", regions)
with right_col:
    selected_year = st.selectbox("Select Year", years)

subset = df[(df["Region"] == selected_region) & (df["Year"] == selected_year)]

st.markdown(f"### Overview for **{selected_region}** in **{selected_year}**")

# --- Pie Chart: Fire Area by Month ---
st.markdown("#### 🔥 Fire Spread Distribution by Month")
fire_area_data = subset.set_index("Month")["Avg_Fire_Area_km2"]

fig1, ax1 = plt.subplots(figsize=(6, 6))
# Use distinct color palette for better contrast
distinct_colors = [
    "#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00",
    "#ffff33", "#a65628", "#f781bf", "#999999", "#66c2a5",
    "#fc8d62", "#8da0cb"
]

wedges, texts, autotexts = ax1.pie(
    fire_area_data,
    autopct='%1.1f%%',
    startangle=140,
    radius=1.1,
    colors=distinct_colors[:len(fire_area_data)],
    textprops={'fontsize': 8, 'color': 'black'},
    labels=None
)
ax1.axis("equal")
ax1.set_title("Avg Fire Area by Month", fontsize=12, fontweight='bold')
ax1.legend(wedges, fire_area_data.index, title="Month", loc="center left", bbox_to_anchor=(1, 0.5))
st.pyplot(fig1)

# --- Bar Chart: Vegetation by Month ---
st.markdown("#### 🌱 Vegetation Health by Month")
veg_data = subset.set_index("Month")["Avg_Veg_Pixel_Count"]

fig2, ax2 = plt.subplots(figsize=(9, 4))

bar_colors = [
    "#1b9e77", "#d95f02", "#7570b3", "#e7298a", "#66a61e",
    "#e6ab02", "#a6761d", "#666666", "#8dd3c7", "#ffffb3",
    "#bebada", "#fb8072"
]

bars = ax2.bar(veg_data.index, veg_data.values, color=bar_colors[:len(veg_data)], edgecolor='black', linewidth=0.5)
ax2.set_ylabel("Pixel Count", fontsize=10)
ax2.set_xlabel("Month", fontsize=10)
ax2.set_title("Average Vegetation Pixel Count", fontsize=12, fontweight='bold')
ax2.tick_params(axis='x', rotation=45)

for bar in bars:
    height = bar.get_height()
    ax2.annotate(f'{height}',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom', fontsize=8)

st.pyplot(fig2)
