import streamlit as st

def setup_page():
    """
    Sets up the page configuration and loads the CSS.
    """
    st.set_page_config(
        layout="wide",
        page_title="GovSafe: Sextortion Mitigation WebApp",
        page_icon="https://raw.githubusercontent.com/ArtisticControl/assets/main/favicon.png",
        initial_sidebar_state="expanded"
    )

    # Load the CSS from the external stylesheet
    with open("css/style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # Bottom of Sidebar Configuration
    st.sidebar.markdown("**Developed by:** [Dr Fernando Forattini](https://fernandoforattini.com)" + "\n**Supported by:**")
    st.sidebar.image("https://raw.githubusercontent.com/ArtisticControl/assets/main/symeco_lero.png", use_column_width=True)
