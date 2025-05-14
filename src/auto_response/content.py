import streamlit as st
from generate_response.generate_response import update_response
from generate_response.generate_response import get_formatted_response

def render_auto_response():
    """Render the content for the Auto Response tab"""

    st.write(get_formatted_response())