import streamlit as st
import folium
import pandas as pd
import plost
from streamlit_folium import folium_static
from modules.shared_config import setup_page
import plotly.express as px

setup_page()

st.title("Gender Related Useful Indicators")

gdi = pd.read_csv("data/gdi/gdi.csv")
max_gdi = gdi["Gender Development Index (2021)"].max()
seattle_weather = pd.read_csv('data/seattle-weather.csv', parse_dates=['date']) #scraps

# ===============================
st.markdown("### Global Gender Development Index (GDI) Map")
st.markdown("""
This interactive map displays the Gender Development Index (GDI) for countries around the world, allowing users to explore changes over time. The GDI measures disparities between men and women in terms of health, knowledge, and living standards.
""")

# User selects a year for the map
selected_year_for_map = st.select_slider(
    "Select Year for Map:",
    options=[str(year) for year in range(1990, 2022)],
    value='2021',
    key='map_year_slider'
)
selected_year_for_map = int(selected_year_for_map)  # Convert to integer
max_gdi_selected_year = gdi[f"Gender Development Index ({selected_year_for_map})"].max()

bins_list = sorted(set([0.4, 0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1, 1.02, max_gdi_selected_year]))

# Prepare the data for the selected year
gdi_selected_year = gdi[["Country", f"Gender Development Index ({selected_year_for_map})"]].dropna()

# Initialize the map with no repeated world copies
m = folium.Map(location=(30, 10), zoom_start=2.35, tiles="cartodb positron", no_wrap=True)

# Add the Choropleth layer using the bins_list for the selected year
folium.Choropleth(
    geo_data="data/countries.geojson",
    data=gdi_selected_year,
    columns=["Country", f"Gender Development Index ({selected_year_for_map})"],
    key_on="feature.properties.name",
    bins=bins_list,
    fill_color="RdYlBu",
    fill_opacity=0.8,
    line_opacity=0.3,
    nan_fill_color="white",
    legend_name=f"Gender Development Index ({selected_year_for_map})",
).add_to(m)

folium.LayerControl().add_to(m)
folium_static(m)

#To select a specific data
country, year, result = st.columns(3)
with country:
    country = st.selectbox("*For Specific Data, Select a Country:*", gdi['Country'].unique())

with year:    
    year = st.slider("*And Select a Year:*", 1990, 2021)

with result:
    # Filter data based on user selections
    filtered_gdi = gdi[gdi['Country'] == country]
    gdi_value = filtered_gdi[f'Gender Development Index ({year})'].values[0]
    # Display GDI value for the selected country
    st.write("*Result:*")
    st.write(f"For **{country}** in **{year}**, the GDI score was **{gdi_value}**.")
        
# ================================================

st.markdown("")


# Row B
st.markdown("### Comparative Analysis of Female Life Expectancy, GDP per Capita, and Population Size")
st.markdown("""
This scatter plot offers a comparative analysis of key socio-economic indicators: female life expectancy, GDP per capita, and total population size across countries.
Such visualizations help in identifying patterns and correlations between women's health, economic development, and demographic dynamics.
""")

df = px.data.gapminder()

fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)
st.plotly_chart(fig, theme="streamlit", use_container_width=True)

line_chart, heatmap = st.columns(2)
with line_chart:
    #Row B: Two Columns Plus Line Chart
    st.markdown('## Trend Analysis Over Time')
    st.markdown("""
    Explore how selected indicators change over time. This line chart allows you to visualize trends, helping identify patterns or shifts
    in key areas such as gender violence, the GDI, Corruption Perception Index, and female education levels etc. Adjust the chart's height for a tailored view.
    """)

    cross_stats, line_height=st.columns((4,6))
    with cross_stats:
        plot_data = st.multiselect('*Select data*', ['gender violence', 'gdi', 'cpi', 'female education'], ['gdi', 'cpi'])
        
    with line_height:
        plot_height = st.slider('*Select plot height*', 200, 350, 250)

    st.line_chart(seattle_weather, x = 'date', y = plot_data, height = plot_height)

with heatmap:    
    time_hist_color = 'gdi'
            
    st.markdown('## Heatmap for Temporal Patterns')
    st.markdown("""
    This heatmap provides a visual representation of activity levels across weeks and days, using the selected color metric. It's an effective tool for identifying temporal patterns, such as periods of higher or lower activity in the dataset provided.
    """)
    plost.time_hist(
        data=seattle_weather,
        date='date',
        x_unit='week',
        y_unit='day',
        color=time_hist_color,
        aggregate='median',
        legend=None,
        height=270,
        use_container_width=True
    )