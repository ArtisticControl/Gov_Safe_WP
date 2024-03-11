import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from modules.shared_config import setup_page

setup_page()

st.markdown('## Brazilian Socioeconomic and Health Indicators')

def main():
    st.markdown('### Data Selection and Visualization Preferences')
    # Creating two columns for the menu
    col1, col2, col3 = st.columns((2, 5, 3))
    
    # Adding menu options in the two columns
    with col1:
        selected_date = st.date_input("Preferred Date:", None)
        
    with col2:
        data_type = st.selectbox("Preferred Type of Data:", ["New Cases", "Accumulated Cases", "Other Data"])
        # You can add any other controls or information you want in this column
    
    with col3:
        data_type = st.multiselect("Preferred Variables:", ["State", "Colum1", "Colum2",])
        # Placeholder for any future additions
        pass
    
    # Space
    st.divider()

    # Displaying the map below
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Analysis of Violence Against Women")
        st.markdown("""
        This map visualization highlights geographical distribution of violence against women across Brazil, 
        enabling insights into regional patterns and hotspots.
        """)
        #st.map(braz_df, zoom=3.3, color= '#0044ff')
        df = pd.DataFrame(
            np.random.randn(500, 2) / [0.25, 0.3] + [-13, -50],
            columns=['lat', 'lon'])

        st.map(df, zoom=3, color='#728FCE')

        # Map Data Frame
        braz_df = pd.DataFrame({
            'latitude': [-15],
            'longitude': [-55]
        })


    #Histogram
    with col2:
        st.markdown("#### 'Corruption' in Political Discourse Analysis")
        st.markdown("""
        Explore the presence of 'corruption' within political discourses by party, 
        providing a visual overview of how frequently this theme appears and its potential implications.
        """)
        df = px.data.iris()
        fig = px.scatter(
            df,
            x="sepal_width",
            y="sepal_length",
            color="sepal_length",
            color_continuous_scale="reds",
        )
        tab1, tab2 = st.tabs(["By Decade", "Multiple Tabs can be Added"])
        with tab1:
            st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        with tab2:
            st.plotly_chart(fig, theme=None, use_container_width=True)

    # Another Row
    # Comparative Analysis of Socioeconomic Indicators
    st.markdown("#### Socioeconomic Indicators and Female Life Expectancy")
    st.markdown("""
    This section offers a comparative view of female life expectancy against GDP per capita and population size, 
    highlighting how economic factors correlate with health outcomes across different nations.
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

if __name__ == "__main__":
    main()