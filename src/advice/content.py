import streamlit as st
from generate_response.generate_response import update_response

def render_advice():
    """Render the content for the Advice tab"""
    st.header("Advice")
    
    # Simple text area for advice with on_change callback
    st.text_area("Enter advice here", 
                "This is the advice content.",
                height=200,
                key="advice_content",
                on_change=update_response) 