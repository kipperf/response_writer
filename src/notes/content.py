import streamlit as st
from generate_response.generate_response import update_response

def render_notes():
    """Render the content for the Notes tab"""
    st.header("Notes")
    
    # Simple text area for notes with on_change callback
    st.text_area(label="Enter your notes here", 
                value="No Notes Provided",
                height=200,
                key="notes_content",
                on_change=update_response) 