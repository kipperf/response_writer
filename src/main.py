import streamlit as st
from generate_response.generate_response import get_formatted_response

# Enable debug mode to see more information
st.set_option('client.showErrorDetails', True)

st.title("Response Writer")

# Define tabs
overview, national_standard_paragraphs, advice, notes, auto_response = st.tabs(["Overview", "National Standard Paragraphs", "Advice", "Notes", "Generated Response"])

# Render content for each tab
with overview:
    from overview.content import render_overview
    render_overview()

with national_standard_paragraphs:
    from national_standard_paragraphs.content import render_national_standard_paragraphs
    render_national_standard_paragraphs()

with advice:
    from advice.content import render_advice
    render_advice()

with notes:
    from notes.content import render_notes
    render_notes()

with auto_response:
    from auto_response.content import render_auto_response
    render_auto_response()


