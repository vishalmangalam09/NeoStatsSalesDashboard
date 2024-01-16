import streamlit as st
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

from streamlit_option_menu import option_menu
import dashboardd, Add_data
st.set_page_config(page_title="Neostats sales Prospect", page_icon=":chart_with_upwards_trend:", layout="wide")

def creds_entered():
    if st.session_state["user"].strip() == "admin" and st.session_state["passwd"].strip() == "admin":
        st.session_state["authenticated"] = True
    else:
        st.session_state["authenticated"] = False
        st.error("invalid")


def authenticate_user():
    if "authenticated" not in st.session_state:
        st.text_input(label="Username :", value="", key="user", on_change=creds_entered)
        st.text_input(label="Password :", value="", key="passwd", type="password", on_change=creds_entered)

        return False
    else:
        if st.session_state["authenticated"]:
            return True
        else:
            st.text_input(label="Username :", value="", key="user", on_change=creds_entered)
            st.text_input(label="Password :", value="", key="passwd", type="password", on_change=creds_entered)
            return False


if authenticate_user():
    
    

    st.sidebar.image("neostats.jpg", caption="NeoStats Analytics Solutions PVT LTD")
    st.header("Neostats Sales Prospect")
    st.markdown('', unsafe_allow_html=False)

    def run():
        with st.sidebar:
            app = option_menu(
                menu_title='Menu',
                options=['dashboard', 'Add Record'],
                icons=['person-circle'],
                menu_icon='N',
                default_index=0,
                styles={
                    "container": {"padding": "2!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "15px"},
                    "nav-link": {"color": "white", "font-size": "15px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        if app == "Add Record":
            Add_data.app()
        elif app == "dashboard":
            dashboardd.app()

    run()



