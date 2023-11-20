import streamlit as st


def selector(options: list, label: str, default: str = None):
    selected = st.sidebar.selectbox(label, [option for option in options])
    return selected
